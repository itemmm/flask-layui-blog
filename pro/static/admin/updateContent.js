$(function() {
        var editor = editormd({
            id   : "editormd",
            placeholder: "just to do it!",
            height: 700,
            saveHTMLToTextarea : true,
            flowChart : true,
            path : "../../static/editormd/lib/"
        });
    });


layui.use(["jquery","form","layer"],function(){
    var jquery = layui.jquery;
    var form = layui.form;
    var layer = layui.layer;


    form.on("submit(save)",function(data){
        let params = data.field;
        jquery.ajax({
            type: "POST",
            url: "/admin/updateContent",
            data: params,
            success: function(res){
                        layer.alert(res.msg, {icon: 6}, function () {
                            let index = layer.alert();
                            layer.close(index);
                            window.close();
                        })
            },
            error: function () {
                            layer.alert('操作失败，网络故障!', {icon: 5});
                        }
        })
    })
});