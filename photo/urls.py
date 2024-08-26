from django.urls import path
from photo import views
from photo.views import AlbumLV, AlbumDV, PhotoDV, AlbumPhotoCV, AlbumChangeLV, AlbumPhotoUV, AlbumDelV, PhotoCV, PhotoChangeLV, PhotoUV, PhotoDelV

app_name = 'photo'

urlpatterns = [
    path('', AlbumLV.as_view(), name='album_list'),
    path('album/<int:pk>/', AlbumDV.as_view(), name='album_detail'),
    path('photo/<int:pk>/', PhotoDV.as_view(), name='photo_detail'),
    path('album/add/', AlbumPhotoCV.as_view(), name='album_add'),
    path('album/change/', AlbumChangeLV.as_view(), name='album_change'),
    path('album/<int:pk>/update/', AlbumPhotoUV.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', AlbumDelV.as_view(), name='album_delete'),
    path('photo/add/', PhotoCV.as_view(), name='photo_add'),
    path('photo/change/', PhotoChangeLV.as_view(), name='photo_change'),
    path('photo/<int:pk>/update/', PhotoUV.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDelV.as_view(), name='photo_delete')
]