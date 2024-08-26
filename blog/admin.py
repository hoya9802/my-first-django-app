from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from blog.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # TaggableManger class는 직접 등록할 수 없기 때문에, 별로로 정의해서 등록
    list_display = ('id', 'title', 'modify_dt', 'tag_list')     # 추후 Post 객체를 보여줄때 지정한 컬럼을 화면에 출력 지정
    list_filter = ('modify_dt',)                    # admin page에서 filter sidebar를 생성
    search_fields = ('title', 'content')            # admin page에서 검색박스를 표시하고, 입력된 단어를 title과 content에서 검색
    prepopulated_fields = {'slug': ('title',)}      # admin page에서 title를 입력하면 자동으로 slug가 생성됨

    # 해당 메서드는 django-taggit documentation을 참조!
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related('tags')
    
    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    