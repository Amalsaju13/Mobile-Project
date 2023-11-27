from django.shortcuts import render, redirect
from owner.models import Mobiles
from django.views.generic import View,CreateView,ListView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from customer.forms import UserRegistrationForm, LoginForm,PasswordResetForm,OrderForm,ReviewForm
from django.contrib.auth import authenticate, login,logout
from customer.models import Carts,Orders,Reviews
from customer.decorators import sign_in_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Sum



# Create your views here.
@method_decorator(sign_in_required,name='dispatch')
class CustomerIndexView(ListView):
    model = Mobiles
    template_name = 'custhome.html'
    context_object_name = 'mobiles'

    # def get(self, request, *args, **kwargs):
    #     qs = Mobiles.objects.all()
    #     return render(request, "custhome.html", {"mobiles": qs})


class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'signup.html'
    success_url = 'signin'
    # def get(self, request, *args, **kwargs):
    #     form = UserRegistrationForm()
    #     return render(request, "signup.html", {"form": form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('signin')
    #     else:
    #         return render(request, 'signup', {'form': form})


class SigInView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'signin.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                print('login successs')
                login(request,user)
                return redirect("custhome")
            else:
                print('login failed')
                return render(request, 'signin.html', {'form': form})
@sign_in_required
def SignOut(request,*args,**kwargs):
    logout(request)
    return redirect('signin')

@method_decorator(sign_in_required,name='dispatch')
class PasswordResetView(View):
    def get(self,request):
        form=PasswordResetForm()
        return render(request,'password_reset.html',{'form':form})
    def post(self,request):
        form=PasswordResetForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data.get('oldpassword')
            newpassword=form.cleaned_data.get('newpassword')
            user=authenticate(request,username=request.user,password=oldpassword)
            if user:
                user.set_password(newpassword)
                user.save()
                return redirect('signin')
            else:
                return render(request, 'password_reset.html', {'form': form})
        else:
            return render(request, 'password_reset.html', {'form': form})

@sign_in_required
def AddToCart(request,*args,**kwargs):
    mobile=Mobiles.objects.get(id=kwargs['id'])
    user=request.user
    cart=Carts(product=mobile,user=user)
    cart.save()
    messages.success(request,"Item added to Cart")
    return redirect('custhome')

@method_decorator(sign_in_required,name='dispatch')
class ViewMyCart(ListView):
    model=Carts
    template_name = 'cart.html'
    context_object_name = 'carts'

    # def get_queryset(self):
    #     return Carts.objects.filter(user=self.request.user).exclude(status='cancelled').order_by('-date')
    def get(self,request,*args,**kwargs):
        carts=Carts.objects.filter(user=self.request.user).exclude(status='cancelled').order_by('-date')
        total=Carts.objects.filter(user=request.user).exclude(status='cancelled').aggregate(Sum('product__price'))
        gtotal=total.get("product__price__sum")
        context={"carts":carts,"total":gtotal}
        return render(request,'cart.html',context)


def remove_from_cart(request,*args,**kwargs):
    cart=Carts.objects.get(id=kwargs['id'])
    cart.status = "cancelled"
    cart.save()
    messages.error(request,"Item removed from Cart")
    return redirect('viewmycart')

class OrderCreateView(CreateView):
    form_class = OrderForm
    template_name = 'ordercreate.html'
    model=Orders

    def post(self, request, *args, **kwargs):
        cart_id=kwargs.get("c_id")
        product_id=kwargs.get("p_id")
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            product=Mobiles.objects.get(id=product_id)
            user=request.user
            order.product=product
            order.user=user
            order.save()
            cart=Carts.objects.get(id=cart_id)
            cart.save()
            messages.success(request,"Your order has been placed")
        return redirect("custhome")

class OrderListView(ListView):
    model=Orders
    template_name = 'orderlist.html'
    context_object_name = 'orders'
    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user).order_by("-date")

class CreateReview(CreateView):
    model = Reviews
    form_class = ReviewForm
    template_name = "postreview.html"

    def post(self, request, *args, **kwargs):
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.posted_by=self.request.user
            product=Mobiles.objects.get(id=kwargs["id"])
            review.product=product
            review.save()
            messages.success(request,"Your Review has been Posted")
            return redirect("custhome")
        else:
            return render(request,self.template_name,{"form":form})

class ProductDetailView(DetailView):
    model = Mobiles
    template_name = "Productdetail.html"
    context_object_name = "mobile"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        mobile=self.get_object()
        reviews=mobile.reviews.all()
        context["reviews"]=reviews
        return context




