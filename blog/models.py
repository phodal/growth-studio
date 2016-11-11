from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django_markdown.models import MarkdownField


class Blog(models.Model):
    class Meta:
        verbose_name = _('博客')
        verbose_name_plural = _('博客')

    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User)
    slug = models.SlugField(max_length=100, unique=True)
    content = MarkdownField(default='SOME STRING')
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_blog_post', None, {'slug': slugify(self.slug)}
