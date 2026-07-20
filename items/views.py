from django.shortcuts import render,redirect,get_object_or_404
from.models import Furniture


# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def add_item(request):
    #  logic 
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        material = request.POST.get('material')
        colour = request.POST.get('colour')
        price = request.POST.get('price')

        furniture = Furniture(item_name=item_name, material=material, colour=colour, price=price)
        furniture.save()

        return redirect('view_items')
    return render(request, 'add_item.html')

def view_items(request):
    items = Furniture.objects.all()
    return render(request, 'view_items.html', {'items': items})

def edit_item(request, item_id):
    item = get_object_or_404(Furniture, id=item_id)
    if request.method == 'POST':
        item.item_name = request.POST.get('item_name')
        item.material = request.POST.get('material')
        item.colour = request.POST.get('colour')
        item.price = request.POST.get('price')
        item.save()
        return redirect('view_items')
    return render(request, 'edit_item.html', {'item': item})



def delete_item(request, item_id):
    item = get_object_or_404(Furniture, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('view_items')
    return render(request, 'delete_item.html', {'item': item})