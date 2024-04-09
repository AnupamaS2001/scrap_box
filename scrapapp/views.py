from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,UpdateView,View
from django.urls import reverse
from scrapapp.forms import Register_form,Signin_form,Profile_form,Scrap_form
from django.contrib.auth import authenticate,login,logout
from scrapapp.models import UserProfile,Scrap,Wishlist

class SignupView(CreateView):
    template_name="register.html"
    form_class=Register_form

    def get_success_url(self):
        return reverse("login")
    
class SigninView(FormView):
    template_name="login.html"
    form_class=Signin_form

    def post(self,request,*args,**kwargs):
        form=Signin_form(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            passwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=passwd)
            if user_obj:
                login(request,user_obj)
                print(request.user)
                return redirect("scrap_list")
        return render(request,"login.html",{"form":form})
    
class ProfileView(UpdateView):
    template_name="profile.html"
    form_class=Profile_form
    model=UserProfile

    def get_success_url(self):
        return reverse("detail")
    
class ProfileDetailView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=UserProfile.objects.get(id=id)
        return render(request,"profiledetail.html",{"data":qs})

class ScrapAddView(CreateView):
    template_name="scrapadd.html"
    form_class=Scrap_form
    model=Scrap

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("scrap_list")
    
class ScrapListView(View):
    def get(self,request,*args,**kwargs):
        data=Scrap.objects.all()
        return render(request,"scraplist.html",{"data":data})
    
class ScrapDetailView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Scrap.objects.get(id=id)
        return render(request,"scrapdetail.html",{"data":qs})
    
class ScrapDeleteView(View):
        def get(self,request,*args, **kwargs):
            id=kwargs.get("pk")
            qs=Scrap.objects.get(id=id).delete()
            return redirect("scrap_list")
    

class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
    

class WishListView(View):
     def post(self,request,*args,**kwargs):
          id=kwargs.get("pk")
          scrap_obj=Scrap.objects.get(id=id)
          action=request.POST.get("action")
          wishlist,created=Wishlist.objects.get_or_create(user=request.user)
          if action =="add":
            wishlist.scrap.add(scrap_obj)
          elif action == "remove":
            wishlist.scrap.remove(scrap_obj)
          return redirect("scrap_list")

class WishListdetailView(View):
      def get(self,request,*args,**kwargs):
            data=Wishlist.objects.get(user=request.user)
            return render(request,"wishlist.html",{"data":data})
