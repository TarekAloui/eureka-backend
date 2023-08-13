import os
import django
import random
from faker import Faker
from datetime import datetime, timedelta
import sys

# Adding the path of the entire project to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setting up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.main.models import Author, Paper, Tweet

fake = Faker()

# Generating fake authors
def generate_authors(count=10):
    authors = []
    for _ in range(count):
        author = Author(
            name=fake.name(),
            affiliation=fake.company(),
            hIndex=random.randint(0, 100),
            i10Index=random.randint(0, 100),
            citations=random.randint(0, 5000),
            interests=",".join([fake.job() for _ in range(3)]),
            profileUrl=fake.url()
        )
        author.save()
        authors.append(author)
    return authors

# Generating fake tweets
def generate_tweets(count=10):
    tweets = []
    for _ in range(count):
        tweet = Tweet(
            url=fake.url(),
            user_name=fake.user_name(),
            retweets=random.randint(0, 1000),
            likes=random.randint(0, 1000),
            text=fake.sentence(),
            date=fake.date_time_this_year()
        )
        tweet.save()
        tweets.append(tweet)
    return tweets

# Generating fake papers
def generate_papers(authors, tweets, count=10):
    for _ in range(count):
        paper = Paper(
            title=fake.sentence(),
            abstract=fake.paragraph(),
            pub_date=fake.date_time_this_decade(),
            updated_date=fake.date_time_this_year(),
            categories=",".join([fake.word() for _ in range(3)]),
            links=fake.url(),
            comment=fake.sentence(),
            journal_ref="Journal of AI Research",
            trendiness_score=random.random() * 100
        )
        paper.save()
        for author in random.sample(authors, random.randint(1, 5)):
            paper.authors.add(author)
        for tweet in random.sample(tweets, random.randint(1, 5)):
            paper.relatedTweets.add(tweet)

# Main Execution
if __name__ == '__main__':
    authors = generate_authors(10)
    tweets = generate_tweets(10)
    generate_papers(authors, tweets, 50)
