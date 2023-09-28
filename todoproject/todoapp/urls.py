
from django.urls import path
from  .  import views

urlpatterns = [
    path('',views.add,name='home.html'),
    path('delect/<int:taskid>/',views.delect,name='delect'),
    path('update/<int:id>/',views.update,name='update')

    ]