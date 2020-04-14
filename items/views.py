from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'


class ItemUpdateView(UpdateView):
    model = Item
    fields = ('title', 'description', 'price')
    template_name = 'item_edit.html'


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_delete.html'
    success_url = reverse_lazy('item_list')
