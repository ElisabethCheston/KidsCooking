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

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
});
/*
var instance = M.FormSelect.getInstance(elem);
instance.getSelectedValues();
*/

document.addEventListener("DOMContentLoaded", function () {
  const selects = document.querySelector("select");
  const instances = M.FormSelect.init(selects, {});
  const selectOption = document.querySelector("#multipleselect");
    
  selectOption.addEventListener("change", function () {
    const instance = M.FormSelect.getInstance(selectOption);
    const selectedValues = instance.getSelectedValues();
    console.log(selectedValues);
  });
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

$(document).ready(function () {
    $('.modal').modal();
    $('#modal1').modal('open');
});