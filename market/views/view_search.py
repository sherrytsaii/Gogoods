from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from market.models import Local, Markets, Stands, MarketLocal, MarketStand


# Create your views here.
def home(request):
    allcity = Local.objects.all()
    tpct = Local.objects.filter(city="台北市")
    ntpct = Local.objects.filter(city="新北市")

    if request.method == 'POST':
        query_city = request.POST['city']
        if query_city == '0':
            query_cate = request.POST['market']
            query_dist = request.POST['allcity']
            if query_cate == '0':
                if query_dist == '0':
                    markets_list = Markets.objects.all()
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
                else:
                    markets_list = Markets.objects.filter(market_detail__local__id=query_dist)
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
            if query_cate == '1':
                if query_dist == '0':
                    markets_list = Markets.objects.filter(category="優良市集")
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
                else:
                    mlist = Markets.objects.filter(category="優良市集")
                    markets_list = mlist.filter(market_detail__local__id=query_dist)
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
            if query_cate == '2':
                if query_dist == '0':
                    markets_list = Markets.objects.filter(category="綠色市集")
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
                else:
                    mlist = Markets.objects.filter(category="綠色市集")
                    markets_list = mlist.filter(market_detail__local__id=query_dist)
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
        if query_city == '1':
            query_cate = request.POST['market']
            query_dist = request.POST['tpct']
            if query_cate == '0':
                if query_dist == '0':
                    markets_list = Markets.objects.filter(market_detail__local_id__range=["1", "12"])
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
                else:
                    markets_list = Markets.objects.filter(market_detail__local_id=query_dist)
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
            if query_cate == '1':
                if query_dist == '0':
                    mlist = Markets.objects.filter(category="優良市集")
                    markets_list = mlist.filter(market_detail__local_id__range=["1", "12"])
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
                else:
                    mlist = Markets.objects.filter(category="優良市集")
                    markets_list = mlist.filter(market_detail__local_id=query_dist)
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
            if query_cate == '2':
                if query_dist == '0':
                    mlist = Markets.objects.filter(category="綠色市集")
                    markets_list = mlist.filter(market_detail__local_id__range=["1", "12"])
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
                else:
                    mlist = Markets.objects.filter(category="綠色市集")
                    markets_list = mlist.filter(market_detail__local_id=query_dist)
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
        if query_city == '2':
            query_cate = request.POST['market']
            query_dist = request.POST['ntpct']
            if query_cate == '0':
                if query_dist == '0':
                    markets_list = Markets.objects.filter(market_detail__local_id__range=["13", "41"])
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
                else:
                    markets_list = Markets.objects.filter(market_detail__local_id=query_dist)
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
            if query_cate == '1':
                if query_dist == '0':
                    mlist = Markets.objects.filter(category="優良市集")
                    markets_list = mlist.filter(market_detail__local_id__range=["13", "41"])
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
                else:
                    mlist = Markets.objects.filter(category="優良市集")
                    markets_list = mlist.filter(market_detail__local_id=query_dist)
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
            if query_cate == '2':
                if query_dist == '0':
                    mlist = Markets.objects.filter(category="綠色市集")
                    markets_list = mlist.filter(market_detail__local_id__range=["13", "41"])
                    return render(request, 'search/markets.html', {'markets_list': markets_list})
                else:
                    mlist = Markets.objects.filter(category="綠色市集")
                    markets_list = mlist.filter(market_detail__local_id=query_dist)
                    return render(request, 'search/markets.html', {'markets_list': markets_list})

        return render(request, 'search/markets.html', )

    return render(request, 'home.html', {'allcity': allcity, 'tpct': tpct, 'ntpct': ntpct})


def post(request, pk):
    p = Markets.objects.get(pk=pk)
    stand_list = MarketStand.objects.filter(market=p)

    return render(request, 'search/marketsdetail.html', {'post': p, 'stand_list': stand_list})


def maptest(request):
    return render(request, 'search/maptest.html')
