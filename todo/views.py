from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def todo_list(request):
	todos = Post.objects.order_by('deadline')
	return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_new(request):
	form = PostForm()
	return render(request, 'todo/todo_edit.html', {'form': form})


def todo_impressum(request):
	return render(request, 'todo/todo_impressum.html', {})