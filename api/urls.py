from django.conf.urls import url
from .views import get,get_MFI,send_acknowledgement

urlpatterns=[
    url(r'^detail/(?P<symbol>[\w\-]+)/$',view=get),
    url(r'^mfi/(?P<symbol>[\w\-]+)/$',view=get_MFI),
    url('^acknowledge/',view=send_acknowledgement),
]