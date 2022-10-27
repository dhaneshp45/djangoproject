from django.urls import path
from . import views
app_name='app1'
urlpatterns=[
    path('hello/',views.hello,name='hello'),
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('changepass/<int:id>',views.changepass,name='changepass'),
    path('logout/',views.logout,name='logout'),
    path('image/',views.image,name='image'),
]