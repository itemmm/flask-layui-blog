layui.use(["layedit","jquery"],function(){
   var layedit = layui.layedit;
   var $ = layui.jquery;

   var index = layedit.build("comment",{
       tool: ['strong', 'italic', 'underline', 'del', '|',"left","center","right","|","face"]
   });

   $("#save").click(function () {
       let contentId = $("#contentId").val();
       let comment = layedit.getContent(index);
       $.ajax({
           type:"POST",
           url: "/user/addComment",
           data: {"contentId":contentId,"comment":comment},
           success: function(res){
               if(res.code===0){
                   layer.alert(res.msg, {icon: 6}, function () {
                    let index = parent.layer.getFrameIndex(window.name); //获取窗口索引
                    parent.layer.close(index);
                });
               }else{
                   layer.alert(res.msg, {icon: 5});
               }
           },
           error:function(){
               layer.alert('操作失败，网络故障!', {icon: 5});
           }
       })
   })

});