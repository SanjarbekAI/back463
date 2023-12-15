from django.urls import path

from page.views import new_detail_page, home_page_view, add_email

app_name = "page"

urlpatterns = [
    path('news/<int:pk>', new_detail_page, name="news-detail"),
    path('email/', add_email, name="email"),
    path('', home_page_view, name="home"),
]
