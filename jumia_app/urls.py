from django.urls import path
# use class based views


from .views import *

urlpatterns = [
    path('', index, name='home'), 
    path('cart/', cart, name='cart'),
    # path to product details
    path('product/<int:pk>/', product_detail, name='product_detail'),
    # Registration
    path('register/', Registration.as_view(template_name='register.html'), name='register'),
    # Shipping Address
    path('checkout/', ShippingAddress.as_view(template_name = 'store/checkout.html'), name='checkout'),
    path('update_product/', updateProduct, name='update_product'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/<int:pk>/', views.profile_view, name='profile_view'),
    # path('profile/<int:pk>/edit/', views.edit_profile, name='edit_profile'),
    # path('profile/<int:pk>/delete/', views.delete_profile, name='delete_profile'),
    # path('profile/<int:pk>/follow/', views.follow_user, name='follow_user'),
    # path('profile/<int:pk>/unfollow/', views.unfollow_user, name='unfollow_user'),
    # path('profile/<int:pk>/like/', views.like_post, name='like_post'),
    # path('profile/<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
    # path('profile/<int:pk>/comment/', views.comment_post, name='comment_post'),
    # path('profile/<int:pk>/uncomment/', views.uncomment_post, name='uncomment_post'),
    # path('profile/<int:pk>/like_comment/', views.like_comment, name='like_comment'),
    # path('profile/<int:pk>/unlike_comment/', views.unlike_comment, name='unlike_comment'),
]

