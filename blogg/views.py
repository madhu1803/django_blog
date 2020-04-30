from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreate
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,DeleteView,FormView
from django.views.generic.edit import  CreateView,UpdateView
# read-list view
class Index(ListView):
    model = Post
    template_name = "index.html"


# read-detailed view
class Details(DetailView):
    model = Post
    template_name = "details.html"



# create
class Create(CreateView):
    form_class = PostCreate
    template_name = 'upload_form.html'
    success_url = '/'
#

# update
class Update(UpdateView):
    form_class = PostCreate
    template_name = 'upload_form.html'
    queryset = Post.objects.all()
    success_url = '/'

def update_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect("index")
    book_form = PostCreate(request.POST or None, instance=post_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect("index")
    return render(request, "upload_form.html", {"upload_form": book_form})


# delete
class Delete(DeleteView):
    model = Post
    success_url = "/"
