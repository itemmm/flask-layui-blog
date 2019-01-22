layui.use(["jquery","layer"],function () {
    var $ = layui.jquery;
    var layer = layui.layer;

    $("#addCategory").click(function(){
        layer.open({
           type: 2,
           title: "添加分类",
           shadeClose: true,
           area: ["600px","400px"],
           content: "/user/addCategory",
           end: function(){
               location.reload();
           }
        });
    });
});