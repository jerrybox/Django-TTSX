from django.shortcuts import render
from django.core.paginator import Paginator

from sx_store.models import GoodsValue, ArticleCategory


# 这里应该有一个商品推荐系统，可以接收一些限制条件
def recommend(gtype_id, count, order_field=None):
    """
    gtype_id: 食品类型id  None表示类型不限
    order_type：排序字段 "-g_price"
    count： 个数
    """
    if not gtype_id:
        if not order_field:
            goods = GoodsValue.objects.filter(isDelete=0)[0:count]
        else:
            goods = GoodsValue.objects.filter(isDelete=0).order_by(order_field)[0:count]
    else:
        if not order_field:
            goods = GoodsValue.objects.filter(gtype_id=gtype_id, isDelete=0)[0:count]
        else:
            goods = GoodsValue.objects.filter(gtype_id=gtype_id, isDelete=0).order_by(order_field)[0:count]

    data = {'type':gtype_id,
            'goods':goods
    }
    return data


# 商城首页
def index(request):
    # 首页水果展示
    if request.method == 'GET':

        data = {
            'fresh_fruit': recommend(1, 4, '-g_price'),
            'seafood_aquaculture': recommend(2, 4),
            'red_meat': recommend(3, 4),
            'poultry_egg': recommend(4, 4),
            'green_goods': recommend(5, 4),
            'quick_frozen': recommend(6, 4),
        }
        return render(request, 'index.html', data)


# 商品列表
def list(request):
    """
    TODO: 这应该对数据库查询结果（goods_all）进行缓存
    """
    if request.method == 'GET':
        
        gtype_id = request.GET.get('gtype_id')
        page_num = request.GET.get('page', 1)

        kinds = ArticleCategory.objects.all()

        goods_all = GoodsValue.objects.filter(gtype_id=gtype_id, isDelete=0)
        paginator = Paginator(goods_all, 5)
        goods = paginator.page(page_num)

        tj_goods = recommend(gtype_id, 3, '-g_price')

        data = {
            'kinds': kinds,
            'gtype_id':gtype_id,
            'goods': goods,
            'tj_goods': tj_goods
        }
        return render(request, 'list.html', data)

