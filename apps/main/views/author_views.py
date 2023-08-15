from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Author


def list_authors(request):
    authors = Author.objects.all()
    data = [
        {
            "name": author.name,
            "affiliation": author.affiliation,
            # ... add other fields as needed
        }
        for author in authors
    ]
    return JsonResponse(data, safe=False)


def author_detail(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
        data = {
            "name": author.name,
            "affiliation": author.affiliation,
            # ... add other fields as needed
        }
        return JsonResponse(data)
    except Author.DoesNotExist:
        raise Http404("Author not found")


@csrf_exempt
def create_author(request):
    if request.method == "POST":
        data = json.loads(request.body)
        author = Author.objects.create(
            name=data["name"],
            affiliation=data["affiliation"],
            # ... handle other fields
        )
        return JsonResponse({"id": author.id, "name": author.name})
    else:
        return HttpResponse(status=405)  # Method not allowed


@csrf_exempt
def update_author(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        raise Http404("Author not found")

    if request.method == "PUT":
        data = json.loads(request.body)
        author.name = data["name"]
        author.affiliation = data["affiliation"]
        # ... handle other fields
        author.save()
        return JsonResponse({"id": author.id, "name": author.name})
    else:
        return HttpResponse(status=405)  # Method not allowed


@csrf_exempt
def delete_author(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        raise Http404("Author not found")

    if request.method == "DELETE":
        author.delete()
        return HttpResponse(status=204)  # No content
    else:
        return HttpResponse(status=405)  # Method not allowed
