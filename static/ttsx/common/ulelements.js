// ul list元素实例化对象，便于操作
function Good(element) {
    this.ul_element = element;
    
    this.get_id = get_id;

    this.get_checkbox = get_checkbox;
    this.get_addbtn = get_addbtn;
    this.get_minusbtn = get_minusbtn;

    this.get_checked = get_checked;
    this.set_checked = set_checked;

    this.get_price = get_price;
    this.set_price = set_price;

    this.get_quantity = get_quantity;
    this.set_quantity = set_quantity;

    this.get_sum = get_sum;
    this.set_sum = set_sum;
    
    
    function get_id(){
        var good_id = this.ul_element.id;
        return good_id;
    }

    function get_checkbox(){
        var checkbox = this.ul_element.querySelector('input[type=checkbox]');
        return checkbox;
    }
    function get_addbtn(){
        var addbtn = this.ul_element.querySelector('.num_add a.add');
        return addbtn;
    }
    function get_minusbtn(){
        var minusbtn = this.ul_element.querySelector('.num_add a.minus');
        return minusbtn;
    }
    

    function get_checked(){
        var checked = this.ul_element.children[0].firstChild.checked;
        return checked;
    };
    function set_checked(bool){
        this.ul_element.children[0].firstChild.checked = bool;
    };


    function get_price(){
        var price = Number(this.ul_element.children[4].firstElementChild.textContent);
        return price;
    };
    function set_price(price){
        this.ul_element.children[4].firstElementChild.textContent = price;
    };
 	

 	function get_quantity(){
 	    var quantity = this.ul_element.children[5].querySelector('input').value;
 	    return quantity;
 	};
    function set_quantity(quantity){
        this.ul_element.children[5].querySelector('input').value = quantity;
    };


    function get_sum(){
        var sum = Number(this.get_quantity()) * Number(this.get_price());
        return sum;
    }
    function set_sum(){
       var sum = this.get_sum();
       this.ul_element.children[6].firstElementChild.textContent = sum;
    }
}

function get_goods(){
	var goods = [];
	var goods_ele = $('.cart_list_td');

	for (var i=0; i<goods_ele.length; i++){
		goods.push(new Good(goods_ele[i]));
	}
	return goods;
}

