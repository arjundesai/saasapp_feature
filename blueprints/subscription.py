from flask import Blueprint, request, jsonify
from pydantic import BaseModel, EmailStr, ValidationError
from models.subscription import db, Subscription

subscription_bp = Blueprint('subscription', __name__)

# Pydantic schema for validating subscription data
class SubscriptionSchema(BaseModel):
    name: str
    email: EmailStr
    subscription_plan: str

# POST: Subscribe route
@subscription_bp.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        data = SubscriptionSchema(**request.get_json())  # Pydantic validation
        
        # Check if email already exists
        if Subscription.query.filter_by(email=data.email).first():
            return jsonify({"error": "Email already subscribed"}), 400

        # Create new subscription
        new_subscription = Subscription(
            name=data.name,
            email=data.email,
            subscription_plan=data.subscription_plan
        )

        db.session.add(new_subscription)
        db.session.commit()

        return jsonify({"message": "Subscription created successfully!"}), 201

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# GET: Get subscription status by email
@subscription_bp.route('/subscription-status/<email>', methods=['GET'])
def subscription_status(email):
    subscription = Subscription.query.filter_by(email=email).first()

    if not subscription:
        return jsonify({"error": "Subscription not found"}), 404

    return jsonify({
        "name": subscription.name,
        "email": subscription.email,
        "subscription_plan": subscription.subscription_plan,
        "is_active": subscription.is_active
    }), 200
