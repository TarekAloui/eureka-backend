from django.http import HttpResponse, Http404, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from .models import researchPaper
from .form import researchPaperForm

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'pages/home.html', context = {}, status=200)

def paper_detail_view(request, paper_id, *args, **kwargs):
    data = {
        'id': paper_id
    }
    status = 200 
    try: 
        paper = researchPaper.objects.get(id=paper_id)
        data['title'] = paper.title
        data['author'] = paper.author
        data['description'] = paper.description
    except: 
        data['message'] = 'Not found!'
        status = 400 
    #    raise Http404
    return JsonResponse(data, status=status)
    #return HttpResponse(f"Title:{paper.title} Author: {paper.author} Description: {paper.description}")

def paper_create_view(request:HttpRequest, *args, **kwargs):
    form = researchPaperForm(request.POST or None)
    next_url = request.POST.get('next') or None 
    if form.is_valid():
        obj = form.save(commit=False)
        obj = form.save()
        if next_url != None:
            return redirect(next_url)
        form = researchPaperForm()

    return render(request, 'components/forms.html', context={'form':form})

def list_papers(request, *args, **kwargs):
    plist = researchPaper.objects.all()
    papers = [{'id':x.id, 'title':x.title, 'author':x.author, 'description':x.description} for x in plist]
    data = {
        "response": papers
    }
    return JsonResponse(data)





