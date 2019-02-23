// order.js


// <script type="text/javascript">
// 	$('#order_btn').click(function() {
// 		localStorage.setItem('order_finish',2);

// 		$('.popup_con').fadeIn('fast', function() {

// 			setTimeout(function(){
// 				$('.popup_con').fadeOut('fast',function(){
// 					window.location.href = 'index.html';
// 				});	
// 			},3000)
			
// 		});
// 	});
// </script>




function addgoods(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/order/place_order/',
        type: 'POST',
        data: {'order_id': id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success:function (data) {
            if (data.code == '200'){
                console.log(data);
                $('.num_show_'+ id).val(data.count)
                $('#price'+ id).html(data.goods_price)
            }
            tatal_price();
        },
        error:function (data) {
            console.log(data)
        }
    })
}