from models import SessionLocal
from models import User, Subscription, Post

db = SessionLocal()


def add_to_database(obj):
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


user_1 = add_to_database(User(name="den"))
user_2 = add_to_database(User(name="julia"))
user_3 = add_to_database(User(name="petr"))
user_4 = add_to_database(User(name="kiril"))
subscription_1 = add_to_database(
    Subscription(
        users=[user_1],
        source="Forex News"
    )
)
subscription_2 = add_to_database(
    Subscription(
        users=[user_1],
        source="Waterfalls"
    )
)

post_1 = add_to_database(
    Post(
        content="USD now lower than EUR",
        subscriptions=[subscription_1],
        rating=7
    )
)
post_2 = add_to_database(
    Post(
        content="Waterfall in Alanya",
        subscriptions=[subscription_2],
        rating=5
    )
)
post_3 = add_to_database(
    Post(
        content="Turkey give 100000 USD for rebuilding Waterfalls",
        subscriptions=[subscription_1, subscription_2],
        rating=2
    )
)
post_4 = add_to_database(
    Post(
        content="Bitcoin now lose",
        subscriptions=[subscription_1],
        rating=10
    )
)
post_5 = add_to_database(
    Post(
        content="WOW",
        subscriptions=[subscription_1],
        rating=8
    )
)
