layui.use(["layer","jquery","element"],function () {
    var layer = layui.layer;
    var $ = layui.jquery;
    var element = layui.element;

    var page = 1;
    var limit = 10;
    var nextPage = true;

    document.title = localStorage.getItem("nickname");

    function contentList(page,limit){
        $.ajax({
            type: "GET",
            url: "/admin/contentList",
            data: {"page":page,"limit":limit},
            success: function(res){
                let contentList = $("#content-list");
                if(res.code === 0){
                    for(i=0;i<res.data.length;i++){
                        html = '<div style="background-color: #B2DFEE;padding: 20px" onclick="window.open(\'/admin/contentDetail?contentId='+res.data[i].id+'\')">' +

                        '<fieldset class="layui-elem-field layui-field-title" style="margin-top: 30px;">'+
                            '      <legend>'+res.data[i].title+'</legend></fieldset>' +
                        '      <div class="layui-card-body">' +res.data[i].des+
                        '      </div>' +'<div style="opacity: 0.5">创建日期：'+ res.data[i].create_time +'</div><br>'+
                            '<img src="'+res.data[i].avatar+'" class="layui-nav-img" />'+ '<div class="layui-inline" style="opacity: 0.5">' + res.data[i].author_name +'</div>'+
                        '    </div><br>';
                        contentList.append(html);
                        element.render();
                    }
                }else{
                    contentList.append('无更多数据！');
                    nextPage = false;
                }
            },
            error:function () {
                                layer.alert('操作失败，网络故障!', {icon: 5});
                            }
        });
    }

    contentList(page,limit);


    function getScrollTop() {
        var scrollTop = 0;
        if(document.documentElement && document.documentElement.scrollTop) {
            scrollTop = document.documentElement.scrollTop;
        } else if(document.body) {
            scrollTop = document.body.scrollTop;
        }
        return scrollTop;
    }

    //获取当前可视范围的高度
    function getClientHeight() {
        var clientHeight = 0;
        if(document.body.clientHeight && document.documentElement.clientHeight) {
            clientHeight = Math.min(document.body.clientHeight, document.documentElement.clientHeight);
        } else {
            clientHeight = Math.max(document.body.clientHeight, document.documentElement.clientHeight);
        }
        return clientHeight;
    }

    //获取文档完整的高度
    function getScrollHeight() {
        return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
    }


    window.onscroll = function() {
        if(getScrollTop() + getClientHeight() === getScrollHeight() && nextPage === true) {
            page++;
            contentList(page,limit);
        }
    };

});