from django.contrib import admin
from photo.models import Album, Photo

'''
StackedInline : 객체에 연결된 사진 객체들을 세로로 나열하는 방식
TabularInline : '' 가로로 나열하는 방식

'''
class PhotoInline(admin.StackedInline):
    model = Photo
    # admin page에서 추가할때 총 몇개의 데이터를 넣을 건지 알려주는 변수
    extra = 2

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')