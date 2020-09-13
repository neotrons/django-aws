from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AbstractAudit


class Tag(models.Model):
    """
    Stores a single book tags
    """
    id = models.AutoField(_('id'), primary_key=True)
    description = models.CharField(_('description'), max_length=50)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.description


class Author(AbstractAudit):
    """
    Stores a book author record
    """
    id = models.AutoField(_('id'), primary_key=True)
    full_name = models.CharField(_('full name'), max_length=150)
    photo = models.ImageField(_('photo'), upload_to='book/author')

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        return self.full_name


class Category(AbstractAudit):
    """
    Stores a book category record
    """
    id = models.AutoField(_('id'), primary_key=True)
    description = models.CharField(_('description'), max_length=100)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.description


class Book(AbstractAudit):
    """
    Stores a book record, related to :model:`book.Category` and :model:`book.Tag`.
    """
    id = models.AutoField(_('id'), primary_key=True)
    title = models.CharField(_('title'), max_length=150)
    summary = models.TextField(_('summary'), max_length=300)
    cover = models.ImageField(_('cover'), upload_to='book/book')
    file = models.FileField(_('file'), upload_to='book/book')
    pages = models.PositiveSmallIntegerField(_('pages'))
    year = models.PositiveSmallIntegerField(_('year'))
    categories = models.ManyToManyField(
        Category,
        verbose_name=_('categories'),
        related_name='categories',
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_('tags'),
        related_name='tags',
        blank=True
    )

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')

    def __str__(self):
        return self.title
