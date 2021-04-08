from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import News, Comments


def index(request):
    user = request.user
    news = News.objects.all().order_by("-creation_date")
    context = {"news": news, "user": user}
    return render(request, "index.html", context=context)


def create(request):
    return render(request, "create.html")


def save_created(request):
    if request.user.is_authenticated:
        author = request.user.username
    else:
        author = request.GET["author"]
    News.objects.create(
        author_name=author, title=request.GET["title"], link=request.GET["link"]
    )
    return HttpResponseRedirect("..")


def upvote(request, pk):
    news = News.objects.get(id=pk)
    news.amount_of_upvotes += 1
    if news.amount_of_upvotes > 99:
        news.amount_of_upvotes = 99
    else:
        news.save()
    return HttpResponseRedirect("..")


def all_comments(request, fk):
    comments = Comments.objects.filter(news=fk).order_by("-creation_date")
    news = News.objects.get(id=fk)
    context = {"comments": comments, "news": news}
    return render(request, "all_comments.html", context=context)


def add_comment(request, fk):
    if request.user.is_authenticated:
        text = request.POST.get("comment-text")
        Comments.objects.create(
            news=News.objects.get(id=fk),
            content=text,
            author_name=request.user.username,
        )
    return redirect("index")
