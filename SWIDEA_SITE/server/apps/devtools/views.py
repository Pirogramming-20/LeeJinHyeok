from django.shortcuts import render, redirect
from .forms import DevToolForm
from .models import DevTool
# Create your views here.
def main(request) :
    devtools = DevTool.objects.all()
    ctx = {
        'devtools': devtools
    }
    return render (request, 'devtools/devtools_list.html', ctx)
    

def create (request):
    if request.method == "GET":
        form = DevToolForm()
        ctx = {
            'form': form,
        }
        return render (request, 'devtools/devtools_create.html' ,ctx)
    form = DevToolForm(request.POST)
    if form.is_valid():
        devtool_instance = form.save()
        devtool_pk = devtool_instance.pk
        return redirect ('devtools:detail',devtool_pk)
    else:
        return redirect ('devtools:main')


def update (request, pk):
    devtool = DevTool.objects.get(id = pk)
    if request.method == "GET":
        form = DevToolForm(instance=devtool)
        ctx = {'form': form, 'pk': pk}
        return render(request, 'devtools/devtools_update.html', ctx)
    form = DevToolForm(request.POST,instance=devtool) 
    if form.is_valid():
        form.save()
    return redirect ('devtools:detail', pk) 

def delete (request, pk):
    if request.method == "POST":
        devtool= DevTool.objects.get(id = pk)
        devtool.delete()
    return redirect ('devtools:main')

def detail (request, pk):
    devtool = DevTool.objects.get(id = pk)
    ideas_devtool = devtool.idea_set.all()
    ctx = {
        "devtool": devtool,
        "ideas_devtool": ideas_devtool,
    }
    return render (request, 'devtools/devtools_detail.html', ctx)
    
