from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import add_item_form, purchase_form
from .models import item, category, purchase, sale, cartitem

@login_required(login_url='/admin')
def home(request):
    items = item.objects.all()
    total = 0
    total_qty = 0
    for i in items:
        total += (i.price * i.stock)
        total_qty += i.stock
    val = sale.objects.all()
    profit = 0
    total_sales = 0
    sales_qty = 0
    for i in val:
        profit += i.profit
        total_sales += i.total
        sales_qty += i.qty

    return render(request, 'index.html', {'total': total, 'total_qty': total_qty,
                                          'profit': profit, 'total_sales': total_sales, 'sales_qty': sales_qty})


@login_required(login_url='/admin')
def add_item(request):
    form = add_item_form
    data = category.objects.all()
    if request.method == 'POST':
        a = item(name=request.POST['name'], brand=request.POST['brand'],
                 size=request.POST['size'], price=request.POST['price'],
                 mrp=request.POST['mrp'], stock=request.POST['stock'], reorder_level=request.POST['reorder_level'])
        a.save()
    return render(request, 'add_item.html', {'form': form, 'data': data})

@login_required(login_url='/admin')
def addtocart(request, slug):
    products = get_object_or_404(item, id=slug)
    orderitem, created = cartitem.objects.get_or_create(item=products)

    if cartitem.objects.filter(item__id=products.id).exists():
        orderitem.quantity += 1
        orderitem.save()
    else:

        cart = cartitem.objects.create()
        cart.item.add(orderitem)

    return redirect("sale")

@login_required(login_url='/admin')
def place_order(request):
    items = cartitem.objects.all()
    for i in items:
        id=i.item.id
        name = i.item.name
        brand = i.item.brand
        size = i.item.size
        mrp = i.item.mrp
        price = i.item.price
        qty=i.quantity

        total = int(mrp) * int(qty)
        tprice = int(price) * int(qty)
        profit = total - tprice
        a = sale(name=name, brand=brand, size=size, price=price, mrp=mrp, qty=qty, total=total, profit=profit)
        a.save()
        itm = item.objects.get(id=id)
        if item.objects.filter(id=id).exists():
            itm.stock -= int(qty)
            itm.save()
    cartitem.objects.all().delete()
    return redirect('sale')

@login_required(login_url='/admin')
def sales(request):
    data = item.objects.all()
    datas = cartitem.objects.all()
    return render(request, 'sale.html', {'data': data,'datas': datas})
@login_required(login_url='/admin')
def deletecartitem(request,slug):
    products = get_object_or_404(item, id=slug)
    cartitem.objects.filter(item=products).delete()
    return redirect("sale")
@login_required(login_url='/admin')
def purchases(request):
    data = category.objects.all()
    form = purchase_form
    if request.method == 'POST':
        price = request.POST['price']
        qty = request.POST['qty']
        total = int(price) * int(qty)

        form1 = purchase(name=request.POST['name'], brand=request.POST['brand'],
                         size=request.POST['size'], price=request.POST['price'],
                         mrp=request.POST['mrp'], qty=request.POST['qty'], total=total)

        form1.save()

        if item.objects.filter(name=request.POST['name'], size=request.POST['size'],
                               mrp=request.POST['mrp']).exists():
            p_item = item.objects.get(name=request.POST['name'], brand=request.POST['brand']
                                      , size=request.POST['size'], mrp=request.POST['mrp'])
            qty = request.POST['qty']
            p_item.stock += int(qty)
            p_item.save()
        else:
            additem = item(stock=request.POST['qty'], name=request.POST['name'], brand=request.POST['brand']
                           , price=request.POST['price'], size=request.POST['size'], mrp=request.POST['mrp'])
            additem.save()

        return render(request, 'purchase.html', {'form': form, 'data': data})

    return render(request, 'purchase.html', {'form': form, 'data': data})

@login_required(login_url='/admin')
def show(request):
    data = item.objects.all()
    return render(request, 'inventory.html', {'data': data})

@login_required(login_url='/admin')
def find_item(request):
    data = category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        size = request.POST['size']
        if size == "":
            result = item.objects.filter(name=name)
        else:
            result = item.objects.filter(name=name, size=size)

        return render(request, 'inventory.html', {'data': result})

    return render(request, 'find.html', {'cat': data})


def logout(request):
    auth.logout(request)
    return redirect('/')