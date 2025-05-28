from app.db.connection import session
from app.models.models import Provider, Subscription, Customer
from datetime import datetime
from sqlalchemy import func

def create_provider(name, tagline):
    provider = Provider(name=name, tagline=tagline)
    session.add(provider)
    session.commit()
    return provider

def get_all_providers():
    return session.query(Provider).all()

def get_provider_by_id(id):
    return session.query(Provider).filter(Provider.id == id).first()

def get_customers(id):
    return session.query(Customer).join(Subscription).filter(Subscription.provider_id == id).distinct().all()

def active_subscriptions(id):
    return session.query(Subscription).filter(Subscription.provider_id == id, Subscription.exp_date > datetime.now()).distinct().all()

def inactive_subscriptions(id):
    return session.query(Subscription).filter(Subscription.provider_id == id, Subscription.exp_date <= datetime.now()).distinct().all()

def customers_with_inactive_subs(provider_id):
    return session.query(Customer).join(Subscription).filter(
        Subscription.provider_id == provider_id,
        Subscription.exp_date <= datetime.now()
    ).distinct().all()

def total_revenue(provider_id):
    total = (
        session.query(func.sum(Subscription.price))
        .filter(
            Subscription.provider_id == provider_id,
            Subscription.exp_date > datetime.now()
        )
        .scalar()
    )
    return total

def update_provider(id, name, tagline):
    provider = get_provider_by_id(id)
    if provider:
        provider.name = name
        provider.tagline = tagline
        session.commit()
    return provider

def delete_provider(id):
    provider = get_provider_by_id(id)
    if provider:
        session.delete(provider)
        session.commit()
    return provider
