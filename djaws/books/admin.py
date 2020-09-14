from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from core.admin import AuditAdminMixin, ImagePreviewAdminMixin
from .models import Author, Category, Tag, Book


@admin.register(Category)
class CategoryAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('description',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('description',)


@admin.register(Author)
class AuthorAdmin(ImagePreviewAdminMixin, AuditAdminMixin, admin.ModelAdmin):
    list_display = ('full_name',)
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        return self.get_image_preview(field=obj.photo, width='150px')

    photo_preview.short_description = _('image preview')


@admin.register(Book)
class BookAdmin(ImagePreviewAdminMixin, AuditAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'cover_list_display', 'categories_list_display', 'pages', 'year', 'download_file',)
    fields = ('is_active', 'title', 'summary', 'cover', 'cover_preview', 'file', 'categories', 'pages', 'year',
              'tags',)
    readonly_fields = ('cover_preview',)
    filter_horizontal = ('categories', 'tags',)

    def categories_list_display(self, obj):
        categories = obj.categories.values_list('description', flat=True)
        return ', '.join(map(str, categories))

    categories_list_display.short_description = _('categories')

    def cover_preview(self, obj):
        return self.get_image_preview(field=obj.cover)

    cover_preview.short_description = _('image preview')

    def cover_list_display(self, obj):
        return self.get_image_preview(field=obj.cover, width='150px')

    cover_preview.short_description = _('cover')

    def download_file(self, obj):
        if obj.file is None:
            return ''
        return mark_safe(f"<a href='{obj.file.url}' target='_blank'>{_('Download')}</a>")

    download_file.short_description = _('file')
