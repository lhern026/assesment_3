from django.shortcuts import render
from .models import Item
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', { 'items' : items})

class Add(CreateView):
    model= Item
    fields = '__all__'

