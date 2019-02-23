from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse

from sx_user.models import UserTicketModel


class UserMiddle(MiddlewareMixin):
    def process_request(self, request):
        # 需要登录验证的页面
        need_login = ['/store/list/',
                      '/user/user_center_info/',
                      '/user/user_center_order/',
                      '/user/user_center_site/',
                      '/shopping/detail/',
                      '/shopping/addgoods/',
                      '/shopping/subgoods/',
                      '/shopping/goodsnum/',
                      '/shopping/addcart/',
                      '/shopping/buycart/',
                      '/shopping/tatalprice/',
                      '/shopping/delgoodscart/',
                      '/order/place_order/',
                      '/order/user_center_info/',
                      '/order/user_center_order/',
                      '/order/user_center_site/',
                      '/user/logout/',
                      ]

        # 必须在未登录状态下才能访问的页面
        without_login = ['/user/login/',
                         '/user/register/',
        ]

        ticket = request.COOKIES.get('ticket')
        if ticket:
            user_ticket = UserTicketModel.objects.filter(ticket=ticket).order_by('-out_time').first()
            # user ticket 存在
            if user_ticket:
                # ticket 已过期
                if datetime.now() > user_ticket.out_time.replace(tzinfo=None):
                    return HttpResponseRedirect(reverse('user:login'))
                else:
                    # 必须未登录状态下访问
                    if request.path in without_login:
                        referer_url = request.META.get('HTTP_REFERER')
                        if not referer_url:
                            return HttpResponseRedirect(reverse('store:index'))    
                        else:
                            return HttpResponseRedirect(referer_url)
                    # 必须登录及游客页面
                    else:
                        request.user = user_ticket.user
                        return None
            else:
                if request.path in need_login:
                    return HttpResponseRedirect(reverse('user:login'))
                return None
        else:
            if request.path in need_login:
                return HttpResponseRedirect(reverse('user:login'))
            return None


        # # 判断页面是否需要登录
        # if request.path in need_login:
        #     # 如果需要验证登录,则获取cookies中的ticket值
        #     ticket = request.COOKIES.get('ticket')
        #     # 如果cookies中没有ticket值, 则跳转到登录页面
        #     if not ticket:
        #         return HttpResponseRedirect(reverse('user:login'))
        #     # 将获取的ticket值保存在变量user_ticket中
        #     user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()

        #     if user_ticket:
        #         # 判断ticket值是否过期，如果没过期
        #         if datetime.now() > user_ticket.out_time.replace(tzinfo=None):
        #             # 过期处理
        #             # 这里会不会造成，过期会话下访问，会挤掉或删掉未过期的会话
        #             UserTicketModel.objects.filter(user=user_ticket.user).delete()
        #             return HttpResponseRedirect(reverse('user:login'))
        #         else:
        #             # 没过期处理
        #             request.user = user_ticket.user
        #             # ttsx_users_ticket表中查询当前的user, 且ticket值不等于cookie中的ticket值
        #             # 没看懂这是什么意思
        #             UserTicketModel.objects.filter(Q(user=user_ticket.user) & Q(ticket=ticket))
        #             return None
        #     else:
        #         return HttpResponseRedirect(reverse('user:login'))
        # else:
            
        #     return None



