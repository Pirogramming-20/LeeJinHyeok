from django.shortcuts import render, redirect
from .forms import IdeaForm
from .models import Idea
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
# Create your views here.
def main(request) :
    
    sort_option = request.GET.get('sort', 'default')

    if sort_option == 'starred':
        ideas = Idea.objects.order_by('-is_starred', 'title')
    elif sort_option == 'name':
        ideas = Idea.objects.order_by('title')
    elif sort_option == 'registration':
        ideas = Idea.objects.order_by('id')
    elif sort_option == 'latest':
        ideas = Idea.objects.order_by('-id', 'title')
    else:
        # 기본 정렬 옵션
        ideas = Idea.objects.all()
        
    ctx = {
        'ideas': ideas
    }
    return render (request, 'ideas/ideas_list.html', ctx)

def detail (request, pk):
    idea = Idea.objects.get(id = pk)
    ctx = {
        "idea": idea
    }
    return render (request, 'ideas/ideas_detail.html', ctx)


def create (request):
    if request.method == "GET":
        form = IdeaForm()
        ctx = {
            "form": form
        }
        return render (request, 'ideas/ideas_create.html', ctx)
    
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
        idea_instance = form.save()
        idea_pk = idea_instance.pk
        return redirect ('ideas:detail', idea_pk)
    else:
        return redirect ('ideas:main')
    
    
def delete (request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(id = pk)
        idea.delete()
    return redirect ("ideas:main")
    

def update (request, pk):
    idea = Idea.objects.get(id = pk)
    if request.method == "GET":
        form = IdeaForm(instance=idea)
        ctx = {'form': form, 'pk': pk}
        return render(request, 'ideas/ideas_update.html', ctx)
    form = IdeaForm(request.POST, request.FILES, instance=idea) 
    if form.is_valid():
        form.save()
    return redirect ('ideas:detail', pk) 

def toggle_star(request, pk):
    idea = Idea.objects.get(id = pk)
    if idea.is_starred == False:
        idea.is_starred = True
    else:
        idea.is_starred = False
        
    idea.save()
    return redirect ("ideas:main")