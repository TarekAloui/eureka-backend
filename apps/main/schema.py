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
class CreateAuthorInput(graphene.InputObjectType):
    name = graphene.String()
    affiliation = graphene.String()
    hIndex = graphene.Int()
    i10Index = graphene.Int()
    citations = graphene.Int()
    interests = graphene.String()
    profileUrl = graphene.String()

class CreateAuthor(graphene.Mutation):
    class Arguments:
        authorInput = CreateAuthorInput(required=True)

    author = graphene.Field(AuthorType)

    def mutate(self, info, authorInput):
        author = Author.objects.create(name=authorInput.name, affiliation=authorInput.affiliation, hIndex=authorInput.hIndex, i10Index=authorInput.i10Index, citations=authorInput.citations, interests=authorInput.interests, profileUrl=authorInput.profileUrl)
        return CreateAuthor(author=author)

class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        authorInput = CreateAuthorInput(required=True)

    author = graphene.Field(AuthorType)

    def mutate(self, info, id, authorInput):
        author = Author.objects.get(pk=id)
        name, affiliation, hIndex, i10Index, citations, interests, profileUrl = authorInput.name, authorInput.affiliation, authorInput.hIndex, authorInput.i10Index, authorInput.citations, authorInput.interests, authorInput.profileUrl
        if name:
            author.name = name
        if affiliation:
            author.affiliation = affiliation
        if hIndex:
            author.hIndex = hIndex
        if i10Index:
            author.i10Index = i10Index
        if citations:
            author.citations = citations
        if interests:
            author.interests = interests
        if profileUrl:
            author.profileUrl = profileUrl
        
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


# Paper Mutations

# TODO

# Tweet Mutations
# TODO


# Mutation
class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
