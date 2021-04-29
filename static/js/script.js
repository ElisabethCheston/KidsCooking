/*----- Materialize CSS JQuery Helpers -----*/
$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $(".tooltipped").tooltip();
    $("select").formSelect();
    $(".parallax").parallax();
    $(".modal").modal();
    //$('#multipleselect').append({"Oven", "Stove", "Knife", "Microwave", "Mixer"})
    $('#multipleselect').formSelect()
});

/* --- Reference: https://stackoverflow.com/questions/44001532/select-all-option-in-materialize-multi-select.--- */
/*
var activateOption = function(collection, newOption) {
    if (newOption) {
        collection.find('li.selected').removeClass('selected');

        var option = $(newOption);
        option.addClass('selected');
    }
};

$(document).ready(function() {
    $('select').material_select();
    $('.test-input > .select-wrapper > .select-dropdown').prepend('<li class="toggle selectall"><span><label></label>Select all</span></li>');
    $('.test-input > .select-wrapper > .select-dropdown').prepend('<li style="display:none" class="toggle selectnone"><span><label></label>Select none</span></li>');
    $('.test-input > .select-wrapper > .select-dropdown .selectall').on('click', function() {
        selectAll();
        $('.test-input > .select-wrapper > .select-dropdown .toggle').toggle();
    });
    $('.test-input > .select-wrapper > .select-dropdown .selectnone').on('click', function() {
        selectNone();
        $('.test-input > .select-wrapper > .select-dropdown .toggle').toggle();
    });
});

function selectNone() {
    $('select option:selected').not(':disabled').prop('selected', false);
    $('.dropdown-content.multiple-select-dropdown input[type="checkbox"]:checked').not(':disabled').prop('checked', '');
    //$('.dropdown-content.multiple-select-dropdown input[type="checkbox"]:checked').not(':disabled').trigger('click');
    var values = $('.dropdown-content.multiple-select-dropdown input[type="checkbox"]:disabled').parent().text();
    $('input.select-dropdown').val(values);
    console.log($('select').val());
};

function selectAll() {
    $('select option:not(:disabled)').not(':selected').prop('selected', true);
    $('.dropdown-content.multiple-select-dropdown input[type="checkbox"]:not(:checked)').not(':disabled').prop('checked', 'checked');
    //$('.dropdown-content.multiple-select-dropdown input[type="checkbox"]:not(:checked)').not(':disabled').trigger('click');
    var values = $('.dropdown-content.multiple-select-dropdown input[type="checkbox"]:checked').not(':disabled').parent().map(function() {
        return $(this).text();
    }).get();
    $('input.select-dropdown').val(values.join(', '));
    console.log($('select').val());
};
*/

/* --- Email Fuction --- */

function sendMail(contactform) {
    emailjs.send({
        "first_name": contactform.name.value,
        "last_name": contactform.name.value,
        "from_email": contactform.emailaddress.value,
        "message": contactform.message.value
    })
        .then(
            function (response) {
                var left_position = $("body").width()/2 - $("#popup").width()/2;
           $("#gray-panel").fadeIn("slow");
           $("#popup").css("left", left_position).fadeIn("slow");

                console.log("SUCCESS", response);
                contactform.reset(); // To clear the page
            },
            function (error) {
                console.log("FAILED", error);
                alert("Sorry, Please try again", error);
            }
        );
    return false;  // To block from loading a new page   
}


/* --- URL IMAGES --- */

/* --- For Add Recipe --- */
// Reference  https://stackoverflow.com/questions/31398473/load-image-in-div-from-url-obtained-from-a-text-box/31398762
function addImage() {
    var url = document.getElementById("url_img").value;
    var image = new Image();
    image.src = url;
    document.getElementById("image-container").appendChild(image);
}

