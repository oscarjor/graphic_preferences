from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import Selection
import flickrapi
import random

api_key = "628f929193af464fca54cb728e9b7f0f"
secret = "4fccfbe6edbc67e9"
url_template = 'http://farm%(farm_id)s.staticflickr.com/%(server_id)s/%(photo_id)s_%(secret)s.jpg'
tags = ["sports","cats","dogs","love","games"]

def url_for_photo(p):
	return url_template % {
		'server_id': p.get('server'),
		'farm_id': p.get('farm'),
		'photo_id': p.get('id'),
		'secret': p.get('secret'),
	}

def login_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			context = {'message':'Please check your user and password!'}
			return render(request, 'quiz/login.html', context)
	else:
		context = {'message':''}
		return render(request, 'quiz/login.html', context)

def logout_view(request):
	logout(request)
	return redirect('/login/')

def index(request):
	if not request.user.is_authenticated:
		return redirect('/login/')
	else:

		flickr = flickrapi.FlickrAPI(api_key, secret)
		category1 = random.choice(tags)
		photos = flickr.photos_search(tags=category1, per_page=1000)
		url1 = url_for_photo(random.choice(photos[0]))
		category2 = random.choice(tags)
		photos2 = flickr.photos_search(tags=category2, per_page=1000)
		url2 = url_for_photo(random.choice(photos2[0]))

		if request.method == "POST":
			image_url = request.POST['image_url']            
			category = request.POST['category']
			selection = Selection()
			selection.user = request.user
			selection.image_url = image_url
			selection.category = category
			selection.save()
			context = {'message': 'Your selection has been saved.', 'url1': url1, 'url2': url2, 'category1': category1, 'category2': category2}
		else:
			
			context = {'message': '', 'url1': url1, 'url2': url2, 'category1': category1, 'category2': category2}
		return render(request, 'quiz/index.html', context)
