from django.contrib import admin
from .models import Book, Category,Isbn
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("isbn", "content")
    list_filter = ("categories",)
    search_fields = ("owner",)

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Isbn)