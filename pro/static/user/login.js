layui.use(["form","jquery"],function(){
    var form = layui.form;
    var $ = layui.jquery;

    form.on("submit(login)",function(data){
       let params = data.field;
       let userName = params.userName;
       let passWord = hex_md5(params.passWord);
       $.ajax({
           type: "POST",
           url: "/user/login",
           data: {"userName":userName,"passWord":passWord},
           success:function(res){
               if(res.code===0){
                   localStorage.clear();
                   localStorage.setItem("avatar",res.data[0].avatar);
                   localStorage.setItem("nickname",res.data[0].nickname);
                   localStorage.setItem("login_name",res.data[0].login_name);
                   window.location.href='/index';
               }else{
                   layer.alert(res.msg, {icon: 5});
               }
           },
           error:function(){
               layer.alert('操作失败，网络故障!', {icon: 5});
           }
       })
    });

});