from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProfileImage
from .forms import LoginForm, ProductForm, ProfilePictureForm, RegistrationForm
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def comments(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        comment = request.POST.get('comment')
        uid = request.POST.get('id')
        if(comment == ''):
            return HttpResponse('Invalid request', status=400)
        else:
            user = get_object_or_404(User, pk=uid) 
            selected_product = Product.objects.get(pk=product_id)
            selected_product.comments.append({'comment': comment, 'user_name': f"{user.first_name} {user.last_name}"})
            selected_product.save()
            return JsonResponse({'message': 'success'})
    else:
        return HttpResponse('Invalid request', status=400)

def like_blog(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        uid = request.POST.get('id')
        is_like = request.POST.get('like')
        selected_product = Product.objects.get(pk=product_id)
        
        if is_like=="1":
            filtered_elements = False
            for i in selected_product.like_users:
                if i == uid:
                    filtered_elements = True
                    break

            if(filtered_elements):
                return JsonResponse({'message': 'You already liked this post.'})
            else:
                selected_product.likes += 1
                if selected_product.dislikes>0:
                    selected_product.dislikes -= 1
                selected_product.like_users.append(uid)
                try:
                    selected_product.dislike_users.remove(uid)
                except:
                    pass
                selected_product.save()
                return JsonResponse({'message': 'success'})
                
        else:
            filtered_elements = False
            for i in selected_product.dislike_users:
                if i == uid:
                    filtered_elements = True
                    break

            if(filtered_elements):
                return JsonResponse({'message': 'You already disliked this post.'})
            else:
                selected_product.dislikes += 1
                if selected_product.likes>0:
                    selected_product.likes -= 1
                selected_product.dislike_users.append(uid)
                try:
                    selected_product.like_users.remove(uid)
                except:
                    pass
                selected_product.save()
                return JsonResponse({'message': 'success'})
                 
    else:
        return HttpResponse('Invalid request', status=400)


def dashboard(request,id):
    try:
        profilePic =  get_object_or_404(ProfileImage, userId=id)
        product = Product.objects.all().filter(userId=id) 
        user = get_object_or_404(User, pk=id)    
    except:
        profilePic = None
        user = get_object_or_404(User, pk=id) 
        product = None
    return render(request, 'dashboard.html', {'user': user,'profilePic': profilePic, 'products': product})

def create_blog(request,id):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard', id=id)
    else:
        form = ProductForm()
    return render(request, 'create_blog.html', {'form': form,'id':id})


def upload_profile_pic(request,id):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProfilePictureForm()
    return render(request, 'upload_profile_pic.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    profilePic =  get_object_or_404(ProfileImage, userId=user.id)
                    product = Product.objects.all().filter(userId=user.id)
                    
                except:
                    profilePic = None
                    product = None
                return render(request, 'dashboard.html', {'user': user,'profilePic': profilePic, 'products': product})
            else:
                pass
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Add success message or redirect to login page
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

# --------------------------------------------------------------
def product_list(request, for_loged_users=False, id=0):
     products = Product.objects.all()
     if request.method == 'POST':
        for_loged_users = request.POST.get('data_to_pass')
        id = request.POST.get('id')
        
        return render(request, 'index.html', {'products': products, 'for_loged_users':for_loged_users, 'id':id })
     else:
        return render(request, 'index.html', {'products': products, 'for_loged_users':for_loged_users })
    


def product_detail(request, pk,id):
	product = Product.objects.get(pk=pk)
	return render(request, 'index2.html', {'product': product, 'id': id})

def product_detail_no_login(request, pk):
	product = Product.objects.get(pk=pk)
	return render(request, 'product_detail_no_login.html', {'product': product})

def product_detail_login(request, pk, id):
	product = Product.objects.get(pk=pk)
	return render(request, 'product_detail_login.html', {'product': product, 'id':id})


def edit_product(request, pk, id):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard', id=id)
               
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form': form})

def delete_product(request, pk,id):
	product = get_object_or_404(Product, pk=pk)
	if request.method == 'POST':
		product.delete()
		return redirect('dashboard', id=id)
	return render(request, 'delete.html', {'product': product})


def home(request):
	return HttpResponse('Hello, World!')
