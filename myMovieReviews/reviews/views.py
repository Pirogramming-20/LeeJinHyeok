from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.

def reviews_list (request):
    reviews = Review.objects.all() #Post 모델의 DB에 있는 object들을 모두 가져와라.
    context = {
        "reviews": reviews
    }
    return render(request, 'reviews_list.html', context)

def reviews_detail (request, pk):
    review = Review.objects.get(id = pk)
    context = {
        "review": review
    }
    return render (request, 'reviews_detail.html', context)

def reviews_create (request):
    if request.method =="POST" :
        Review.objects.create ( #DB의 Post 폴더에 게시물 하나가 만들어진다.
            title = request.POST["title"],
            year = request.POST["year"],
            director = request.POST["director"],
            genre = request.POST["genre"],
            score = request.POST["score"],
            runtime = request.POST["runtime"],
            actor = request.POST["actor"],
            content = request.POST["content"],
        )
        return redirect("/reviews")
    return render(request, "reviews_create.html")

def reviews_delete (request, pk):
    if request.method == "POST":
        review = Review.objects.get(id = pk)
        review.delete()
    return redirect ("/reviews")

def reviews_update (request, pk):
    review = Review.objects.get(id=pk)
    if request.method=="POST":
        review.title = request.POST["title"]
        review.year = int(request.POST["year"])
        review.content = request.POST["content"]
        review.score = float(request.POST["score"])
        review.runtime = int(request.POST["runtime"])
        review.director = request.POST["director"]
        review.actor = request.POST["actor"]
        review.genre = request.POST["genre"]
        review.save()
        return redirect(f"/reviews/{pk}")
    context = {
        "review": review
    }
    return render(request, "reviews_update.html", context)
    