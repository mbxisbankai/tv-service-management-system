from app.db.connection import session
from app.models.models import Customer, Provider, Subscription
from datetime import datetime, timedelta

def seed():
    # Clear old data if needed (optional)
    session.query(Subscription).delete()
    session.query(Customer).delete()
    session.query(Provider).delete()
    session.commit()

    # Add providers
    p1 = Provider(name="Netflix", tagline="Watch movies and TV shows")
    p2 = Provider(name="Hulu", tagline="Stream your favorite TV")

    session.add_all([p1, p2])
    session.commit()

    # Add customers
    c1 = Customer(name="Alice")
    c2 = Customer(name="Bob")

    session.add_all([c1, c2])
    session.commit()

    # Add subscriptions (use provider_name instead of provider_id)
    sub1 = Subscription(
        price=9.99,
        sub_date=datetime.now(),
        exp_date=datetime.now() + timedelta(days=30),
        provider_name=p1.name,  # changed here
        customer_id=c1.id,
    )
    sub2 = Subscription(
        price=12.99,
        sub_date=datetime.now(),
        exp_date=datetime.now() + timedelta(days=30),
        provider_name=p2.name,  # changed here
        customer_id=c2.id,
    )

    session.add_all([sub1, sub2])
    session.commit()

    print("Seed data added successfully.")

if __name__ == "__main__":
    seed()
