from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def home(request):
    # دریافت ۳ مورد از آخرین آیتم‌ها برای صفحه اصلی
    items = Item.objects.all()[:3]
    return render(request, "home.html", {"items": items})

def item_list(request):
    # دریافت تمام آیتم‌ها
    items = Item.objects.all()
    return render(request, "item_list.html", {"items": items})

def item_detail(request, id):
    # دریافت یک آیتم خاص یا نمایش خطای ۴۰۴ اگر یافت نشد
    item = get_object_or_404(Item, id=id)
    return render(request, "item_detail.html", {"item": item})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
