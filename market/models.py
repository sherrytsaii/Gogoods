from django.conf import settings
from django.contrib.auth.models import User, Permission, Group
from django.db import models
from django.utils.encoding import smart_text
import csv
import os

# Create your models here.
# Managers
class Local_Manager(models.Manager):
    def create_localdata(self, city, district):
        data = self.create(
            city=city,
            district=district
        )
        return data


class ATM_Manager(models.Manager):
    def create_atmdata(self, addr, institution):
        data = self.create(
            addr=addr,
            institution=institution
        )
        return data


class Parking_Manager(models.Manager):
    def create_parkingdata(self, name, addr):
        data = self.create(
            name=name,
            addr=addr
        )
        return data


class Stands_Manager(models.Manager):
    def create_standsdata(self, name, phone, desc):
        data = self.create(
            name=name,
            phone=phone,
            desc=desc
        )
        return data


class Markets_Manager(models.Manager):
    def create_marketsdata(self, name, category, addr, desc):
        data = self.create(
            name=name,
            category=category,
            addr=addr,
            desc=desc
        )
        return data


# class User_Manager(models.Manager):
#     def create_usersdata(self, user):
#         data = self.create(
#             user=user,
#         )
#         return data


# Models
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    bonus = models.IntegerField(null=True, blank=True, default=0)
    # objects = User_Manager

    def __str__(self):
        return smart_text(self.user.username)


class MarketPerm(models.Model):
    class Meta:
        permissions = (
            ("can_buy", "Buyer can buy"),
            ("can_sell", "vendor can sell"),
        )


class Parking(models.Model):
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=300)
    objects = Parking_Manager()

    def __str__(self):
        return smart_text(self.name)


class ATM(models.Model):
    addr = models.CharField(max_length=300)
    institution = models.CharField(max_length=50)  # 金融機構
    objects = ATM_Manager()

    def __str__(self):
        return smart_text(self.id)


class Markets(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    addr = models.CharField(max_length=300)
    desc = models.TextField(blank=True)
    objects = Markets_Manager()

    def __str__(self):
        return smart_text(self.name)


class Local(models.Model):
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)  # city：縣市  district：區
    objects = Local_Manager()

    def __str__(self):
        return smart_text(self.city) + smart_text(self.district)


class ParkingLocal(models.Model):
    parking = models.OneToOneField(Parking, related_name="parking_detail")
    local = models.ForeignKey(Local)
    objects = Parking_Manager()

    def __str__(self):
        return smart_text(self.parking)


class ATMLocal(models.Model):
    atm = models.OneToOneField(ATM, related_name="ATM_detail")
    local = models.ForeignKey(Local)

    def __str__(self):
        return smart_text(self.atm)


class MarketLocal(models.Model):
    market = models.OneToOneField(Markets, related_name="market_detail")
    local = models.ForeignKey(Local)

    def __str__(self):
        return smart_text(self.market)


class Stands(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    desc = models.TextField(blank=True)
    objects = Stands_Manager()

    def __str__(self):
        return smart_text(self.name)


class MarketStand(models.Model):
    stand = models.OneToOneField(Stands, related_name="standM_detail")
    market = models.ForeignKey(Markets)

    def __str__(self):
        return smart_text(self.stand)


class StandVendor(models.Model):
    stand = models.OneToOneField(Stands, related_name="standV_detail")
    vendor = models.ForeignKey(UserProfile)

    def __str__(self):
        return smart_text(self.stand.name)


class Translations(models.Model):
    marketStand = models.ForeignKey(MarketStand)
    buyer = models.ForeignKey(UserProfile)
    charge = models.IntegerField()
    add_bonus = models.IntegerField()
    used_bonus = models.IntegerField()
    desc = models.TextField(blank=True)
    trans_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return smart_text(self.id)


# Get Data
# def get_ATMdata():  # Table：ATM、ATMLocal
#     workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
#     c = os.path.join(workpath, 'static/opendata/ATM.csv')
#
#     with open(c, "r", encoding='big5', errors='ignore') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             tmp = ATM.objects.create_atmdata(
#                 row['Address'],
#                 row['Institution_name']
#             )
#             local = Local.objects.get(district=row['District'])
#             atmLocal = ATMLocal(local=local, atm=tmp)
#             atmLocal.save()
#     return reader
#
#
# def get_Localdata():  # Table：Local
#     workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
#     c = os.path.join(workpath, 'static/opendata/Local.csv')
#     with open(c, "r", encoding='big5', errors='ignore') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             Local.objects.create_localdata(
#                 row['city'],
#                 row['district']
#             )
#     return reader
#
#
# def get_Parkingdata():  # Table：Parking、ParkingLocal
#     workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
#     c = os.path.join(workpath, 'static/opendata/Parking.csv')
#     with open(c, "r", encoding='big5', errors='ignore') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             tmp = Parking.objects.create_parkingdata(
#                 row['name'],
#                 row['addr']
#             )
#             local = Local.objects.get(district=row['district'])
#             parkingLocal = ParkingLocal(local=local, parking=tmp)
#             parkingLocal.save()
#
#     return reader
#
#
# def get_Marketsdata():  # Table：Markets、MarketLocal
#     workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
#     c = os.path.join(workpath, 'static/opendata/Markets.csv')
#     with open(c, "r", encoding='big5', errors='ignore') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             tmp = Markets.objects.create_marketsdata(
#                 row['name'],
#                 row['category'],
#                 row['addr'],
#                 row['desc']
#             )
#             local = Local.objects.get(district=row['district'])
#             marketLocal = MarketLocal(local=local, market=tmp)
#             marketLocal.save()
#
#     return reader

