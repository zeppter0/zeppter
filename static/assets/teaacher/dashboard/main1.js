function auto_ajax(data,url){

    $.ajax({
        url: url,
        type: "post",
        data: data,
        success : function (e){
            return e
        }
    })

}