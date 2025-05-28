from app.db.connection import session
from app.models.models import Customer, Provider, Subscription

def create_customer(name):
    customer = Customer(name=name)
    session.add(customer)
    session.commit()
    return customer

def add_subscription(customer_id, provider_name, price):

    subscription = Subscription(
        customer_id=customer_id,
        provider_name=provider_name,
        price=price
    )
    session.add(subscription)
    session.commit()
    return subscription

def get_all_customers():
    return session.query(Customer).all()

def get_customer_by_id(id):
    return session.query(Customer).filter(Customer.id == id).first()

def get_subscriptions(id):
    return session.query(Subscription).filter(Subscription.customer_id == id).distinct().all()

def get_providers(id):
    return session.query(Provider).join(Subscription).filter(Subscription.customer_id == id).distinct().all()

def update_customer(id, name):
    customer = get_customer_by_id(id)
    if customer:
        customer.name = name
        session.commit()
    return customer

def delete_customer(id):
    customer = get_customer_by_id(id)
    if customer:
        session.delete(customer)
        session.commit()
    return customer


