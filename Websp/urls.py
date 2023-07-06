from django.urls import path
from . import views
urlpatterns=[
    path('' '',views.home,name="home"),
    path('register',views.register,name="register"),
    path('mainpage',views.mainpage,name='mainpage'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('adddash',views.adddash,name='adddash'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('remove_dash/<str:id>', views.remove_dash,name='remove_dash'),
    path('scrape/', views.scrape, name='scrape'),
    path('transform/<str:id>',views.transform,name='transform'),
    path('wish/<str:id>',views.wish,name='wish'),
    path('master/',views.master,name='master'),
    path('stop_scrape/',views.stop_scrape,name='stop_scrape'),
    
]