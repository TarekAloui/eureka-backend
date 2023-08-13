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

# Mutation
class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()
    # Add fields for Paper and Tweet mutations here...


schema = graphene.Schema(query=Query, mutation=Mutation)
