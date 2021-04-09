

function home(url,datashow){


    $.ajax({
                    url : url,
                    type: "GET",
        data : {hide : "show"},
                    success : function (e){
                        datashow(e);
                    }

    });




}
function headtag(url ,data ,show){
    $.ajax({
        url : urls,
        type: "GET",
        data : data,
        success : function (e){
            show(e)
        }
    })
}
function getdata(id,data,sodata){


    $.ajax({
        url : "/mobile/"
    })
}






