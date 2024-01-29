window.addEventListener('DOMContentLoaded', event => {
    $('html').click(function (e) {
        var elem = e.target;
        if ($(elem).parent().attr('id') == "search-icon") {
            $('#search-bar').removeClass('d-none');
            $('#search-icon').addClass('d-none');
        } else if ($(elem).parent().parent().parent().attr('id') == "search-bar") {
        } else {
            $('#search-bar').addClass('d-none');
            $('#search-icon').removeClass('d-none');
        }
    });
    // Remove the * in sign up page
    $(".asteriskField").remove();
    $("#hint_id_password1").remove();
    $("#logout-link").on('click', function() {
        $('#sign-out-link').click();
        console.log("asdhuasd");
    });

    $(".overlay").mouseover(function() {
        $(this).css('opacity', '1'); 
     });
  
     $(".overlay").mouseleave(function() {
        $(this).css('opacity', '0'); 
     });

    // Code to change the attributes depending on screen
//     $(window).on('resize', function(){
//         var win = $(this);
//         if (win.width() < 950) {
//             $(".login-section").removeClass("login-section");
//         }
//     });
//     if($(window).width() < 950) {
//         $(".login-section").removeClass("login-section");
//    } 
    });
