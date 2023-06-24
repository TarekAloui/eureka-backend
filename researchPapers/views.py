from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render
from .models import researchPaper
from .form import researchPaperForm

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'pages/home.html', context = {}, status=200)

def paper_detail_view(request, paper_id, *args, **kwargs):
    try: 
        paper = researchPaper.objects.get(id=paper_id)
    except: 
        raise Http404
    return HttpResponse(f"<h1>Title:{paper.title} Author: {paper.author} Description: {paper.description}</h1>")

def paper_create_view(request:HttpRequest, *args, **kwargs):
    form = researchPaperForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj = form.save()
        form = researchPaperForm()
    return render(request, 'components/forms.html', context={'form':form})





