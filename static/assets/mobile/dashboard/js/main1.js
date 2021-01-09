

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


