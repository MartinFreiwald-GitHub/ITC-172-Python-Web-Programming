from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product
from .forms import ProductForm

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def techtypes (request):
    type_list=ProductType.objects.all()
    return render(request, 'club/types.html', {'type_list': type_list})

def getproducts(request):
    product_list=Product.objects.all()
    return render (request, 'club/products.html', {'product_list': product_list})

def productdetail(request, id):
    detail=get_object_or_404(Product, pk=id)
    context = { 'detail': detail}
    return render (request, 'club/details.html',context=context )
#form view
def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'club/newproduct.html', {'form': form})

