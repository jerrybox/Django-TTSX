//加减计算
function add_minus(num1, flag, num2){
	var num1 = Number(num1);
	var num2 = Number(num2);
	var sum;
	var minus;

	if (flag == '+'){
		sum = num1 + num2;
		return sum
	} else if (flag == '-'){
		minus = num1 - num2
		return minus
	}
}


// 增加商品数量
function addgoods() {
	var quantity_old = $('.num_show').val();
	var quantity_new = add_minus(quantity_old, '+', 1);
	var max_quantity = $('#repertory').text();

	if (quantity_new <= max_quantity){
		$('.num_show').val(quantity_new);
		tatal_price(quantity_new);
	} else {
		alert('很抱歉，库存不足！');
	}
}


// 减少商品数量
function subgoods(id) {
	var quantity_old = $('.num_show').val();
	var quantity_new = add_minus(quantity_old, '-', 1);

	if (quantity_new > 0){
		$('.num_show').val(quantity_new);
		tatal_price(quantity_new);
	} else {
		alert('亲! 生活不易啊, 至少买一个吧!');
	}
}


// 计算商品总价
function tatal_price(quantity_new) {
	var price = $('.show_pirze em').text();
	var total_price = Number(quantity_new) * Number(price);
	$('#price_total').text(total_price);
}


// 添加到购物车
function add_cart(id) {
	var num = $('.num_show').val();
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url:'/shopping/addgoods/',
        type:'POST',
        data: {'goods_id': id, 'num':num},
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success:function (data) {
            if (data.code == '200') {
                alert('已添加到购物车！')
                console.log(data);
            }
        },
        error:function (data) {
            console.log(data)
        }
    })
}


// 添加到购物车
function add_cart(id) {
	var num = $('.num_show').val();
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url:'/shopping/addgoods/',
        type:'POST',
        data: {'goods_id': id, 'num':num},
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success:function (data) {
            if (data.code == '200') {
                alert('已添加到购物车！')
                console.log(data);
            }
        },
        error:function (data) {
            console.log(data)
        }
    })
}


// 立即购买
function buy_cart() {
	var num = $('.num_show').val();
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    var redirect_url = $('.buy_btn').attr('href');
    var id = $('.buy_btn').attr('id');

    $.ajax({
        url:'/shopping/addgoods/',
        type:'POST',
        data: {'goods_id': id, 'num':num},
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success:function (data) {
            if (data.code == '200') {
                window.location.replace(redirect_url);
                console.log(data);
            }
        },
        error:function (data) {
            console.log(data);
        }
    })
}

$('.buy_btn').click(buy_cart);
