from django.conf.urls import patterns, url

import source_code_view.views

urlpatterns = [
    url(r'^$', source_code_view.views.index, name='index'),
    url(r'^search', source_code_view.views.search, name='search'),
]
