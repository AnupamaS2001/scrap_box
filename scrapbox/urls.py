"""
URL configuration for scrapbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from scrapapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("sign_up/",views.SignupView.as_view(),name="sign_up"),
    path("signin/",views.SigninView.as_view(),name="login"),
    path("signout/",views.SignoutView.as_view(),name="signout"),
    path("profile_edit/<int:pk>",views.ProfileView.as_view(),name="edit"),
    path("profile_detail/<int:pk>",views.ProfileDetailView.as_view(),name="detail"),
    path("scrapadd/",views.ScrapAddView.as_view(),name="scrap_add"),
    path("scraplist/",views.ScrapListView.as_view(),name="scrap_list"),
    path("scrapdetail/<int:pk>/",views.ScrapDetailView.as_view(),name="scrap_detail"),
    path("scrapdelete/<int:pk>/",views.ScrapDeleteView.as_view()),
    path("product/<int:pk>/wishlist/",views.WishListView.as_view(),name="wishlist"),
    path("product/wishlist/list",views.WishListdetailView.as_view(),name="wishlistdetail"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
