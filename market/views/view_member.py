from django.shortcuts import render
from market.forms import TransForm, UserForm
from market.models import StandVendor, Stands, Translations, MarketStand


def stand(request):
    user_id = request.user.profile.id
    standList = StandVendor.objects.filter(vendor=user_id)

    return render(request, 'member/vendor/standList.html', {'user_id': user_id, 'standList': standList})


def standDetail(request, id):
    stand = Stands.objects.get(id=id)
    trans_list = Translations.objects.filter(marketStand=stand.standM_detail.id)
    return render(request, 'member/vendor/standDetail.html', {'stand': stand, 'trans_list': trans_list})


def newTrans(request, id):
    market_stand = MarketStand.objects.get(stand=id)
    stand = Stands.objects.get(id=id)
    if request.method == "POST":
        try:
            f = TransForm(request.POST)
            if f.is_valid():
                f = f.save()
                trans_list = Translations.objects.filter(marketStand=market_stand.id)

                return render(request, 'member/vendor/standDetail.html',
                              {'market_stand': market_stand, 'stand': stand, 'trans_list': trans_list})
            else:
                return render(request, 'member/vendor/editTrans.html',
                              {'f': f, 'message': "輸入錯誤", 'market_stand': market_stand})
        except Exception as e:
            e = "查無此買家"
            return render(request, 'member/vendor/editTrans.html',
                          {'f': f, 'message': e, 'success': True, 'market_stand': market_stand})
    else:
        f = TransForm()
    return render(request, 'member/vendor/editTrans.html', {'f': f, 'market_stand': market_stand})


def buyerTranslations(request):
    user_id = request.user.profile.id
    trans_list = Translations.objects.filter(buyer=user_id)
    bonus = request.user.profile.bonus

    return render(request, 'member/buyer/translations.html', {'trans_list': trans_list, 'bonus': bonus})


def memberDetail(request):
    return render(request, 'member/memberDetail.html')


def editMember(request):
    f = UserForm(instance=request.user)
    if request.method == "POST":
        try:
            f = UserForm(request.POST, instance=request.user)
            if f.is_valid():
                f = f.save(commit=True)
                return render(request, 'member/memberDetail.html',
                              {'success': True, 'message': '更新成功~'})
            else:
                return render(request, 'member/editMember.html',
                              {'f': f, 'message': "fail!", 'success': True})
        except Exception as e:
            e = "錯了"
            return render(request, 'member/editMember.html',
                          {'f': f, 'message': e, 'success': True})

    return render(request, 'member/editMember.html', {'f': f})
