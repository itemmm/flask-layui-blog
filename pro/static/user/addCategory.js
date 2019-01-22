layui.use(["form","jquery"],function(){
   var form = layui.form;
   var $ = layui.jquery;

   form.on("submit(save)",function(data){
       let params = data.field;
       $.ajax({
           type:"POST",
           url:"/user/addCategory",
           data:params,
           success:function(res){
               if(res.code===0){
                   layer.alert('操作成功', {icon: 6}, function () {
                        let index = parent.layer.getFrameIndex(window.name); //获取窗口索引
                        parent.layer.close(index);
                });
               }else{
                   layer.alert(data.msg, {icon: 5});
               }
           },
           error:function(){
               layer.alert('操作失败，网络故障!',{icon:5});
           }
       })
   })
});