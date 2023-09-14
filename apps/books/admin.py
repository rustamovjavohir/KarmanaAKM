from django.contrib import admin
from apps.books.models import Book, Author, Category, Image
from config import settings


# Register your models here.


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ('name', 'image', 'image_full_path', 'is_main')
    search_fields = ('name', 'is_main')
    list_filter = ('name', 'is_main')

    def get_book(self, obj):
        return obj.book.name

    get_book.short_description = 'Книга'

    def get_author(self, obj):
        return obj.author.name

    get_author.short_description = 'Автор'

    def image_full_path(self, obj):
        return f"{settings.HOST}{obj.image.url}"

    image_full_path.short_description = 'rasm manzili (url)'


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    fields = ('name', 'slug', 'image')
    readonly_fields = ('slug',)

    def get_image(self, obj):
        return obj.image.image.url

    get_image.short_description = 'Изображение url'


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    readonly_fields = ('slug',)

    def get_image(self, obj):
        return obj.image.image.url

    get_image.short_description = 'Изображение url'


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name', 'author', 'category')
    fields = ('name', 'slug', 'image', 'author', 'category', 'description')
    readonly_fields = ('slug',)

# test branch
