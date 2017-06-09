from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
# Create your models here.

class Category(models.Model):
    '''
    django要求模型必须继承自models.Model
    '''
    name = models.CharField(max_length=100)

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

class Tag(models.Model):

    name = models.CharField(max_length=100)

    @python_2_unicode_compatible
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):

    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文
    body = models.TextField()

    # 创建时间
    created_time = models.DateTimeField()

    # 修改时间
    modified_time = models.DateTimeField()

    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)

    # 类别外键
    category = models.ForeignKey(Category)

    # 标签多对多
    tag = models.ManyToManyField(Tag,blank=True)

    # 作者
    author = models.ForeignKey(User)

    @python_2_unicode_compatible
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-created_time']

        

    