from django.urls import path

from . import views

urlpatterns = [
    path('',views.homepage_view,name="home"),
    path('detail/<str:food_id>/',views.food_detail_or_order_view,name='detail'),
    path('ordering/<str:food_id>/',views.ordering_view,name='ordering'),
    path('search/',views.search_view,name='search'),
    path('category/',views.category_view,name='category'),
    path('categories/',views.all_category_view,name='categories'),
    path('foods/',views.all_foods_view,name='foods'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
]