from django.conf.urls import patterns, url

from crate.web.packages.views import ReleaseDetail

urlpatterns = patterns("",
    url(r"^(?P<package>[^/]+)/(?:(?P<version>[^/]+)/)?$", ReleaseDetail.as_view(), name="package_detail"),
)
