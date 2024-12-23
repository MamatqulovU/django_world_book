from django.http import *
from django.shortcuts import render
from .forms import AuthorsForm
from .models import Book, Author, BookInstance, Genre
from django.views.generic import ListView
from django.views import generic
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from .models import Book

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')

# mualliflar haqidagi mal`umotlarning MBda saqlanishi
def create(request):
    if request.method == "POST":
        author = Author()
        author.first_name = request.POST.get("first_name")
        author.last_name = request.POST.get("last_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/authors_add")

# mualliflarni MBdan o`chirish
def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/authors_add/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Muallif topilmadi</h2>")

# MBdagi mal`umotlarni o`zgartirish
def edit1(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author.first_name =  request.POST.get("first_name")
        author.last_name =  request.POST.get("last_name")
        author.date_of_birth =  request.POST.get("date_of_birth")
        author.date_of_death =  request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/authors_add/")
    else:
        return render(request, "edit1.html", {"author":author})

# ma`lumotlarni MBdan olish va authors_add.html shablonini yuklash
def authors_add(request):
    author = Author.objects.all()
    authorsform = AuthorsForm()
    return render(request, "catalog/authors_add.html",
                  {"form":authorsform, "author":author})

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    '''
    Joriy foydalanuvchining qo`lida bo`lgan kitoblar
    ko`rinishining universal klassi
    '''
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrower_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(
                borrower=self.request.user,
                status__exact='2').order_by('due_back')




class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'

def index(request):
    # Ba`zi asosiy ob`yektlar "miqdori" generatsiyasi
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Mavjud kitoblar (status = "omborda")
    num_instances_available = (
        BookInstance.objects.filter(status__exact=2).count())
    num_authors = Author.objects.count() # 'all()' metodi sukut bo`yicha qo`llanilgan

    # session o`zgaruvchisida sanalgan, bu viewga kirishlar soni
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # index.html HTML-shablonining context o`zgaruvchisi tarkibidagi
    # ma`lumotlar bilan tayyorlanishi
    return render(request, 'index.html',
                  context={'num_books':num_books,
                           'num_instances':num_instances,
                           'num_instances_available':num_instances_available,
                           'num_authors':num_authors,
                           'num_visits':num_visits}
                  )

class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    ordering = ['title']

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4