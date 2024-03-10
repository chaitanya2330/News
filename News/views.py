from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    news = NewsDetailModel.objects.all()
    latest_news = NewsDetailModel.objects.filter(status='Latest')[:2]
    latest_news_reverseorder = NewsDetailModel.objects.filter(status='Latest')[2:4]
    popular_news = NewsDetailModel.objects.filter(status='Popular')[:3]
    carsonal_filter = NewsDetailModel.objects.all()[:3]
    carsonal_filter_box = NewsDetailModel.objects.all()[3:7]
    flicker_photo = NewsDetailModel.objects.all()[:6]
    context = {
        'news': news,
        'related': latest_news,
        'popular_news': popular_news,
        'reverse_latest': latest_news_reverseorder,
        'carsonal_filter': carsonal_filter,
        'carsonal_filter_box': carsonal_filter_box,
        'breaking_news': news,
        'flicker_photo': flicker_photo,
    }
    return render(request, 'News/home.html', context)