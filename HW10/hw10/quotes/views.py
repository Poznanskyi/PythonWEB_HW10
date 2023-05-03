from bson import ObjectId
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import QuoteForm, AuthorForm, TagForm
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def add_quotes(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:users')
        else:
            return render(request, 'quotes/add_quotes.html', context={'form': QuoteForm()})
    return render(request, 'quotes/add_quotes.html', context={'form': QuoteForm()})



def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            print(new_quote)
            print('OK')
            return redirect(to='quotes:users')
        else:
            return render(request, 'quotes/add_author.html', context={'form': AuthorForm(), 'message':'Wrong Data'})
    return render(request, 'quotes/add_author.html', context={'form': AuthorForm()})


def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(to='quotes:users')
        else:
            return render(request, 'quotes/add_tag.html', context={'form': TagForm(), 'message': 'Wrong Data'})
    return render(request, 'quotes/add_tag.html', context={'form': TagForm()})
