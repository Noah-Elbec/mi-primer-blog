from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')
    return render(request,'blog/post_list.html',{'posteos':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk = pk)
    return render(request,'blog/post_detail.html',{'post': post})