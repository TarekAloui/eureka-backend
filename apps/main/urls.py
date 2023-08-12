from django.contrib import admin
from django.urls import path
from .views import (
    list_papers,
    paper_detail,
    create_paper,
    update_paper,
    delete_paper,
    list_authors,
    author_detail,
    create_author,
    update_author,
    delete_author,
    list_tweets,
    tweet_detail,
    create_tweet,
    update_tweet,
    delete_tweet,
)

# add all views inside views/__init__.py
urlpatterns = [
    path("list_papers", list_papers, name="list_papers"),
    path("paper_detail/<int:paper_id>", paper_detail, name="paper_detail"),
    path("create_paper", create_paper, name="create_paper"),
    path("update_paper/<int:paper_id>", update_paper, name="update_paper"),
    path("delete_paper/<int:paper_id>", delete_paper, name="delete_paper"),
    path("list_authors", list_authors, name="list_authors"),
    path("author_detail/<int:author_id>", author_detail, name="author_detail"),
    path("create_author", create_author, name="create_author"),
    path("update_author/<int:author_id>", update_author, name="update_author"),
    path("delete_author/<int:author_id>", delete_author, name="delete_author"),
    path("list_tweets", list_tweets, name="list_tweets"),
    path("tweet_detail/<int:tweet_id>", tweet_detail, name="tweet_detail"),
    path("create_tweet", create_tweet, name="create_tweet"),
    path("update_tweet/<int:tweet_id>", update_tweet, name="update_tweet"),
    path("delete_tweet/<int:tweet_id>", delete_tweet, name="delete_tweet"),
]
