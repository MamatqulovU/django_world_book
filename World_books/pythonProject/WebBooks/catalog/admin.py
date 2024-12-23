from django.contrib import admin
from django.templatetags.i18n import language

from .models import Author, Book,  Genre, Language, Status, BookInstance

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)


# administrator klasiga tavsiflar
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# admin klassini unga mos model bilan registratsiya qiling
admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance


# Kitoblar uchun administrator klasslarini registratsiya qilamiz
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]



# Kitob nusxasi uchun administrator klasslarini registratsiya qilamiz
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('book', 'status')
    fieldsets = (
        (None, {
            'fields':('book', 'imprint', 'inv_nom')
        }),
        ('Availability', {
            'fields':('status', 'due_back', 'borrower')
        }),
    )