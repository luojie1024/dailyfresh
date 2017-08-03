# coding=utf-8
from haystack.views import SearchView
from .models import GoodsInfo
from df_cart.models import CartInfo


class MySeachView(SearchView):
    def extra_context(self):
        """
        重载extra_context来添加额外的context内容
        """

        # 查询新品
        newgood = GoodsInfo.objects.all().order_by('-id')[:2]
        # 保持原来context不变
        context = super(MySeachView, self).extra_context()
        # 新增context
        context['page_name'] = 1
        context['title'] = '查询结果'
        context['newgood'] = newgood
        return context
