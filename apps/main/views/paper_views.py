from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Paper


def list_papers(request):
    papers = Paper.objects.all()
    data = [
        {
            "id": str(paper.id),
            "title": paper.title,
            # ... add other fields as needed
        }
        for paper in papers
    ]
    return JsonResponse(
        data, safe=False
    )  # `safe=False` is required because we're sending back a list


def paper_detail(request, paper_id):
    try:
        paper = Paper.objects.get(pk=paper_id)
        data = {
            "id": str(paper.id),
            "title": paper.title,
            "abstract": paper.abstract,
            # ... add other fields as needed
        }
        return JsonResponse(data)
    except Paper.DoesNotExist:
        raise Http404("Paper not found")


@csrf_exempt  # This is to exempt the view from CSRF checks. In production, you'd want to handle CSRF.
def create_paper(request):
    if request.method == "POST":
        data = json.loads(request.body)
        paper = Paper.objects.create(
            title=data["title"],
            # ... handle other fields
        )
        return JsonResponse({"id": str(paper.id), "title": paper.title})
    else:
        return HttpResponse(status=405)  # Method not allowed


@csrf_exempt
def update_paper(request, paper_id):
    try:
        paper = Paper.objects.get(pk=paper_id)
    except Paper.DoesNotExist:
        raise Http404("Paper not found")

    if request.method == "PUT":
        data = json.loads(request.body)
        paper.title = data["title"]
        # ... handle other fields
        paper.save()
        return JsonResponse({"id": str(paper.id), "title": paper.title})
    else:
        return HttpResponse(status=405)  # Method not allowed


@csrf_exempt
def delete_paper(request, paper_id):
    try:
        paper = Paper.objects.get(pk=paper_id)
    except Paper.DoesNotExist:
        raise Http404("Paper not found")

    if request.method == "DELETE":
        paper.delete()
        return HttpResponse(status=204)  # No content
    else:
        return HttpResponse(status=405)  # Method not allowed
