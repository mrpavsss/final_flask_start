"""testing users"""
import logging

#from faker import Faker
from app import db
from app.db.models import User, Transaction

def test_adding_user(application, client):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        user = User('keith@webizly.com', 'testtest', is_admin=True)
        db.session.add(user)
        user = User.query.filter_by(email='keith@webizly.com').first()
        log.info(user)
        assert user.email == 'keith@webizly.com'
        user.transactions = [Transaction(2000, 'CREDIT')]
        db.session.commit()
        #assert db.session.query(Song).count() == 2
        rec1 = Transaction.query.filter_by(amount=2000).first()
        assert rec1.amount == 2000

        db.session.delete(user)
        db.session.delete(rec1)
        db.session.commit()
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
