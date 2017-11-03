from market.models import *
from django.contrib.auth.models import Group, User
import csv
import os


def get_Userdata(request):  # Table：ATM、ATMLocal
    workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    c = os.path.join(workpath, 'static/opendata/name.csv')
    vendor_group = Group.objects.get(name="Vendor")

    with open(c, "r", encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user = User.objects.create_user(username=row['username'], password=row['password'], first_name=row['first_name'], last_name=row['last_name'], email=row['email'])
            user.groups.add(vendor_group)
            user.save()
            profile = UserProfile(user=user)
            profile.save()
    return reader


def get_Standsdata(request):  # Table：Stands、StandVendor、MarketStands
    workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    c = os.path.join(workpath, 'static/opendata/Stands.csv')
    with open(c, "r", encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tmp = Stands.objects.create_standsdata(
                row['name'],
                row['phone'],
                row['desc']
            )
        # MarketStand Table
            market = Markets.objects.get(name=row['market'])
            marketStand = MarketStand(market=market, stand=tmp)
            marketStand.save()

        # StandVendor Table
            vendor = User.objects.get(username=row['vendor_username'])
            # vendor_profile = UserProfile.objects.get(user=vendor.id)
            standVendor = StandVendor(vendor=vendor.profile, stand=tmp)
            standVendor.save()

    return reader

def get_ATMdata(request):  # Table：ATM、ATMLocal
    workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    c = os.path.join(workpath, 'static/opendata/ATM.csv')

    with open(c, "r", encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tmp = ATM.objects.create_atmdata(
                row['Address'],
                row['Institution_name']
            )
            local = Local.objects.get(district=row['District'])
            atmLocal = ATMLocal(local=local, atm=tmp)
            atmLocal.save()
    return reader


def get_Localdata(request):  # Table：Local
    workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    c = os.path.join(workpath, 'static/opendata/Local.csv')
    with open(c, "r", encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Local.objects.create_localdata(
                row['city'],
                row['district']
            )
    return reader


def get_Parkingdata(request):  # Table：Parking、ParkingLocal
    workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    c = os.path.join(workpath, 'static/opendata/Parking.csv')
    with open(c, "r", encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tmp = Parking.objects.create_parkingdata(
                row['name'],
                row['addr']
            )
            local = Local.objects.get(district=row['district'])
            parkingLocal = ParkingLocal(local=local, parking=tmp)
            parkingLocal.save()

    return reader


def get_Marketsdata(request):  # Table：Markets、MarketLocal
    workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    c = os.path.join(workpath, 'static/opendata/Markets.csv')
    with open(c, "r", encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tmp = Markets.objects.create_marketsdata(
                row['name'],
                row['category'],
                row['addr'],
                row['desc']
            )
            local = Local.objects.get(district=row['district'])
            marketLocal = MarketLocal(local=local, market=tmp)
            marketLocal.save()

    return reader