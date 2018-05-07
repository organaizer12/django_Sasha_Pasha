from django.urls import path, include
from . import views
from django.contrib.auth import logout
urlpatterns = [
	path('', views.index, name = 'index'),
#    path('time/', views.time, name = 'time'),
#    path('time/plus/<int:offset>/', views.dtime, name = 'dtime'),
    path('news/', views.news, name = 'news'),
    path('accounts/', include('django.contrib.auth.urls')),
]