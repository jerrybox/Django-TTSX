$(function(){

	var error_name = false;
	var error_password = false;

    
	$('#user_name').blur(function() {
		clear_error();
		check_user_name();
	});

	$('#pwd').blur(function() {
		clear_error();
		check_pwd();
	});

	//clear error from server
	function clear_error(){
		$(".login_error").html("");
	}

	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').next().html('请输入5-20个字符的用户名')
			$('#user_name').next().show();
			error_name = true;
		}
		else
		{
			$('#user_name').next().hide();
			error_name = false;
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}


	$(".input_submit").click(function(){
		check_user_name();
		check_pwd();
		clear_error();

		console.log("error_name:",error_name)
		console.log("error_password:",error_password)

		if(error_name == false && error_password == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});

})
