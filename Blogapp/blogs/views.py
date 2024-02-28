from django.shortcuts import render
from categories.models import Category
from .models import Blogs
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def home(request):
    categories = Category.objects.all()
    blogs = Blogs.objects.all().order_by('-created')

    b = blogs

    paginator = Paginator(blogs, 3)
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1

    try:
        blogsPerPage = paginator.page(page)

    except (EmptyPage, InvalidPage):
        blogsPerPage = paginator.page(paginator.num_pages)

    return render(request, 'deshboard/index.html', {
        'categories': categories,
        'blogs':blogsPerPage,
        'paginator':paginator,
        'b':b,
    })

def login(request):
    return render(request, 'authentication/login.html')

def signup(request):
    return render(request, 'authentication/signup.html')

def viewblog(request):
    return render(request, 'deshboard/viewblog.html')