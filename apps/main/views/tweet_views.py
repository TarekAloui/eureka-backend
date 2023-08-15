from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Tweet


def list_tweets(request):
    tweets = Tweet.objects.all()
    data = [
        {
            "url": tweet.url,
            "user_name": tweet.user_name,
            # ... add other fields as needed
        }
        for tweet in tweets
    ]
    return JsonResponse(data, safe=False)


def tweet_detail(request, tweet_id):
    try:
        tweet = Tweet.objects.get(pk=tweet_id)
        data = {
            "url": tweet.url,
            "user_name": tweet.user_name,
            # ... add other fields as needed
        }
        return JsonResponse(data)
    except Tweet.DoesNotExist:
        raise Http404("Tweet not found")


@csrf_exempt
def create_tweet(request):
    if request.method == "POST":
        data = json.loads(request.body)
        tweet = Tweet.objects.create(
            url=data["url"],
            user_name=data["user_name"],
            # ... handle other fields
        )
        return JsonResponse({"id": tweet.id, "url": tweet.url})
    else:
        return HttpResponse(status=405)


@csrf_exempt
def update_tweet(request, tweet_id):
    try:
        tweet = Tweet.objects.get(pk=tweet_id)
    except Tweet.DoesNotExist:
        raise Http404("Tweet not found")

    if request.method == "PUT":
        data = json.loads(request.body)
        tweet.url = data["url"]
        tweet.user_name = data["user_name"]
        # ... handle other fields
        tweet.save()
        return JsonResponse({"id": tweet.id, "url": tweet.url})
    else:
        return HttpResponse(status=405)


@csrf_exempt
def delete_tweet(request, tweet_id):
    try:
        tweet = Tweet.objects.get(pk=tweet_id)
    except Tweet.DoesNotExist:
        raise Http404("Tweet not found")

    if request.method == "DELETE":
        tweet.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)
