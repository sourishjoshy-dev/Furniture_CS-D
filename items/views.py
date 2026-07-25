from django.shortcuts import render,redirect,get_object_or_404
from .models import Furniture
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
def home(request):
    return render(request, 'home.html')

@login_required
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

@login_required
def view_items(request):
    items = Furniture.objects.all()
    return render(request, 'view_items.html', {'items': items})

@login_required
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



@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Furniture, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('view_items')
    return render(request, 'delete_item.html', {'item': item})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('view_items')
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})