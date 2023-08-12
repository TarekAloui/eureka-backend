# apps/core/schema.py

import graphene
from graphene_django import DjangoObjectType
from .models import Author, Paper, Tweet


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class PaperType(DjangoObjectType):
    class Meta:
        model = Paper


class TweetType(DjangoObjectType):
    class Meta:
        model = Tweet


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    papers = graphene.List(PaperType)
    tweets = graphene.List(TweetType)

    def resolve_authors(self, info):
        return Author.objects.all()

    def resolve_papers(self, info):
        return Paper.objects.all()

    def resolve_tweets(self, info):
        return Tweet.objects.all()


schema = graphene.Schema(query=Query)
