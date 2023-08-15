import graphene
from graphene_django import DjangoObjectType
from .models import Author, Paper, Tweet


# Object Types
class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class TweetType(DjangoObjectType):
    class Meta:
        model = Tweet


class PaperType(DjangoObjectType):
    authors = graphene.List(AuthorType)
    relatedTweets = graphene.List(TweetType)
    class Meta:
        model = Paper

    def resolve_authors(self, info):
        return self.authors.all()
    
    def resolve_relatedTweets(self, info):
        return self.relatedTweets.all()


# Queries
class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    papers = graphene.List(PaperType)
    tweets = graphene.List(TweetType)
    paper = graphene.Field(PaperType, id=graphene.UUID(required=True))
    tweet = graphene.Field(TweetType, id=graphene.UUID(required=True))
    author = graphene.Field(AuthorType, id=graphene.UUID(required=True))

    def resolve_authors(self, info):
        return Author.objects.all()

    def resolve_papers(self, info):
        return Paper.objects.all()

    def resolve_tweets(self, info):
        return Tweet.objects.all()
    
    def resolve_paper(self, info, id):
        return Paper.objects.get(pk=id)
    
    def resolve_tweet(self, info, id):
        return Tweet.objects.get(pk=id)
    
    def resolve_author(self, info, id):
        return Author.objects.get(pk=id)


# Author Mutations
class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        affiliation = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, name, affiliation=None):
        author = Author.objects.create(name=name, affiliation=affiliation)
        return CreateAuthor(author=author)


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        affiliation = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, id, name=None, affiliation=None):
        author = Author.objects.get(pk=id)
        if name:
            author.name = name
        if affiliation:
            author.affiliation = affiliation
        author.save()
        return UpdateAuthor(author=author)


class DeleteAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            author = Author.objects.get(pk=id)
            author.delete()
            return DeleteAuthor(success=True)
        except Author.DoesNotExist:
            return DeleteAuthor(success=False)


# Similar mutations for Paper and Tweet can be defined here...

class CreatePaper(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        abstract = graphene.String()
        authors = graphene.List(AuthorType)
        relatedTweets = graphene.List(TweetType)

    paper = graphene.Field(PaperType)

    def mutate(self, info, title, abstract=None, authors=None, relatedTweets=None):
        paper = Paper.objects.create(title=title, abstract=abstract, authors=authors, relatedTweets=relatedTweets)
        return CreatePaper(paper=paper)
    

class UpdatePaper(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        abstract = graphene.String()
        authors = graphene.List(AuthorType)
        relatedTweets = graphene.List(TweetType)

    paper = graphene.Field(PaperType)

    def mutate(self, info, id, title=None, abstract=None, authors=None, relatedTweets=None):
        paper = Paper.objects.get(pk=id)
        if title:
            paper.title = title
        if abstract:
            paper.abstract = abstract
        if authors:
            paper.authors = authors
        if relatedTweets:
            paper.relatedTweets = relatedTweets
        paper.save()
        return UpdatePaper(paper=paper)


class DeletePaper(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            paper = Paper.objects.get(pk=id)
            paper.delete()
            return DeletePaper(success=True)
        except Paper.DoesNotExist:
            return DeletePaper(success=False)


class CreateTweet(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        text = graphene.String(required=True)
        author = graphene.Field(AuthorType)
        relatedPaper = graphene.Field(PaperType)

    tweet = graphene.Field(TweetType)

    def mutate(self, info, id, text, author=None, relatedPaper=None):
        tweet = Tweet.objects.create(id=id, text=text, author=author, relatedPaper=relatedPaper)
        return CreateTweet(tweet=tweet)
    

class UpdateTweet(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        text = graphene.String()
        author = graphene.Field(AuthorType)
        relatedPaper = graphene.Field(PaperType)

    tweet = graphene.Field(TweetType)

    def mutate(self, info, id, text=None, author=None, relatedPaper=None):
        tweet = Tweet.objects.get(pk=id)
        if text:
            tweet.text = text
        if author:
            tweet.author = author
        if relatedPaper:
            tweet.relatedPaper = relatedPaper
        tweet.save()
        return UpdateTweet(tweet=tweet)


class DeleteTweet(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            tweet = Tweet.objects.get(pk=id)
            tweet.delete()
            return DeleteTweet(success=True)
        except Tweet.DoesNotExist:
            return DeleteTweet(success=False)


# Mutation
class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()
    create_paper = CreatePaper.Field()
    update_paper = UpdatePaper.Field()
    delete_paper = DeletePaper.Field()
    create_tweet = CreateTweet.Field()
    update_tweet = UpdateTweet.Field()
    delete_tweet = DeleteTweet.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
