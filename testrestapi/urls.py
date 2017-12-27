from django.conf.urls import url, include
from testrestapi.views import PartyDetail,PartyList

urlpatterns = [
	url(r'^list/',PartyList.as_view()),
        url(r'^detail/(?P<pk>[0-9]+)$', PartyDetail.as_view()),
]
