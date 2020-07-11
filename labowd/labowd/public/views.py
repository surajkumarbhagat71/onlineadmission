from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import ListView,View,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class HomeView(ListView):
    model = Peoples
    template_name = "home.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        return context


class PeopleDetailView(DetailView):
    model = Peoples
    template_name = "item.html"

    def get_context_data(self, **kwargs):
        context = super(PeopleDetailView, self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['related_peoples'] = Peoples.objects.exclude(pk=self.kwargs['pk'])
        return context

class AddRecordView(LoginRequiredMixin,View):
    form = AddRecordForm()
    def get(self,request,*args,**kwargs):
        data= {"form":self.form}
        return render(self.request,"addRecord.html",data)

    def post(self,request,*args,**kwargs):
        form = AddRecordForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            #todo : if not form is valid then what
            pass

class SearchListView(ListView):
    model = Peoples
    template_name = "search.html"

    def get_queryset(self):
        people = Peoples.objects.all()
        query = self.request.GET.get("search",None)
        if query:
            cond = Q(name__icontains=query) | Q(category__cat_title__icontains=query)
            return people.filter(cond)
        return people

