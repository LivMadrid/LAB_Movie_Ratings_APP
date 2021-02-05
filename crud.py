"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db
import datetime


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie. """

    movie = Movie(title=title,
                 overview=overview,
                 release_date=release_date,
                 poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def create_rating(user, movie, score):
    """Create and return a new rating"""

    rating = Rating(user=user, movie=movie, score=score)

    
    db.session.add(rating)
    db.session.commit()

    return rating

# def test_tables():
#     test_user= create_user('tests@tests.com', 'testings')
#     test_movie = create_movie('title','overview', datetime.datetime.now(), 'path ok')
#     test_rating = create_rating( test_user, test_movie, 5)




if __name__ == '__main__':
    from server import app
    connect_to_db(app)