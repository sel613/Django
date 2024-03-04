from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
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

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


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

class FoodDetail(DetailView):
    model = Item
    template_name = "food/detail.html"


def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})


# class based view for create item
class CreateItem(CreateView):
    model = Item;
    fields = ['item_name','item_desc','item_price','item_img']
    template_name = 'food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)    

def edit_item(request,id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance = item)
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
