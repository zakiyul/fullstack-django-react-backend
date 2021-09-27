from django.shortcuts import render, redirect
from .models import FoodModel
from app.models import Chef

def addFood(request):
  template_name = 'add-food.html'
  chefPilih = False

  if request.method == 'POST':
    nama    = request.POST.get('nama')
    harga   = request.POST.get('harga')
    chef    = request.POST.get('chef')
    gambar  = request.FILES.get('foto')

    data = FoodModel()
    data.nama = nama
    data.harga = harga
    data.chef = Chef.objects.get(id=chef)
    data.gambar = gambar
    data.save()
    return redirect('/')


  
  return render(request, template_name, context={
    'header': 'Add Food',
    'chefs': Chef.objects.all(),
    'addFood':'active',
    'action':'Add',
    'chefPilih': chefPilih
  })
