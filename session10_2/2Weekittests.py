import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Panel
from 2Weekitbackend import app.py, db


class TestQuery(unittest.TestCase):
    
    engine = create_engine('sqlite:///:memory:')
    db = SQLAlchemy()
    Session = sessionmaker(bind=engine)
    session = Session()

    def create_test_app():
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "xxxxxxtestdatabasexxx"
        # Dynamically bind SQLAlchemy to application
        db.init_app(app)
        app.app_context().push() # this does the binding
        return app
        
    def setUp(self):
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()
            self.populate_db()

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.drop_all()

    def query_test(self):
        Base.metadata.create_all(self.engine)
        expected = [Users(1, 'usamapuri', 'Usama', '12345678', 'usamapuri@gmail.com')]
        result = self.session.query(Users).all()
        self.assertEqual(result, expected)
    
    def add_task_test(self):
        Base.metadata.create_all(self.engine)
        self.session.add(Tasks(1, 'Marathon' , 'Run a Marathon')
        expected = [Tasks(1, 'Marathon' , 'Run a Marathon')]
        self.assertEqual(result, expected)
    


if __name__ == '__main__':
    unittest.main()
