

$(function(){
    // 匹配电话
	var reg = /^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$/;
    $('#tel').blur(function () {
        console.log(123);
        var flag = reg.test($(this).val());
        if(flag){
            $.get('/check_tel/', {'tel':$(this).val()}, function (response) {
                console.log(response);

                if (response['status'] == '1') {
                    $('.content .int2').hide()
                }
                else {
                    $('.content .int2').show().html(response['msg'])
                }
            });

        }else {
            $('.content .int2').show().html('电话输入不正确')
        }
    });
    $('#tel').focus(function () {
        $('.content .int2').hide()
    });
    // 匹配 密码
	$('#password').blur(function () {
        var password = $(this).val();
        if (password.length<6 || password.length==0){
            $('.content .int3').show().html('密码长度小于6位')
        }else {
            $('.content .int3').hide();
        }
    });
	$('#password').focus(function () {
        $('.content .int3').hide()
    });
    // 匹配二次密码
    $('#mypassword').blur(function () {
        console.log(456);
        var mypassword = $(this).val();
        var password = $('#password').val();
        if (mypassword<6 || mypassword != password){
            $('.content .int4').show().html('与第一次密码输入不匹配')
        }
        else {
            $('.content .int4').hide()
        }
    });
    $('#mypassword').focus(function () {
        $('.content .int4').hide()
    })

    // 匹配邮箱
    var emails = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/;
    $('#email').blur(function () {
        console.log(789);
        var email= $(this).val();
        var fay = emails.test(email);
        if (fay){
            $('.content .int5').hide()
        }else {
            $('.content .int5').show().html('邮箱格式有误')
        }
    })
    $('#email').focus(function () {
        $('.content .int5').hide()
    })
});