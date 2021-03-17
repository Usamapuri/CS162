from sqlalchemy import create_engine, orm, Column, Integer, String,ForeignKey, Text, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime as DateTime
from sqlalchemy.ext.indexable import index_property


base  = declarative_base()

engine = create_engine('sqlite:///bankloans.db', echo=True)
engine.connect()


class Clients(base):
    __tablename__ = 'Clients'
    id = Column(Integer, primary_key = True)
    first_name = Column(Text)
    sur_name = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    first_sur_name = index_property('first_name', 'sur_name')
    name_data =index_property('first_name', 'email', 'phone')
    
    def __repr__(self):
        return "<Clients(id={0}, first_name={1}, sur_name={2}, email ={3}, phone ={4})>".format(self.id, self.first_name, self.sur_name, self.email, self.phone)
        
class Loans(base):
    __tablename__ = 'Loans'
    account_id = Column(Integer, unique=True)
    client_number = Column(Integer, ForeignKey(Clients.id), primary_key = True)
    start_date = Column(Text)
    start_month = Column(Text)
    term = Column(Integer)
    remaining_term = Column(Integer)
    principal_debt = Column(Integer)
    account_limit = Column(Integer)
    balance = Column(Integer)
    status = Column(Text)

    def __repr__(self):
        return '''<Loans(account_id = {0},client_number= {1},start_date= {2},start_month= {3},term= {4},remaining_term= {5}, principal_debt= {6},account_limit= {7},balance= {8},status= {9})>'''.format(self.account_id,self.client_number, self.start_date, self.start_month, self.term, self.principal_debt,self.account_limit,self.balance,self.status)



base.metadata.create_all(bind = engine)
Session = sessionmaker(bind = engine)
session = Session()

session.add(Clients(id = 1, first_name = 'Robert', sur_name = 'Warren', email = 'RobertDWarren@teleworm.us', phone = 251546-9442))
session.add(Clients(id = 2, first_name = 'Vincent', sur_name = 'Brown', email = 'VincentHBrown@rhyta.com', phone = 251546-9442))
session.add(Clients(id = 3, first_name = 'Janet', sur_name = 'Prettyman', email = 'JanetTPrettyman@teleworm.us', phone = 251546-9442))
session.add(Clients(id = 4, first_name = 'Martin', sur_name = 'Kershner', email = 'MartinaMKershner@rhyta.com', phone = 251546-9442))
session.add(Clients(id = 5, first_name = 'Tony', sur_name = 'Schroeder', email = 'TonySSchroeder@teleworm.us', phone = 251546-9442))
session.add(Clients(id = 6, first_name = 'Harold', sur_name = 'Grimes', email = 'HaroldVGrimes@dayrep.com', phone = 251546-9442))

session.add(Loans(account_id = 1, client_number= 1, start_date= '2017-11-01 10:00:00', start_month= '201712', term= 36, remaining_term= 35, principal_debt= 10000, account_limit= 15000, balance= 9800,status = 'Normal'))
session.add(Loans(account_id = 2, client_number= 2, start_date= '2018-01-01 10:00:00', start_month= '201802', term= 24, remaining_term= 24, principal_debt= 1000, account_limit= 1500, balance= 1000,status= 'Normal'))
session.add(Loans(account_id = 3, client_number= 1, start_date= '2016-11-01 10:00:00', start_month= '201612', term= 12, remaining_term= -3, principal_debt= 2000, account_limit= 15000, balance= 4985,status= 'Arrears'))
session.add(Loans(account_id = 4, client_number= 3, start_date= '2018-01-01 10:00:00', start_month= '201802', term= 12, remaining_term= 24, principal_debt= 3500, account_limit= 5000, balance= 1300,status= 'Normal'))
session.add(Loans(account_id = 5, client_number= 4, start_date= '2017-11-01 10:00:00', start_month= '201712', term= 12, remaining_term= 35, principal_debt= 10000, account_limit= 15000, balance= 0,status= 'PAID OFF'))
session.add(Loans(account_id = 6, client_number= 5, start_date= '2018-01-01 10:00:00', start_month= '201802', term= 28, remaining_term= 24, principal_debt= 1000, account_limit= 1500, balance= 0,status= 'PAID OFF'))
session.add(Loans(account_id = 7, client_number= 6, start_date= '2015-11-01 10:00:00', start_month= '201512', term= 12, remaining_term= -20, principal_debt= 10000, account_limit= 15000, balance= 9800,status= 'Arrears'))
session.add(Loans(account_id = 7, client_number= 4, start_date= '2018-01-01 10:00:00', start_month= '201802', term= 12, remaining_term= 1, principal_debt= 2400, account_limit= 3600, balance= 130,status= 'Normal'))

session.commit()