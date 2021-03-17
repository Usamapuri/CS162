from sqlalchemy import create_engine, orm, Column, Integer, String,ForeignKey, Text, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime as DateTime
from sqlalchemy.ext.indexable import index_property


base  = declarative_base()

engine = create_engine('sqlite:///bankloans.db', echo=True)
engine.connect()

class Customer(base):
    __tablename__ = 'Customer'
    customer_id = Column(Integer, primary_key = True)
    first_name = Column(Text)
    sur_name = Column(Text)
    address1 = Column(Text)
    address2 = Column(Text)
    address3 = Column(Text)    
    email = Column(Text)
    phone = Column(Text)
    first_sur_name = index_property('first_name', 'sur_name')
    name_data =index_property('first_name', 'email', 'phone')

class Product(base):
    __tablename__ = 'Product'
    product_id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    price = Column(Integer)
    cost = Column(Integer)

class Orders(base):
    __tablename__ = 'Orders'
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey(Customer.customer_id), primary_key=True)
    order_date = Column(Text)
    order_month = Column(Integer)

class OrderItem(base):
    __tablename__ = 'OrderItem'
    order_id = Column(Integer, ForeignKey(Orders.order_id), primary_key=True)
    product_id = Column(Integer, ForeignKey(Product.product_id), primary_key=True)
    quantity = Column(Integer)

class WareHouse(base):
    __tablename__ = 'WareHouse'
    ware_id = Column(Integer, primary_key=True)
    name = Column(Text)
    address1 = Column(Text)
    address2 = Column(Text)
    address3 = Column(Text)

class Inventory(base):
    __tablename__ = 'Inventory'
    ware_id = Column(Integer, ForeignKey(WareHouse.ware_id), primary_key=True)
    product_id = Column(Integer, ForeignKey(Product.product_id), primary_key=True)
    quantity = Column(Integer)

class Supplier(base):
    __tablename__ = 'Supplier'
    supplier_id = Column(Integer, primary_key=True)
    name = Column(Text)
    address1 = Column(Text)
    address2 = Column(Text)
    address3 = Column(Text)
    email = Column(Text)
    phone = Column(Text)

class supplierProduct(base):
    __tablename__ = 'SupplierProduct'
    supplier_id= Column(Integer, ForeignKey(Supplier.supplier_id), primary_key = True)
    product_id = Column(Integer, ForeignKey(Product.product_id), primary_key=True)
    daysleadtime = Column(Integer)
    cost = Column(Integer)

class supplierOrders(base):
    __tablename__ = 'SupplierOrder'
    supplier_id= Column(Integer, ForeignKey(Supplier.supplier_id), primary_key = True)
    product_id = Column(Integer, ForeignKey(Product.product_id), primary_key=True)
    ware_id = Column(Integer, ForeignKey(WareHouse.ware_id), primary_key=True)
    quantity = Column(Integer)
    status = Column(Text)
    dateordered = Column(Text)
    datedue = Column(Text)



    
    def __repr__(self):
        return "<Clients(id={0}, first_name={1}, sur_name={2}, email ={3}, phone ={4})>".format(self.id, self.first_name, self.sur_name, self.email, self.phone)


base.metadata.create_all(bind = engine)
Session = sessionmaker(bind = engine)
session = Session()

session.add(Product(3001, "Widget", "Widge all your worries away!", 99.95, 23.05))
session.add(Product(3002, "Wodget", "Wodge all your worries away!", 199.95, 123.05)

session.add(Orders(1000, 2000, "2025-01-01 10:00:00", 202501))
session.add(OrderItems(1000, 3001, 1))
session.add(OrderItems(1000, 3002, 2))


