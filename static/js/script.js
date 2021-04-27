/*----- Materialize CSS JQuery Helpers -----*/
$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $(".tooltipped").tooltip();
    $("select").formSelect();
    $(".parallax").parallax();
    // $('.dropdown-trigger').dropdown();
    // $(".fixed-action-btn").floatingActionButton();
    // $(".modal").modal();
});


/* --- URL IMAGES --- */

/* --- For Add Recipe --- */
// Reference  https://stackoverflow.com/questions/31398473/load-image-in-div-from-url-obtained-from-a-text-box/31398762
function addImage() {
    var url = document.getElementById("url_img").value;
    var image = new Image();
    image.src = url;
    document.getElementById("image-container").appendChild(image);
}


  // Or with jQuery

  $(document).ready(function(){
    $('.modal').modal();
    $('#modal1').modal('open'); 
  });