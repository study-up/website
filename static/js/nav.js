$(init)

function init(){
    $("#nav ul li").mouseenter(naventer)
    $("#nav ul li").mouseleave(navleav)
}

function naventer(){
    if($(this).css("background")!="rgb(204, 204, 204) none repeat scroll 0% 0% / auto padding-box border-box"){
        $(this).css("background","#226039 ");
    }
}

function navleav(){
    if($(this).css("background")!="#ccc"){
        $(this).css("background","");
    }
}