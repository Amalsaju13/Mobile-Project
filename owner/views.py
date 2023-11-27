from django.shortcuts import render, redirect
from owner.forms import MobileForm, OrderEditForm
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, TemplateView
from owner.models import Mobiles
from customer.models import Orders,Reviews
from django.core.mail import send_mail


# Create your views here.
class AddMobile(CreateView):
    model = Mobiles
    form_class = MobileForm
    template_name = 'add_mobile.html'
    success_url = reverse_lazy('allmobiles')
    # def get(self, request):
    #     form = MobileForm()
    #     return render(request, "add_mobile.html", {"form": form})
    #
    # def post(self, request):
    #     form = MobileForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    # print(form.cleaned_data.get("brand"))
    # print(form.cleaned_data.get("name"))
    # print(form.cleaned_data.get("specification"))
    # print(form.cleaned_data.get("ram"))
    # print(form.cleaned_data.get("strorage"))
    # print(form.cleaned_data.get("price"))
    # print(form.cleaned_data.get("quantity"))
    #
    # qs = Mobiles(
    #     brand=form.cleaned_data.get("brand"),
    #     name=form.cleaned_data.get("name"),
    #     specification=form.cleaned_data.get("specification"),
    #     ram=form.cleaned_data.get("ram"),
    #     storage=form.cleaned_data.get("strorage"),
    #     price=form.cleaned_data.get("price"),
    #     quantity=form.cleaned_data.get("quantity")
    # )
    # qs.save()

    #     return redirect("allmobiles")
    #     # return render(request, "add_mobile.html", {"msg": "Mobile added"})
    # else:
    #     return render(request, "add_mobile.html", {"form": form})


class MobileList(ListView):
    model = Mobiles
    template_name = "mobilelist.html"
    context_object_name = "mobiles"

    # def get(self,request):
    #     qs=Mobiles.objects.all()
    #     return render(request,"mobilelist.html",{'mobiles':qs})


class MobileDetailView(DetailView):
    model = Mobiles
    template_name = "mobiledetail.html"
    context_object_name = 'mobile'
    pk_url_kwarg = 'id'
    # def get(self,request,*args,**kwargs):
    #     qs=Mobiles.objects.get(id=kwargs.get("id"))
    #     return render(request,'mobiledetail.html',{'mobile':qs})


class MobileDeleteView(View):
    def get(self, request, *args, **kwargs):
        qs = Mobiles.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("allmobiles")


class ChangeMobile(UpdateView):
    model = Mobiles
    template_name = "mobilechange.html"
    form_class = MobileForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy('allmobiles')
    # def get(self,request,*args,**kwargs):
    #     qs=Mobiles.objects.get(id=kwargs.get("id"))
    #     form=MobileForm(instance=qs)
    #     return render(request,'mobilechange.html',{"form":form})
    #
    # def post(self,request,*args,**kwargs):
    #     qs=Mobiles.objects.get(id=kwargs.get("id"))
    #     form=MobileForm(request.POST,instance=qs,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("allmobiles")


class DashBoardView(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        neworders = Orders.objects.filter(status='order_placed')
        return render(request, self.template_name, {"neworders": neworders})


class OrderDetailView(DetailView):
    model = Orders
    template_name = 'orderdetail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'id'


class OrderChangeView(UpdateView):
    model = Orders
    template_name = "orderchange.html"
    form_class = OrderEditForm
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        order = Orders.objects.get(id=kwargs['id'])
        return render(request, self.template_name, {"order": order, "form": self.form_class})

    def post(self, request, *args, **kwargs):
        order = Orders.objects.get(id=kwargs["id"])
        form = OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            deliverydate = str(form.cleaned_data.get("expected_delivery_date"))
            form.save()
            send_mail(
                "Order Confirmation",
                "Your order delivered on " + deliverydate + " Thank You for Using Mobile Store",
                "geoamal12@gmail.com",
                ["amalsaju13@outlook.com"],
                fail_silently=False,
            )
            return redirect('dashboard')



