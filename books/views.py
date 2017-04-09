#Front end of the app/website: What actually gets displayed on the webpage
from django.shortcuts import render
from .models import Book
from django.template import loader
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#A view is a webpage. In order to access it, certain URLs need to be entered
def detail(request, book_id):
    #return HttpResponse("<h2>Details for Book Id:" + str(book_id) + "</h2>")
    try:
        book = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        raise Http404("This book does not exist")
    return render(request, 'books/detail.html', {'book' :book})




def index(request):
    '''
    #this is what the User is going to see
    #connect to the database to get information from it
    all_books = Book.objects.all()
    html = ''
    for each in all_books:
        url = '/books/' + str(each.id) + "/"
        html+='<a href="' + url +'">' + str(each.name) +'</a><br>'
    return HttpResponse(html)
    '''
    all_books = Book.objects.all()
    #template = loader.get_template('books/index.html')
    #Provide context
    context = {
        'all_books': all_books
    }
    #render the template
    #return HttpResponse(template.render(context, request))
    return render(request,'books/index.html', context )

