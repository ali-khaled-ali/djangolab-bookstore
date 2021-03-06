from django.contrib import admin
from .models import Book, Category,Isbn
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("isbn", "content")
    list_filter = ("categories",)
    search_fields = ("owner",)

class BookInline(admin.StackedInline):
    model = Book
    max_num = 3
    extra = 1

class IsbnAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Isbn, IsbnAdmin)