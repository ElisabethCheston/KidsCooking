// jQuery

$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
    // Dropdow list options for add recipes
    $('select').formSelect();
});

// Contact form
$(document).ready(function () {
    M.updateTextFields();
// Message resize field
    $('#textarea1').val('New Text');
    M.textareaAutoResize($('#textarea1'));
});