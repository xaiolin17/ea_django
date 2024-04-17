# app/views.py
import random
import datetime
from .models import SymbolModel
from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator


def home(request):

    return render(request, '')


def my_view(request):

    context = {
        'headline': 'Welcome',
        'user': request.user
    }

    return render(request, 'try.html', context)


def stock_list(request):
    # 查询所有的SymbolModel数据
    all_symbols = SymbolModel.objects.all()

    # 设置每页显示的记录数
    paginator = Paginator(all_symbols, 10)

    # 获取当前页的页码
    page_number = request.GET.get('page')

    # 获取当前页的数据
    page_obj = paginator.get_page(page_number)

    # 将当前页的对象传递给模板
    return render(request, 'stock_list.html', {'page_obj': page_obj})


def stock_list_break(request):
    symbols = SymbolModel.objects.all().values('symbol', 'datatime', 'OPrice', 'LPrice', 'HPrice', 'CPrice')
    return JsonResponse(list(symbols), safe=False)


def add_random_data(request):
    if request.method == 'POST':
        # 假设我们为价格范围设定了一些限制
        min_price = 100.00
        max_price = 200.00

        # 生成随机数据
        symbol = 'STK' + str(random.randint(1000, 9999))
        datatime = timezone.now()
        OPrice = round(random.uniform(min_price, max_price), 4)
        LPrice = round(random.uniform(min_price, max_price), 4)
        HPrice = round(random.uniform(min_price, max_price), 4)
        CPrice = round(random.uniform(min_price, max_price), 4)

        # 保存到数据库
        SymbolModel.objects.create(
            symbol=symbol,
            datatime=datatime,
            OPrice=OPrice,
            LPrice=LPrice,
            HPrice=HPrice,
            CPrice=CPrice
        )

        # 返回JSON响应表示成功
        return JsonResponse({'status': 'success', 'message': 'Random data inserted.'})

    # 如果不是POST请求，返回错误信息
    return JsonResponse({'status': 'error', 'message': 'Bad request. Must be POST.'}, status=400)