

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



       var hisshow = 1


    var arry_history = []


class zhistory{

    sethistory(){




        if(!arry_history.includes(location.pathname)){
            arry_history.unshift(location.pathname)
            console.log(arry_history)



        }
    }
    gethistory(hish){
        if (arry_history.length>=hisshow) {
            var urls = arry_history[hisshow]
            if (urls === "/" || urls === ""){
                urls="/mobileload"
            }

            home(urls, function (e) {
                hisshow++
                hish(e)
                console.log(hisshow)
            })
        }else {
            hisshow = arry_history.length
        }

    }
    check_history(){
        if (!arry_history.includes(location.pathname)){
            var dat = []
           var i = hisshow -2;

          /*  while (i<hisshow){
                arry_history.splice(i,1)
            }*/

            if (hisshow !== 0) {
                while (i<arry_history.length){
                    dat.unshift(arry_history[i]);
                    i++;
                }
                arry_history = []
                arry_history = dat


                hisshow = 1
                console.log(arry_history.length)
            }



        }
    }


}

    zhis = new zhistory()




   function delele_comment(elem){
                $.ajax({
           url: "/comment/delete",
           type: "post",
           data: {divce: "mobile", id: $(elem).data("id"), userid: $(elem).data('userid'),csrfmiddlewaretoken:$(elem).data('csrf'),},
           success: function (data) {
               data = JSON.parse(data)
               if (data.response === "success") {
                   $("#" + data.id).remove()

               }
                                  console.log(data)

           }

       })

   }


   function hrefs(vid){
    window.location.href = '/mobile/content/'+vid+'/'
   }







