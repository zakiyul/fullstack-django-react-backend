from django.shortcuts import render, redirect
from .models import Chef
from food.models import FoodModel

# Create your views here.
def index(req):
  template_name = 'index.html'

  return render(req, template_name, context={
    'header': 'Homepage eki-dev',
    'chefs': Chef.objects.all(),
    'foods': FoodModel.objects.all(),
    'home': 'active' 
  })

def addChef(req):
  template_name = 'add-chef.html'

  if req.method == 'POST':
    nama    = req.POST.get('nama')
    umur    = req.POST.get('umur')
    gender  = req.POST.get('gender')
    foto    = req.FILES.get('foto')
    show    = req.POST.get('show')
    if show == 'on':
      show = True
    else:
      show = False
    
    data        = Chef()
    data.nama   = nama
    data.umur   = umur
    data.gender = gender
    data.foto   = foto
    data.show   = show
    data.save()
    return redirect('/')

  return render(req, template_name, context={
    'header': 'Add Chef',
    'chefs': Chef.objects.all(),
    'addChef': 'active',
    'action': 'Add'
  })

def editChef(req, pk):
  template_name = 'add-chef.html'

  if req.method == 'POST':
    data        = Chef.objects.get(id=pk)  

    nama    = req.POST.get('nama')
    umur    = req.POST.get('umur')
    gender  = req.POST.get('gender')
    show    = req.POST.get('show')

    if req.FILES:
      foto        = req.FILES.get('foto')
      data.foto   = foto

    if show == 'on':
      show = True
    else:
      show = False

    data.nama   = nama
    data.umur   = umur
    data.gender = gender
    data.show   = show
    data.save()
    return redirect('/')

  return render(req, template_name, context={
    'header': 'Homepage',
    'chefs': Chef.objects.all(),
    'chef': Chef.objects.get(id=pk),
    'action': 'Edit'
  })

def deleteChef(request, pk):
  template_name = 'delete.html'

  if request.method == 'POST':
    data = Chef.objects.get(id=pk)
    data.delete()
    return redirect('/')
  
  return render(request, template_name, context={
    'chef': Chef.objects.get(id=pk),
    'header': 'Delete Page'
  })