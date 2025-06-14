from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse("This is an item view.")

# def detail(request,item_id):
#     item = Item.objects.get(pk=item_id)
#     context ={
#         'item':item,
#     }
#     return render(request,'food/detail.html',context)


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

# add item
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form})

# This is a class based view for create item
class CreateItem(CreateView):
    model = Item;
    fields = ['item_name','item_des','item_price','item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)
    


# update item
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form':form,'item':item})

# delete item
def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item':item})