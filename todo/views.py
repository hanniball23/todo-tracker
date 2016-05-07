from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def todo_list(request):
	todos = Post.objects.order_by('deadline')
	return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('todo_list')
	else:
		form = PostForm()
	return render(request, 'todo/todo_edit.html', {'form': form})

def todo_edit(request, pk):
	todo = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=todo)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('todo_list')
	else:
		form = PostForm(instance=todo)
	return render(request, 'todo/todo_edit.html', {'form': form})

def todo_delete(request, pk):
	todo = get_object_or_404(Post, pk=pk)
	Post.objects.get(pk=pk).delete()
	return redirect('todo_list')

def todo_impressum(request):
	return render(request, 'todo/todo_impressum.html', {})