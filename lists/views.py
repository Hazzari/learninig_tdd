from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    """Домашняя страница"""
    return render(request, 'index.html')


def view_list(request):
    """Новый список"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/unique-of-a-kind-list/')

