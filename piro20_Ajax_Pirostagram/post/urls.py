from django.urls import path
from .views import *
app_name = 'post'
urlpatterns = [
    path ('', main, name='main'),
    path ('create/', create, name='create'),
    path ('detail/<int:pk>', detail, name = 'detail'),
    path ('update/<int:pk>', update, name = 'update'),
    path ('delete/<int:pk>', delete, name = 'delete'),
    path ('like/', like, name="like"),
    path ('comment/', comment, name="comment"),
    path ('get_comments/<int:pk>/', get_comments, name="get_comments"),
    path ('delete_comment/<int:postId>/<int:commentId>/', delete_comment, name = "delete_comment")
]