function init(){
    var good_check = get_goods();
	var all_check = $('.settlements input[type=checkbox] ')[0];
	var balance_btn = $('.settlements .col04 a')[0];

	// 增加商品数量
	function addgoods() {
	    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
	    var good_id = this.id;
	    $.ajax({
	        url: '/shopping/addgoods/',
	        type: 'POST',
	        data: {'goods_id': good_id},
	        dataType: 'json',
	        headers: {'X-CSRFToken': csrf},
	        success:function (data) {
	            if (data.code == '200'){
	                // console.log(data);
	                $('.num_show_'+ String(good_id)).val(data.count);
	                $('#price'+ String(good_id)).html(data.goods_price);
	            }
	            total_price();
	        },
	        error:function (data) {
	            console.log(data)
	        }
	    })
	}


	// 减少商品数量
	function subgoods() {
	    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
	    var good_id = this.id;
	    $.ajax({
	        url:'/shopping/subgoods/',
	        type:'POST',
	        data:{'goods_id': good_id},
	        dataType:'json',
	        headers:{'X-CSRFToken':csrf},
	        success:function (data) {
	            if (data.code == '200') {
	                if (data.count >= 1){
	                    $('.num_show_'+ String(good_id)).val(data.count)
	                    $('#price'+ String(good_id)).html(data.goods_price)
	                }else {
	                    alert('亲! 生活不易啊, 至少买一个吧!')
	                }
	                total_price();
	                // console.log(data);
	            }
	        },
	        error:function (data) {
	            console.log(data)
	        }
	    })
	}

    
	//是否全选
	function check_all(){
		for (var i=0; i<good_check.length; i++){
			if (! good_check[i].get_checked()){
				return false
			} 
		}
		return true
	}

	// 更新商品总价
	function total_price() { 
		var goods_price = good_check;
		// var goods_price = $('.cart_list_td');
		var total_price = 0;
		var good_num = 0;

		for (var i=0; i<goods_price.length; i++){
			if (goods_price[i].get_checked()){
				total_price +=  goods_price[i].get_sum();
				good_num += 1;
			}
		}

        $('#tatal_price').html(total_price);
        $('#all_num').html(good_num);
	}

	//全选全不选
	all_check.onclick = function(){
		for (var i=0; i<good_check.length; i++){
			good_check[i].set_checked(this.checked);
		}
		total_price();
	}

	//监听单选事件
	for (var i=0; i<good_check.length; i++){

        // 加减符号添加事件
        good_check[i].get_addbtn().id = good_check[i].get_id();
        good_check[i].get_addbtn().onclick = addgoods;

        good_check[i].get_minusbtn().id = good_check[i].get_id();
        good_check[i].get_minusbtn().onclick = subgoods;


        good_check[i].set_sum();

		// 复选框添加事件
		good_check[i].get_checkbox().onclick = function(){
			if (! this.checked ){
				all_check.checked = false;
			} else if (check_all()) {
				all_check.checked = true;
			}
			total_price();
		};
	}
    total_price();


	//结算
	balance_btn.onclick = function(){
	    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
	    var dir_href = this.getAttribute('dir_href');
	    var goods_id_list = [];

		for (var i=0; i<good_check.length; i++){
			if (good_check[i].get_checked()){
				goods_id_list.push(good_check[i].get_id());
			}
		}

		var href = dir_href + '?' + 'goods_id_list=' + JSON.stringify({'goods_id': goods_id_list})
		window.location.replace(href);
	}

}


window.onload = init;

