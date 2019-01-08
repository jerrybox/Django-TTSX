function init(){

	var good_check = $('.cart_list_td input[type=checkbox] ')
	var all_check = $('.settlements input[type=checkbox] ')[0]

	//是否全选
	function check_all(){
		for (var i=0; i<good_check.length; i++){
			if (! good_check[i].checked){
				return false
			} 
		}
		return true
	}

	// 更新商品总价
	function total_price() {
		var goods_price = $('.cart_list_td');
		var total_price = 0;

		for (var i=0; i<goods_price.length; i++){
			if (goods_price[i].children[0].firstChild.checked){
				total_price +=  Number(goods_price[i].children[6].firstElementChild.textContent);
			}
		}

        $('#tatal_price').html(total_price);
	}

	//全选全不选
	all_check.onclick = function(){
		for (var i=0; i<good_check.length; i++){
			good_check[i].checked = this.checked;
		}
		total_price();
	}

	//监听单选事件
	for (var i=0; i<good_check.length; i++){
		good_check[i].onclick = function(){
			if (! this.checked ){
				all_check.checked = false;
			} else if (check_all()) {
				all_check.checked = true;
			}
			total_price();
		};
	}

}

window.onload = init;

