// -- jQuery from Materialized -- //

$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
    // Dropdow list options for add recipes
    $('select').formSelect();
    $('.dropdown-trigger').dropdown();
    // $("select[required]").css({ display: "block", height: 0, padding: 0, width: 0, position: "absolute" });
});

function getSelectedValues() {
    var selectValue = document.getElementById("list").nodeValue;
    console.log(getSelectedValues);
}
// -- Single selections  -- //
/*
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
    instance.getSelectedValues();
});
*/

// -- Multi selections  -- //
/*
document.addEventListener('DOMContentLoaded', function () {
        var elems = document.querySelector('select');
        elems.onchange = selectThem;
        var instances = M.FormSelect.init(elems);
        function selectThem() {
            var selectedOne = instances.getSelectedValues();
            console.log(selectedOne);
        }
    });
    */
// -- Access form data -- //

//validation select option for a dropdown is taken from
//StackOverflow: https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown
$('textarea#recipe_description,input#recipe_name').characterCounter();
$('.tooltipped').tooltip();
$('.modal').modal();