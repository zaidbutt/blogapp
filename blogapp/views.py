from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

def post_list(request):
	posts = Post.published.all()
	return render(request, 'blogapp/post/list.html',
				{'posts': posts })


def post_detail(request, id):
	# try:
	# 	post = Post.published.get(id=id)
	# except Post.DoesNotExist:
	# 	raise Http404("No Post Found")
	
	post = get_object_or_404(Post,id=id)

	return render(request, 'blogapp/post/detail.html', 
						 {'post': post})

