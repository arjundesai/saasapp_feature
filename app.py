from flask import Flask
from config import Config
from models.subscription import db
from blueprints.subscription import subscription_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db.init_app(app)

# Register the subscription blueprint
app.register_blueprint(subscription_bp)

# Use Flask's application startup event for table creation
# @app.before_first_request
@app.before_request
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
