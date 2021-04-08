from celery import app

from .models import News


@app.task(name="reset_upvotes")
def reset_upvotes():
    all_news = News.objects.all()

    for article in all_news:
        article.amount_of_upvotes = 0
