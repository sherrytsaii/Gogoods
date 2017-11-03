from django.shortcuts import render
from market.forms import UserCreateForm
from django.contrib.auth.models import Group, User


# Create your views here.
def demo(request):
    return render(request, 'demo.html', )


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            identity = form.cleaned_data['identity']
            form.save()
            buyer_group = Group.objects.get(name="Buyer")
            vendor_group = Group.objects.get(name="Vendor")
            if identity == "buyer":
                new_user = User.objects.get(username=name)
                new_user.groups.add(buyer_group)
                new_user.save()
            if identity == "vendor":
                new_user = User.objects.get(username=name)
                new_user.groups.add(vendor_group)
                new_user.save()

            return render(request, 'registration/success.html')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', {'form': form})
