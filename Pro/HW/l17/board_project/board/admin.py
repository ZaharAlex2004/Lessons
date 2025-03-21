from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Ad, Comment, User, Category


class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at', 'is_active', 'category']
    list_filter = ['is_active', 'category']
    search_fields = ['title', 'description']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at', 'ad', 'user']
    list_filter = ['ad', 'user']
    search_fields = ['content']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'phone_number', 'address', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'address')}),
    )


admin.site.register(Ad, AdAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
