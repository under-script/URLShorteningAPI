from django.contrib import admin

from api.models import Shorten


# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10

    class Meta:
        abstract = True


class ShortenAdmin(BaseAdmin):
    list_display = [f.name for f in Shorten._meta.fields]
    list_display_links = ('id', 'short_url')


admin.site.register(Shorten, ShortenAdmin)
