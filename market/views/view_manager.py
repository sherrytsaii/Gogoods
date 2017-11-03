from django.shortcuts import render
from market.models import User, UserProfile, Group, StandVendor, Stands


def mainMag(request):
    return render(request, 'manager/manager.html')


def vendorMag(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            User.objects.filter(username=request.POST['delete']).delete()
        else:
            username = request.POST['updata']
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            email = request.POST['email']
            User.objects.filter(username=username).update(first_name=firstname)
            User.objects.filter(username=username).update(last_name=lastname)
            User.objects.filter(username=username).update(email=email)
    vendor_group = Group.objects.get(name="Vendor")
    vendor = User.objects.filter(groups=vendor_group)
    return render(request, 'manager/vendorManagement.html', {'vendor': vendor})


def buyerMag(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            User.objects.filter(username=request.POST['delete']).delete()
        elif 'updata' in request.POST:
            User.objects.filter(username=request.POST['updata']).update(first_name=request.POST['first_name'])
            User.objects.filter(username=request.POST['updata']).update(last_name=request.POST['last_name'])
            User.objects.filter(username=request.POST['updata']).update(email=request.POST['email'])
            UserProfile.objects.filter(user_id=User.objects.get(username=request.POST['updata']).id).update(
                bonus=int(request.POST['bonus']))
    buyer_group = Group.objects.get(name="Buyer")
    buyer = User.objects.filter(groups=buyer_group)

    return render(request, 'manager/buyerManagement.html', {'buyer': buyer})


def sdvdMag(request, id):
    if 'updata' in request.POST or 'delete' in request.POST:
        if 'updata' in request.POST:
            Stands.objects.filter(id=StandVendor.objects.get(id=request.POST['updata']).stand_id).update(
                name=request.POST['name'])
            Stands.objects.filter(id=StandVendor.objects.get(id=request.POST['updata']).stand_id).update(
                phone=request.POST['phone'])
            Stands.objects.filter(id=StandVendor.objects.get(id=request.POST['updata']).stand_id).update(
                desc=request.POST['desc'])
        elif 'delete' in request.POST:
            Stands.objects.filter(id=request.POST['delete']).delete()
    vendor_stand = StandVendor.objects.filter(vendor=UserProfile.objects.filter(user=User.objects.filter(id=id)))
    vendor = User.objects.get(id=id)
    return render(request, 'manager/standvendorManagement.html', {'vendor_stand': vendor_stand, 'vendor': vendor})
