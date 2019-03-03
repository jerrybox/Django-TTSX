from django.test import TestCase

from ttsx.sx_user.models import UserModel, UserAddress
from ttsx.sx_order.models import OrderModel

# Create your tests here.


class OrderModelTestCase(TestCase):
	def setUp(self):
		testuser = UserModel.objects.create(
			username='testcase', 
			password='password123', 
			password_c='password123', 
			email='testcase@email.com'
			)
		address = UserAddress.objects.create(
			user=testuser,
			recipients="赵钱孙李",
			phone="17189562378",
			addressee_p="085422",
			direction="中国北京东城天安门1号",
			)
		OrderModel.objects.create(
			o_user=testuser, 
			o_total=1234.00, 
			o_address=address.complete_address, 
			)
	
	def test_order_exist(self):
		order = OrderModel.objects.get(o_total=1234.00)
		self.assertEqual(order.o_status, 'NotPaid')

