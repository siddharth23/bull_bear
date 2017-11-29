from django.conf.urls import url
from .views import get,get_MFI
urlpatterns=[
    url(r'^detail/(?P<symbol>[\w\-]+)/$',view=get),
    url(r'^mfi/(?P<symbol>[\w\-]+)/$',view=get_MFI),
]