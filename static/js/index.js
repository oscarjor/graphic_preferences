$(document).ready(function() {

   $(".image").click(function () {
         
    var image_url = $(this).attr("src");
    var category =  $(this).attr("category");
    $("#image_url").val(image_url);
    $("#category").val(category);
    $( "#selection" ).submit();

    });

});