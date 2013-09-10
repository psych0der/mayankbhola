import models
from django.contrib import admin
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryToPostInline(admin.TabularInline):
    model = models.CategoryToPost
    extra = 1

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class TagToPostInline(admin.TabularInline):
    model = models.TagToPost
    extra = 1

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)
    inlines = [CategoryToPostInline,TagToPostInline]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(models.Image)
admin.site.register(models.Tag,TagAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)