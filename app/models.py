import os

from sqlalchemy import (create_engine, Table, Column, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
db_name = os.getenv("POSTGRES_DB", default="db")
db_user = os.getenv("POSTGRES_USER", default="postgres")
db_password = os.getenv("POSTGRES_PASSWORD", default=12345)

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@db/{db_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

user_subscriptions = Table(
    'user_subscriptions',
    Base.metadata,
    Column(
        'user_id',
        ForeignKey('users.id'),
        primary_key=True
    ),
    Column(
        'subscription_id',
        ForeignKey('subscriptions.id'),
        primary_key=True
    ),

)

posts_subscriptions = Table(
    'posts_subscriptions', Base.metadata,
    Column(
        'post_id',
        ForeignKey('posts.id'),
        primary_key=True
    ),
    Column(
        'subscription_id',
        ForeignKey('subscriptions.id'),
        primary_key=True
    ),

)

digests_posts = Table(
    'digests_subscriptions', Base.metadata,
    Column(
        'digest_id',
        ForeignKey('digests.id'),
        primary_key=True
    ),
    Column(
        'post_id',
        ForeignKey("posts.id"),
        primary_key=True
    ),

)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    subscriptions = relationship(
        "Subscription",
        back_populates="users",
        secondary=user_subscriptions
    )


class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True)
    source = Column(String)

    users = relationship(
        "User",
        back_populates="subscriptions",
        secondary=user_subscriptions
    )
    posts = relationship(
        "Post",
        back_populates="subscriptions",
        secondary=posts_subscriptions
    )
    extend_existing = True


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=True)
    subscriptions = relationship(
        "Subscription",
        back_populates="posts",
        secondary=posts_subscriptions
    )
    rating = Column(Integer)
    digests = relationship(
        "Digest",
        back_populates="posts",
        secondary=digests_posts
    )


class Digest(Base):
    __tablename__ = "digests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    posts = relationship(
        "Post",
        back_populates="digests",
        secondary=digests_posts
    )


Base.metadata.create_all(bind=engine)
