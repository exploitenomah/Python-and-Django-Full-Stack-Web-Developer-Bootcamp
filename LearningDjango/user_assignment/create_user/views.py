from django.shortcuts import render
from create_user.models import MyUser
# Create your views here.

def index(request):
  users_list = MyUser.objects.order_by("firstname")
  data = { "users": users_list}
  return render(request, "create_user/index.html", context=data)