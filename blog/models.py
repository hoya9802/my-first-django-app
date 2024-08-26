from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')

    # auto_now_add는 객체가 생성되면 자동으로 시각을 저장
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)

    # auto_now는 객체가 데이터베이스에 저장될 때의 시각을 자동으로 저장. 즉, 객체가 변경될때 저장
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='OWNER')

    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'post'
        # admin page에서 보여주는 복수형 글자
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # 해당 메서드가 실행되면 url 패턴 이름을 기반으로 url를 동적으로 생성합니다.
        return reverse('blog:post_detail', args=(self.slug,))
    
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)