import math

from django.shortcuts import render, HttpResponse
from home.models import Blog, Contact, Review


# Create your views here.
def home(request):
    reviews = Review.objects.all()
    print(reviews)
    context={'reviews':reviews}
    return render(request, 'index.html', context)
def blog(request):
    no_of_posts=3
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page=int(page)

    blogs = Blog.objects.all()
    length=len(blogs)
    no_of_pages= math.ceil(length/no_of_posts)
    print(no_of_pages)
    blogs=blogs[(page-1)*no_of_posts:page*no_of_posts]

    if page>1:
        prev=page-1
    else:
        prev=None

    if page<math.ceil(length/no_of_posts):
        nxt=page+1
    else:
        nxt=None
    context = {'blogs': blogs, 'prev':prev, 'nxt':nxt, 'no_of_pages':no_of_pages, }
    return render(request, 'blog.html', context)
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')

        instance=Contact(name=name,phone=phone,email=email,desc=desc)
        instance.save()
    return render(request, 'contact.html')
def blogpost(request,slug):
    blog= Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    return render(request, 'blogpost.html',context)
def search(request):
    return render(request, 'search.html')

def review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('review')
        image = request.FILES['image']
        print(image.name,image.size)
        instance = Review(name=name,email=email,review=text, image=image)
        instance.save()

    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'index.html', context)