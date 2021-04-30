from django.contrib import admin
from .models import Genre, Movies


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MoviesAdmin(admin.ModelAdmin):
    #fields = ('title', 'genre')
    exclude = ('date_created', )
    list_display = ('id', 'title', 'number_in_stock', 'genre', 'daily_rate', 'release_year')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MoviesAdmin)