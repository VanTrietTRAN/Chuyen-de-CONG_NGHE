"""
URL configuration for view_template project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, register_converter, re_path
from polls import views
from mysite import converters
from apps.main import views as main_views
from credit import views as credit_views
from apps.main.views import AsyncView


register_converter(converters.FourDigitYearConverter, "yyyy")

extra_patterns = [
    path("reports/", credit_views.report),
    path("reports/<int:id>/", credit_views.report),
    path("charge/", credit_views.charge),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("articles/2003/", views.special_case_2003),
    path("articles/<int:year>/", views.year_archive),

    path("articles/<yyyy:year>/", views.year_archive),

    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),

    re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive),
    re_path(r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.month_archive),
    re_path(
        r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$",
        views.article_detail,
    ),

    path("blog/", views.page),
    path("blog/page<int:num>/", views.page),

    path("community/", include("aggregator.urls")),
    path("contact/", include("contact.urls")),

    path("", main_views.homepage),
    path("help/", include("apps.help.urls")),
    path("credit/", include(extra_patterns)),

    path(
        "<page_slug>-<page_id>/",
        include(
            [
                path("history/", views.history),
                path("edit/", views.edit),
                path("discuss/", views.discuss),
                path("permissions/", views.permissions),
            ]
        ),
    ),

    path("<username>/blog/", include("foo.urls.blog")),
    path("", views.blog.index),
    path("archive/", views.blog.archive),

    path("blog/<int:year>/", views.year_archive, {"foo": "bar"}),

    path("blog/", include("inner"), {"blog_id": 3}),
    path("archive/", views.archive),
    path("about/", views.about),

    path("articles/<int:year>/", views.year_archive, name="news-year-archive"),

    path("author-polls/", include("polls.urls", namespace="author-polls")),
    path("publisher-polls/", include("polls.urls", namespace="publisher-polls")),
    
    path("polls/", include("polls.urls")),

    path("async/", AsyncView.as_view(), name="async-demo"),


]



