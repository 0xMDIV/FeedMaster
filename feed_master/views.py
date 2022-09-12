import feedparser
import logging

from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import FeedForm
from .models import Feed


# Create your views here.
def index(request):
    return render(request, 'base.html')


# all feeds
def overview_feeds(request):
    feeds = Feed.objects.all()
    feeds_list = fetch_feeds(feeds)
    feed_form = FeedForm()

    if request.method == "POST":
        feed_form = FeedForm(request.POST)
        if feed_form.is_valid():
            try:
                feed_form.save()
                messages.success(request, 'New Feed added!')
            except Exception as e:
                messages.warning(request, f'New Feed couldnt be added: {e}')

            return redirect('overview')



    return render(request, 'overview.html', {
        'feeds_list': feeds_list,
        'feed_form': feed_form,
    })


def detail_feed(request, pk=None):
    if pk is not None:
        feed = get_object_or_404(Feed)
        print(f"Feed Detail: {feed}")


def add_feed(request):
    feed_form = FeedForm()

    if request.method == "POST":
        feed_form = FeedForm(request.POST)
        if feed_form.is_valid():
            feed_form.save()

    return render(request, '', {
        'form': feed_form,
    })
    pass


def remove_feed(request):
    pass


def subscribed_feeds(request):
    pass


def feeds_list(request):
    pass


def fetch_feeds(feeds):
    print(f"Fetch feeds: {feeds}")
    feeds_list = []
    # todo: add feed name, then the list of feed data and each data is a dict

    for entry in feeds:
        feed = feedparser.parse(entry.url)

        feed_data = []
        for data in feed.entries:
            feed_data.append({'title': data.title, 'author': data.author, 'content': data.content})

        feeds_list.append(feed_data)

    return feeds_list
