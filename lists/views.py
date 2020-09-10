from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    """Домашняя страница"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/unique-of-a-kind-list')
    return render(request, 'index.html')


def view_list(request):

    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})



