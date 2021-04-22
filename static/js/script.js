/*----- Materialize CSS JQuery Helpers -----*/
$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $(".tooltipped").tooltip();
    $("select").formSelect();
    // $('select').material_select();
    $(".parallax").parallax();
    $('.dropdown-trigger').dropdown();
    // $(".fixed-action-btn").floatingActionButton();
    // $(".modal").modal();
});


/*----- Display url image ----- 
----------- on AddRecipe Pages----------
Adapted from https://stackoverflow.com/questions/31398473/
load-image-in-div-from-url-obtained-from-a-text-box/31398762*/
function addImage() {
    var url = document.getElementById("url_img").value;
    var image = new Image();
    image.src = url;
    document.getElementById("image-container").appendChild(image);
}

