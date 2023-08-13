from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

app_name = 'news'

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('update/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDelete.as_view(), name='post_delete')
]
