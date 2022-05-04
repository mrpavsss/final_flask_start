# """testing users"""
# import logging
#
# #from faker import Faker
# from app import db
# from app.db.models import User, Transaction
#
# def test_adding_user(application):
#     """adding transactions"""
#     log = logging.getLogger("myApp")
#     with application.app_context():
#         assert db.session.query(User).count() == 0
#         assert db.session.query(Transaction).count() == 0
#         #showing how to add a record
#         #create a record
#         user = User('keith@webizly.com', 'testtest', is_admin=True)
#         #add it to get ready to be committed
#         db.session.add(user)
#         #call the commit
#         #db.session.commit()
#         #assert that we now have a new user
#         #assert db.session.query(User).count() == 1
#         #finding one user record by email
#         user = User.query.filter_by(email='keith@webizly.com').first()
#         log.info(user)
#         #asserting that the user retrieved is correct
#         assert user.email == 'keith@webizly.com'
#         #this is how you get a related record ready for insert
#         user.transactions= [Transaction("test","smap","2000","living"),
#                               Transaction("test2","te","2000","living")]
#         #commit is what saves the transactions
#         db.session.commit()
#         #assert db.session.query(Transaction).count() == 2
#         transaction1 = Transaction.query.filter_by(comapny='test').first()
#         assert transaction1.company == "test"
#         #changing the title of the transaction
#         transaction1.company = "SupertransactionTitle"
#         #saving the new title of the transaction
#         db.session.commit()
#         transaction2 = Transaction.query.filter_by(company='SupertransactionTitle').first()
#         assert transaction2.title == "SupertransactionTitle"
#         #checking cascade delete
#         db.session.delete(user)
#         assert db.session.query(User).count() == 0
#         assert db.session.query(Transaction).count() == 0
