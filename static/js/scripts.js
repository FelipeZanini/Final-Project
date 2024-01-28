window.addEventListener('DOMContentLoaded', event => {
    $('#search-icon').on('click', () => {
        $('#search-bar').removeClass('d-none');
        $('#search-icon').addClass('d-none');
    });
    $('html').click(function (e) {
        var elem = e.target;
        if ($(elem).attr('id') == "search-icon") {
            $('#search-bar').removeClass('d-none');
            $('#search-icon').addClass('d-none');
            console.log(elem);
        } else if ($(elem).parent().parent().parent().attr('id') == "search-bar") {
            console.log("uhdauhda");
        } else {
            $('#search-bar').addClass('d-none');
            $('#search-icon').removeClass('d-none');
            console.log(elem);
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
