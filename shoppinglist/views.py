from django.shortcuts import render,redirect
from shoppinglist.forms import ShoppinglistForm  
from shoppinglist.models import Shoppinglist  
# Create your views here.
def sitem(request):  
    if request.method == "POST":  
        form = ShoppinglistForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ShoppinglistForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    items = Shoppinglist.objects.all()  
    return render(request,"show.html",{'items':items})  
def edit(request, id):  
    item = Shoppinglist.objects.get(id=id)  
    return render(request,'edit.html', {'item':item})  
def update(request, id):  
    item = Shoppinglist.objects.get(id=id)  
    form = ShoppinglistForm(request.POST, instance = item)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'item': item})  
def destroy(request, id):  
    item = Shoppinglist.objects.get(id=id)  
    item.delete()  
    return redirect("/show")  