from . import views
from django.urls import path
app_name='movieapp'

urlpatterns = [
    path('',views.fn_Index,name='index'),
    path('movie_detail/<int:movie_id>/',views.fn_Detail, name='movie_detail'),
    path('add/', views.fn_add, name='add'),
    path('update/<int:id>/',views.fn_Update, name='update'),
    path('delete/<int:id>',views.fn_Delete,name='delete')
]