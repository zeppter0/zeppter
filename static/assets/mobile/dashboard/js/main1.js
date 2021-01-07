

function home(url,datashow){
    data = "";

    $.ajax({
                    url : url,
                    type: "GET",
                    success : function (e){
                        datashow(e);
                    }

    });




}

