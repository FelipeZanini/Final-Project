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
    });
