from django.urls import path

from . import views

urlpatterns = [
    path('',views.homepage_view,name="home"),
    path('detail/<str:food_id>/',views.food_detail_or_order_view,name='detail'),
    path('search/',views.search_view,name='search'),
    path('category/',views.category_view,name='category'),
    path('categories/',views.all_category_view,name='categories'),
    path('foods/',views.all_foods_view,name='foods')
]