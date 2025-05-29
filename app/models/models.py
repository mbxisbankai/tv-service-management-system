from sqlalchemy import Column, Integer, Text, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.connection import Base
from datetime import datetime, timedelta

def expiry_date(context):
    sub_date = context.get_current_parameters().get('sub_date') or datetime.now()
    return sub_date + timedelta(days=31)

class Provider( Base ):
    __tablename__ = "providers"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False, unique=True)
    tagline = Column(Text())

    subscriptions = relationship("Subscription", back_populates="provider")

    def __repr__(self):
        return f"[Provider #{self.id}] {self.name} — \"{self.tagline}\""

    
class Subscription( Base ):
    __tablename__ = "subscriptions"
    
    id = Column(Integer(), primary_key=True)
    price = Column(Float(), nullable=False)
    sub_date = Column(DateTime(), default=datetime.now)
    exp_date = Column(DateTime(), default=expiry_date)

    provider_name = Column(String(), ForeignKey('providers.name'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    provider = relationship("Provider", back_populates="subscriptions")
    customer = relationship("Customer", back_populates="subscriptions")

    def __repr__(self):
        return (
        f"[Subscription #{self.id}] "
        f"Provider: {self.provider_name} | "
        f"Customer ID: {self.customer_id} | "
        f"Price: {self.price} | "
        f"Start: {self.sub_date} → Expiry: {self.exp_date}"
    )

class Customer( Base ):
    __tablename__ = "customers"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)

    subscriptions = relationship("Subscription", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"[Customer #{self.id}] {self.name}"


    


  
