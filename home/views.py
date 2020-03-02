from django.shortcuts import render,redirect
from .models import Post,Category
from django.http import HttpResponse,HttpResponseBadRequest
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def list(request):
    category = Category.objects.all()
    dataset = Post.objects.all()
    content ={
        'Post' : dataset,
        'Category' :category
    }
    return render(request,'home.html',content)

def post_detail(request, id=None):
    if not id:
        return HttpResponseBadRequest()
    instance = Post.objects.get(id=id)
    return render(request,'detail.html',{
        'instance' : instance
    })

def category_detail(request,id=None):
    if not id:
        return HttpResponseBadRequest()
    category=Category.objects.get(id=id)
    post = Post.objects.filter(category=category)
    return render(request,'category_detail.html',{
        'PostByCategoryId' : post
    })

def engine_search(request):
    value = request.GET['search'].strip()  # 'Search' là thuộc tính name trong thẻ input
    posts = Post.objects.filter(content__icontains=value)
    context = {
        'Posts': posts
    }
    return render(request, 'search.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/trangchu')
    else :
        form = UserCreationForm()
    return render(request,'registration/signup.html',{
        'form' : form
    })    

        