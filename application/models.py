from .database import db #dot means look in current directory, since db is intiallized here in the database.py file
                         # whereas no dot means look for database in the root directory

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable = False)
    email = db.Column(db.String(), unique=True, nullable = False)
    password = db.Column(db.String(), nullable = False)
    type = db.Column(db.String(), nullable = False, default="user")
    requests = db.relationship("Request", backref="user")

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    cost = db.Column(db.Integer(), nullable=False)
    status = db.Column(db.String(), nullable=False, default="available")
    requests = db.relationship("Request", backref="product")

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey("product.id"), nullable=False)
    status = db.Column(db.String(), nullable=False, default="requested")