from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    # User 테이블에서 레코드가 삭제되는 경우 그 레코드에 연결된 bookmark 테이블의 레코드도 같이 삭제된다.
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        return self.title
