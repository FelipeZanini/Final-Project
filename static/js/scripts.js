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
    $("#logout-link").on('click', function () {
        $('#sign-out-link').click();
        console.log("asdhuasd");
    });

    $(".overlay").mouseover(function () {
        $(this).css('opacity', '1');
    });

    $(".overlay").mouseleave(function () {
        $(this).css('opacity', '0');
    });

    // Cookie Script
    var addBttns = document.getElementsByClassName('addBttns')

    for (i = 0; i < addBttns.length; i++) {
        addBttns[i].addEventListener('click', function () {
            var productId = this.dataset.product
            var action = this.dataset.action
            console.log('productId:', productId, 'Action:', action)
            console.log('USER:', user)

            if (user == 'AnonymousUser') {
                addCookieItem(productId, action)
            } else {
                updateUserOrder(productId, action)
            }
        })
    }

    function updateUserOrder(productId, action) {
        console.log('User is authenticated, sending data...')

        var url = '/update_item/'

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })
        })
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                location.reload()
            });
    }

    function addCookieItem(productId, action) {
        console.log('User is not authenticated')

        if (action == 'add') {
            if (cart[productId] == undefined) {
                cart[productId] = { 'quantity': 1 }

            } else {
                cart[productId]['quantity'] += 1
            }
        }

        if (action == 'remove') {
            cart[productId]['quantity'] -= 1

            if (cart[productId]['quantity'] <= 0) {
                console.log('Item should be deleted')
                delete cart[productId];
            }
        }
        console.log('CART:', cart)
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

        // location.reload()
    }
});
