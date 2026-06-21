from .database import db #dot means look in current directory, since db is intiallized here in the database.py file
                         # whereas no dot means look for database in the root directory

class User(db.model):