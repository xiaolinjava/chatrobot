from django.contrib import admin
from jjechat.books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    search_fields = ('title', )
    #list_filter = ('publication_date', 'title', 'publisher')
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)