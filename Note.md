
# Markdown:
--------------------------

Markdown [在线预览](http://mahua.jser.me/ "Markdown 在线预览")  


# JS:
--------------------------

jQuery 参考手册 - [选择器](http://www.w3school.com.cn/jquery/jquery_ref_selectors.asp "选择器")  
```
第一步 要确保selector选取到了正确element
```

```jquery
$("input[name$='username']").val().length
```
```
//自动转化类型直接比较
0 > $('.num_show_7').val()

"2" <= "1600"
false

```
```
$('.num_show_7').val(1)
$('.num_show_7').val() // '1'
$('.num_show_7').val() + 1 // '11'
```
```
text() - 设置或返回所选元素的文本内容
html() - 设置或返回所选元素的内容（包括 HTML 标记）
val() - 设置或返回表单字段的值
```
```
typeof all_check
console.dir( all_check)
```

# Python:
---------------------------

```jinja2
{% if msg %}
	<div class="login_error">{{ msg }}</div>
{% endif %}

<!-->tj_goods = {'type': 1, 'good':[1, 2, 3]}  jinjia 模板里面可以通过.key获取value</-->
{% for tj in tj_goods.goods %}  
{% endfor %}
```

jinja url 传参方式：
```
# reqeust.GET.get('gtype_id', '')
href="{% url 'store:list' %}?gtype_id={{fresh_fruit.gtype.id}}"

# def list(request, gtype_id)
href="{% url 'store:list' gtype_id=fresh_fruit.gtype.id %}"

```


```cmd
cd Desktop\code
venv3\Scripts\activate.bat
cd TTSX\Django-TTSX
python manage.py runserver  0.0.0.0:8000
```

```
print("*" * 50, ":", gtype_id)
```

# Django
---------------------------

```shell
python manage.py createsuperuser
admin
password123
```


#### request

	utils的UserAuthMiddleware使用自定义的user代替了session和auth中的user，
	所以同一浏览器下不能同时登录django admin 用户 与ttsx  前台用户


#### Admin

	templates/admin 下的模板文件（e.g login.html）会覆盖原始的Django admin模板文件，
	所以，原templates/admin文件夹改名为ttsxadmin



# DevOps
---------------------------

```shell
python --version
pip freeze > requirements.txt
pip install -r requirements.txt
```


# Git
---------------------------

```git
git rm -r --cache **/__pycache__
git rm -r --cache **/**/__pycache__
```

.gitignore
```
**/__pycache__/
```


# Test
---------------------------

http://localhost:8000/user/register/
```
jerry
password123
jerry@ttsx.com

jerry2
password123
jerry2@ttsx.com
```


# TODO(what to do next):
-----------------------------

缓存
记住我
评论
商品描述
ttsxadmin
搜索
验证码
库存实时更新


