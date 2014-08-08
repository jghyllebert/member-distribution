from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import MemberForm
from .models import Member


class MemberCreateView(CreateView):
    form_class = MemberForm
    model = Member
    template_name = "members/form.html"


class MemberListView(ListView):
    model = Member
    template_name = "members/list.html"
    context_object_name = "members"


class MemberDetailView(DetailView):
    model = Member
    template_name = "members/detail.html"
    context_object_name = "member"