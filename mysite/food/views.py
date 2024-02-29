from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.

def index(request):
    items = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list':items,
    }
    # return HttpResponse(template.render(context,request))
    return render(request,'food/index.html',context)

def item(request):
    return HttpResponse('This is an item View')

def saveditem(request):
    return HttpResponse("<h1>These are your saved item</h1>")

def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    context ={
        'item':item,
    }
    # return HttpResponse("Item Details " % item)
    return render(request,'food/detail.html',context)