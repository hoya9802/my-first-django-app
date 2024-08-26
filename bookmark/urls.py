from django.urls import path
from bookmark.views import BookmarkDV, BookmarkLV, BookmarkCreateView, BookmarkChangeLV, BookmarkUpdateView, BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    # app_urlconf에서는 다른 app들과의 중복을 피하기 위해 템플릿에에서 호출할때
    # app_name:namespace 형식을 사용하여 지정해줘야 합니다.
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('change/', BookmarkChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', BookmarkUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name='delete'),
]