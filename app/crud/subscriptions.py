from app.db.connection import session
from app.models.models import Provider, Subscription, Customer
from datetime import datetime
from sqlalchemy import func

#Don't add to the CLI just yet
def create_subscription(price, provider_name, customer_id):
    subscription = Subscription(price=price, provider_name=provider_name, customer_id=customer_id)
    session.add(subscription)
    session.commit()
    return subscription

def get_all_subscriptions():
    return session.query(Subscription).all()

def get_subscription_by_id(id):
    return session.query(Subscription).filter(Subscription.id == id).first()

def get_provider(id):
    subscription = get_subscription_by_id(id)
    if subscription:
        return subscription.provider
    return None

def get_customer(id):
    subscription = get_subscription_by_id(id)
    if subscription:
        return subscription.customer
    return None

def update_subscription(id, price, provider_name, customer_id):
    subscription = get_subscription_by_id(id)
    if subscription:
        subscription.price = price
        subscription.provider_name = provider_name
        subscription.customer_id = customer_id
        session.commit()
    return subscription


def renew_subscription(id, price, provider_name, customer_id):
    subscription = get_subscription_by_id(id)
    if subscription:
        new_subscription = create_subscription(
            provider_name=provider_name,
            customer_id=customer_id,
            price=price
        )
        return new_subscription
    return None

def delete_subscription(id):
    subscription = get_subscription_by_id(id)
    if subscription:
        session.delete(subscription)
        session.commit()
    return subscription

