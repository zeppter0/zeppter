

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

function toggleFullScreen(element) {
  if (!element.fullscreenElement &&    // alternative standard method
      !element.mozFullScreenElement && !element.webkitFullscreenElement && !element.msFullscreenElement ) {  // current working methods
    if (element.requestFullscreen) {
      element.requestFullscreen();
    } else if (element.msRequestFullscreen) {
      element.msRequestFullscreen();
    } else if (element.mozRequestFullScreen) {
      element.mozRequestFullScreen();
    } else if (element.webkitRequestFullscreen) {
      element.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
    }
  } else {
    if (element.exitFullscreen) {
      element.exitFullscreen();
    } else if (element.msExitFullscreen) {
      element.msExitFullscreen();
    } else if (element.mozCancelFullScreen) {
      element.mozCancelFullScreen();
    } else if (element.webkitExitFullscreen) {
      element.webkitExitFullscreen();
    }
  }
}




