from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import PersonalShopper


class PersonalShopperCreateView(CreateView):
    model = PersonalShopper
    template_name = "personal_shoppers/form.html"


class PersonalShopperUpdateView(UpdateView):
    model = PersonalShopper
    template_name = "personal_shoppers/update.html"


class PersonalShopperListView(ListView):
    model = PersonalShopper
    template_name = "personal_shoppers/list.html"
    context_object_name = "p_shoppers"


class PersonalShopperDetailView(DetailView):
    model = PersonalShopper
    template_name = "personal_shoppers/detail.html"
    context_object_name = "p_shopper"