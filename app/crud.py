from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from models import SessionLocal
from models import Subscription, User, Digest, Post

db = SessionLocal()


def add_to_database(obj, db: Session):
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def return_digest(
        user_id: int,
        rating: int,
        db: Session
):
    try:
        digest = db.query(Digest).filter(
            Digest.user_id == user_id
        ).first()

        digest_posts = get_posts(user_id, db, rating)

        if digest is None:
            new_digest = Digest(
                user_id=user_id,
                posts=digest_posts
            )
            add_to_database(
                new_digest,
                db=db
            )
        else:
            digest.posts = digest_posts
        return digest
    except IntegrityError as e:
        return {1}


def get_posts(user_id: int, db: Session, rating: int = 0):
    subscriptions = db.query(Subscription).join(
        Subscription.users).filter(User.id == user_id).all()

    subscription_ids = [subscription.id for subscription in subscriptions]

    posts = db.query(Post).order_by(Post.rating.desc()).filter(
        Post.subscriptions.any(Subscription.id.in_(subscription_ids)),
        Post.rating >= rating
    ).all()
    return posts
