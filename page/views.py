from django.shortcuts import render, redirect
from django.http import HttpResponse
from page.models import NewsModel, PopularTourModel, DestinationModel, EmailModel


def home_page_view(request):
    news = NewsModel.objects.all().order_by('-created_at')[:3]
    tours = PopularTourModel.objects.all()[:3]
    top_des = DestinationModel.objects.all()[:2]
    bottom_des = DestinationModel.objects.all()[:3]
    context = {
        "news_list": news,
        "tours": tours,
        "top": top_des,
        "bottom": bottom_des,
    }
    return render(request, 'index.html', context)


def new_detail_page(request, pk):
    try:
        news = NewsModel.objects.get(id=pk)
        if news:
            context = {
                "news": news
            }
            return render(request, 'news_item.html', context)
        else:
            return render(request, '404.html')
    except:
        return render(request, '404.html')


def add_email(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user_email = EmailModel.objects.filter(email=email).first()
        if user_email:
            return redirect('page:home')
        new_email = EmailModel.objects.create(
            email=email
        )
        new_email.save()
        return redirect('page:home')
