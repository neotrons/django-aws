from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class AuditAdminMixin:

    def get_merge_fields(self, origin_fields, fields):
        fields = list(fields)
        for field in origin_fields:
            if field not in fields:
                fields.append(field)
        return fields

    def get_all_fields(self, fields):
        audit_fields = ['is_active', 'creation_date', 'created_by', 'update_date', 'update_by', ]
        return self.get_merge_fields(origin_fields=audit_fields, fields=fields)

    def get_all_readonly_fields(self, fields):
        audit_readonly_fields = ['creation_date', 'created_by', 'update_date', 'update_by', ]
        return self.get_merge_fields(origin_fields=audit_readonly_fields, fields=fields)

    def get_fields(self, request, obj=None):
        fields = super(AuditAdminMixin, self).get_fields(request, obj)
        return self.get_all_fields(fields=fields)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(AuditAdminMixin, self).get_readonly_fields(request, obj=None)
        return self.get_all_readonly_fields(fields=readonly_fields)


class ImagePreviewAdminMixin:

    def get_image_html(self, url, width, height):
        return mark_safe('<img src="{}" width="{}" height="{}">'.format(url, width, height))

    def get_image_preview(self, field, width="200px", height="auto"):
        if field:
            image = self.get_image_html(field.url, width, height)
            return mark_safe('<a href="{}" target="_blank">{}</a>'.format(field.url, image))
        return _('upload an image to show here')
