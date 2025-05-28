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

def get_provider_by_name(name):
    return session.query(Provider).filter(Provider.name == name).first()

def get_customers(name):
    return session.query(Customer).join(Subscription).filter(Subscription.provider_name == name).distinct().all()

def active_subscriptions(name):
    return session.query(Subscription).filter(Subscription.provider_name == name, Subscription.exp_date > datetime.now()).distinct().all()

def inactive_subscriptions(name):
    return session.query(Subscription).filter(Subscription.provider_name == name, Subscription.exp_date <= datetime.now()).distinct().all()

def customers_with_inactive_subs(provider_name):
    return session.query(Customer).join(Subscription).filter(
        Subscription.provider_name == provider_name,
        Subscription.exp_date <= datetime.now()
    ).distinct().all()

def customers_with_active_subs(provider_name):
    return session.query(Customer).join(Subscription).filter(
        Subscription.provider_name == provider_name,
        Subscription.exp_date > datetime.now()
    ).distinct().all()

def total_revenue(provider_name):
    total = (
        session.query(func.sum(Subscription.price))
        .filter(
            Subscription.provider_name == provider_name,
            Subscription.exp_date > datetime.now()
        )
        .scalar()
    )
    return total

def update_provider(name, tagline):
    provider = get_provider_by_name(name)
    if provider:
        provider.name = name
        provider.tagline = tagline
        session.commit()
    return provider

def delete_provider(name):
    provider = get_provider_by_name(name)
    if provider:
        session.delete(provider)
        session.commit()
    return provider
