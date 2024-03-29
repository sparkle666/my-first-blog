from django.urls import path
from . import views
from blog.views import MyView, MyTemp
from . import forms
urlpatterns = [
		path('', views.post_list, name='post_list'),
		path('posts/<int:pk>/', views.post_details, name='post_details'),
		path('myview/', views.myview, name='myview'),
		path('hurray/<str:number>/', views.hurray, name='hurray'),
		path('post/new/', views.post_new, name='post_new'),
		path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
		# path('login/', views.login, name='login'),
		path('add/new/', views.add_new, name='add_new'),
		path('latest/', views.latest, name='latest'),
		path('view/', MyView.as_view(), name='my-view'),
		path('test/', MyTemp.as_view(), name = 'test'),
		# path('logout', views.logout_now, name = 'logout_now'),
		
]