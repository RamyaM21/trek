from django.contrib import admin
from .models import District, Trek
from .models import Review

admin.site.register(District)
admin.site.register(Trek)
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('trek', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('trek__name', 'user__username', 'comment')