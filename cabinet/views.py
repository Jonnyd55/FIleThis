from django.views.generic import TemplateView, ListView
from models import File
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.conf import settings
from filethis.enrichment import enrich
from forms import *
import datetime


class IndexView(TemplateView):
	template_name = 'index.html'

class UserView(TemplateView):
	template_name = 'user.html'

def thanks(request):

	return render(request, 'thanks.html')

def catch_feed(request):
	
	if request.method == 'POST':
		form = UploadFileForm(data=request.POST)

		if form.is_valid():
			saved_form = form.save()
			return HttpResponseRedirect('/thanks/')
		else:
			print 'something went wrong'
			print form.errors

	url = request.GET['url']
	title = request.GET['title']
	data = enrich(url, title)
	description = request.GET['description']
	
	def get_items(x):
		items = []
		for i in x:
			items.append(i['name'])
		return ', '.join(items)

	authors = get_items(data['authors'])
	pubdate = None
	if data['published'] is not None:
		pubdate = datetime.datetime.fromtimestamp(data['published']/ 1000)
	
	thumbnail = None
	if len(data['images']) > 0:
		thumbnail = data['images'][0]['url']
	
	form = UploadFileForm(initial={'title':data['title'], 'provider_url': data['original_url'], 'author': authors,
							'provider_name': data['provider_name'], 'bookmark_date': datetime.datetime.now(),
							'pub_date': pubdate, 'summary': data['summary'], 'text': data['text'],
							'thumbnail': thumbnail, 'description': description, 'tags': get_items(data['keywords'])})

	context_dict = {'url': data['summary'], 'file_form' : form, 'thumbnail': thumbnail, 'title': data['title'], 'authors': authors, 'pubdate': pubdate }
	
	return render(request, 'bookmarklet.html', context_dict)

def feed(request):
	files = File.objects.select_related().all().order_by('-id')

	context_dict = {'files': files, 'landing': 'Landing'}
	
	return render(request, 'feeds.html', context_dict)


def button(request):
	
	return render(request, 'bookmarklet.html')

def search(request):
	try:
		search_item = request.GET['term']
	except:
		search_item = ''
	
	files = File.objects.filter(text__contains=search_item).order_by('-id')

	context_dict = {'files': files, 'search_term': search_item}
	
	return render(request, 'search.html', context_dict)

def tagged_items(request, tag):
	
	files = File.objects.filter(tags__name__in=[tag]).order_by('-id')

	context_dict = {'files': files, 'tag_term': tag}

	return render(request, 'search.html', context_dict)

def account(request):
	
	domain = request.META['HTTP_HOST']

	if str(domain) == '127.0.0.1:8000':
		button = 'devel'
	else:
		button = 'prod'

	context_dict = {'type': button}
	
	return render(request, 'button.html', context_dict)
