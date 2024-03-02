from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.
from .forms import ItemForm
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

def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})

def edit_item(request,id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance = None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id = id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})
