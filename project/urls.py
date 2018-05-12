from django.conf.urls import url
from app.views import FrontendView

urlpatterns = [
    url(r'^$', FrontendView.as_view()),
    url(r'^contact/$', FrontendView.contact, name='contact'),
]
