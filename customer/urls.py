from django.urls import path
from customer import views

urlpatterns=[
    path("home",views.CustomerIndexView.as_view(),name="custhome"),
    path("accounts/register",views.SignUpView.as_view(),name="signup"),
    path("accounts/login", views.SigInView.as_view(), name="signin"),
    path('accounts/logout',views.SignOut,name='signout'),
    path("accounts/password/reset", views.PasswordResetView.as_view(), name="passwordreset"),
    path('carts/items/add/<int:id>',views.AddToCart,name='addtocart'),
    path("carts/all", views.ViewMyCart.as_view(), name="viewmycart"),
    path('carts/remove/<int:id>',views.remove_from_cart,name='removeitem'),
    path('order/add/<int:c_id>/<int:p_id>',views.OrderCreateView.as_view(),name='ordercreate'),
    path('orders/all',views.OrderListView.as_view(),name='orderlist'),
    path('orders/reviews/add/<int:id>',views.CreateReview.as_view(),name='review'),
    path('home/detail/<int:id>',views.ProductDetailView.as_view(),name="productdetail")

]