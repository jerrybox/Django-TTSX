from django.test import TestCase

from django.test import TestCase

from sx_user.models import UserModel, UserAddress


# Create your tests here.


class UserModelTestCase(TestCase):
	def setUp(self):
		UserModel.objects.create(
			username='testcase', 
			password='password123', 
			password_c='password123', 
			email='testcase@email.com'
			)

	def test_user_exist(self):
		testuser = UserModel.objects.get(username='testcase')
		self.assertEqual(testuser.password, 'password123')
		self.assertEqual(testuser.password_c, 'password123')
		self.assertEqual(testuser.email, 'testcase@email.com')


class UserAddressTestCase(TestCase):
	def setUp(self):
		testuser = UserModel.objects.create(
			username='testcase', 
			password='password123', 
			password_c='password123', 
			email='testcase@email.com'
			)
		UserAddress.objects.create(
			user=testuser,
			recipients="赵钱孙李",
			phone="17189562378",
			addressee_p="085422",
			direction="中国北京东城天安门1号",
			)


	def test_complete_address(self):
		address = UserAddress.objects.get(recipients="赵钱孙李", phone="17189562378")
		self.assertEqual(address.complete_address, address.recipients + address.phone + address.direction)
