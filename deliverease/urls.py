
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from core import views

from core.customer import views as customer_views
from core.courier import views as courier_views

customer_urlpatterns = [
    path('',customer_views.home, name='home'),
    path('profile/', customer_views.profile_page, name='profile'),
    path('payment-method/', customer_views.payment_method_page, name='payment-method'),

    
]

courier_urlpatterns = [
    path('',courier_views.home, name='home'),

]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('',views.home),

    path('sign-in/', auth_views.LoginView.as_view(template_name='sign-in.html')),
    path('sign-out/', auth_views.LogoutView.as_view(next_page='/')),
    path('sign-up/',views.sign_up),

    path('customer/', include((customer_urlpatterns, 'customer'))),
    path('courier/',include((courier_urlpatterns, 'courier'))),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

