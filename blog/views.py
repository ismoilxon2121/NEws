from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import custom_login_required
from .models import New,Category
import datetime


@custom_login_required
def home(request):
    category_id=request.GET.get('category_id')

    news = New.objects.all().order_by('-id')

    a_week_ago=datetime.date.today()-datetime.timedelta(days=7)

    categories=Category.objects.all()

    if category_id:
        what_news=news.filter(category_id=category_id).order_by('-id')[:4]

    else:
        what_news=news.order_by('-id')[:4]

    context = {
        'last_new': news.first(),
        "bottom_news": news[1:4],
        'right_news': news[4:9],
        "weekly_top_news":news.filter(created_at__gte=a_week_ago).order_by('-seen_qty')[0:5],
        "categories":categories,
        "what_news": what_news ,
        "Weekly_Top_News" : news[4:9]

    }
    return render(request, 'index.html', context)


@custom_login_required
def category(request):
    return render(request, 'category.html')
















