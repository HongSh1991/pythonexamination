$(function() {  
            loadMenu(function (id){  
                window.location= '/index.php/index/baoku' + '/id/' + id + '.html';  
            });  
            $('li[aid=]').css('background',"#F5F5F5");  
  
  
        });  
  
  
    /*传入一个函数参数为 id 即li上的属性 aid*/  
    function loadMenu (fun_clickAction) {  
        /*事件回调函数*/  
        clickAction = fun_clickAction;  
        /*一级菜单的样式*/  
        $(".lmenu > ul > li > span").prepend('<em class="icoclose"></em>');  
        /*二级菜单的样式*/  
        $(".lmenu > ul > li > ul > li").each(function(){  
            /*检查是否有节点*/  
            span = $(this).find("span");   
            if ( span.length ){  
                //有节点的话  
                span.prepend('<em class="icoclose2"></em>');  
            }else{  
                //无节点的话,绑定事件  
                $(this).prepend('<em class="iconleaf"></em>')  
                       .click(function(){  
                            clickAction($(this).attr('aid'));  
                       });  
            }  
        });  
        /*三级菜单的样式*/  
        $(".lmenu > ul > li > ul > li > ul > li")  
            .prepend('<em class="iconleaf2"></em>')  
            .click(function(){  
                clickAction($(this).attr('aid'));  
            });  
  
        $(".lmenu ul li span").click(function(){  
            var ye = $(this).find('em');  
            classNama = ye.attr("class");  
            if( classNama == 'icoclose'){ye.attr('class','icoopen');}  
            else if( classNama == 'icoopen' ){ye.attr('class','icoclose');}  
            else if( classNama == 'icoclose2'){ye.attr('class','icoopen2');}  
            else if( classNama == 'icoopen2' ){ye.attr('class','icoclose2');}  
            $(this).siblings("ul").slideToggle("normal","swing");  
        });  
    }