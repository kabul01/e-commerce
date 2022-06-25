from django.urls import path

from django.conf import settings
from myshop.views import product_list,product_detail,search
from django.conf.urls.static import static



app_name = 'myshop'

urlpatterns = [

    path('', product_list, name='product_list'),

    path('<slug:category_slug>/', product_list,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', product_detail,
         name='product_detail'),
    path('product_search',search , name = 'search'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)