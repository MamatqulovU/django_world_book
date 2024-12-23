from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text=" Kitob janrini kiriting", verbose_name="Kitob janri")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Kitob tilini kiriting", verbose_name="Kitob tili")

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Muallif ismini kiriting",
                                  verbose_name="Muallif ismi")
    last_name = models.CharField(max_length=200,
                                 help_text="Muallif familiyasini kiriting",
                                 verbose_name="Muallif familiyasi",
                                 default="Unknown")
    date_of_birth = models.DateField(help_text="Tug`ilish sanasini kiriting", verbose_name="Tug`ilgan sana",
                                     null=True, blank=True)
    date_of_death = models.DateField(help_text="O`lim sanasini kiriting", verbose_name="O`lim sanasi",
                                     null=True, blank=True)

    def __str__(self):
        return self.last_name

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Kitob nomini kiriting", verbose_name="Kitob nomi")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text="Kitob uchun janrni tanlang",
                              verbose_name="Kitob janri", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text='Kitob uchun tilni tanlang',
                                 verbose_name="Kitob tili", null=True)
    author = models.ManyToManyField('Author',
                                    help_text='Kitob muallifini tanlang',
                                    verbose_name='Kitob muallifi')
    summary = models.TextField(max_length=1000, help_text='Kitobning qisqacha tavsifini kiriting',
                               verbose_name='Kitob annotatsiyasi')
    isbn = models.CharField(max_length=13,
                            help_text='13 ta belgidan iborat bo`lishi kerak',
                            verbose_name='kitob ISBNi')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Kitobning muayyan nusxasiga o`tish uchun URL-manzilni qaytaradi.
        return reverse('catalog:book-detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])
    display_author.short_description = 'Mualliflar'

class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Kitob nusxasining statusini kiriting",
                            verbose_name="Kitob nusxasi statusi")

    def __str__(self):
        return self.name

class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE,
                             null=True,
                             verbose_name="Kitob nomi")
    inv_nom = models.CharField(max_length=20, null=True,
                               help_text='Nusxaning inventar raqamini kiriting',
                               verbose_name='Inventar raqami')
    imprint = models.CharField(max_length=200,
                               help_text="Nashriyot va nashr yilini kiriting",
                               verbose_name='Nashriyot')
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True,
                               help_text='Nusxa holatini o`zgartirish',
                               verbose_name='Kitob nusxasi statusi')
    due_back = models.DateField(null=True, blank=True,
                                help_text='Status muddati yakunini kiriting',
                                verbose_name='Status yakuni sanasi')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name="Buyurtmachi",
                                 help_text="Kitob buyurtmachisini tanlang")

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False























