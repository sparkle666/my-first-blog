from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from .forms import ContactForm, PostForm, Add
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):

	post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'post': post})

def post_details(request, pk):
	
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_details.html', {'post': post})
	# return render(request, 'blog/post_details.html', {'pk': posts['id']})
def myview(request): 
	hello = "Hello there!"
	hi = 'Hi'
	list1 = [1,2,3,4,5,6,7,8]
	return render(request, 'blog/myview.html', {'helloo':hello, 'hi':hi, 'list1': list1})

def hurray(request, number):
	text = '<h1> Your number passed in is %s </h1>' % number
	return HttpResponse(text)

def post_new(request):

	if request.method == 'POST':

		form = PostForm(request.POST)

		if form.is_valid():

			post = form.save(commit='false')
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_details', pk = post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)

	if request.method == 'POST':

		form = PostForm(request.POST, instance=post)

		if form.is_valid():

			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_details', pk = post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def login(request):

	# username = 'not logged in'
	# if request.method == 'POST':
	# 	form1 = ContactForm(request.POST)
	# 	if form1.is_valid():
	# 		username = form1.cleaned_data['username']
	# else:
	form1 = ContactForm()
	return render(request, 'blog/login.html', {'form1': form1})

def add_new(request):
	num_1 = 0
	if request.method == 'POST':
		form_add = Add(request.POST)
		if form_add.is_valid():
			num_1 = form_add.cleaned_data['num1']
	else:
		form_add = Add()
	return render(request, 'blog/add_num.html', {"form_add": form_add, "num_1": num_1})
def latest(request):
	post = Post.objects.all()
	return render(request, 'blog/latest.html', {'post': post})