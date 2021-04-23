from django.shortcuts import render,redirect
from .models import Item
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', { 'items' : items})

class Add(CreateView):
    model= Item
    fields = '__all__'


def delete_item(request, item_id):
    Item.objects.get(id=item_id).delete()
    return redirect('/')


