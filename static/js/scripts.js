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
    var updateBttns = document.getElementsByClassName('updateBttns')

    for (i = 0; i < updateBttns.length; i++) {
        updateBttns[i].addEventListener('click', function () {
            var productId = this.dataset.product
            var action = this.dataset.action
            console.log('productId:', productId, 'Action:', action)
            console.log('USER:', user)
            
            if (action == 'addWishlist') {
                addWishlist(productId, action)
            }
            if (action == 'removeWishlist') {
                removeWishlist(productId, action)
            }
            if (action == 'add') {
                addCookieItem(productId, action)
            } else {
                updateCookieItem(productId, action)
            }
        })
    }

    function addCookieItem(productId, action) {
        if (action == 'add') {
            if (cart[productId] == undefined) {
                cart[productId] = { 'quantity': 1 }

            } else {
                cart[productId]['quantity'] += 1
            }
        }
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    }

    function updateCookieItem(productId, action) {

        if (action == 'delete') {
            delete cart[productId];
        }

        if (action == 'increase') {
            cart[productId]['quantity'] += 1
        }

        if (action == 'degrease') {
            cart[productId]['quantity'] -= 1

            if (cart[productId]['quantity'] <= 0) {
                delete cart[productId];
            }
        }
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    }

    function addWishlist(productId, action) {
        if (action == 'addWishlist') {
            if (wishlist[productId] == undefined) {
                wishlist[productId] =  productId 

            } 
        }
        document.cookie = 'wishlist=' + JSON.stringify(wishlist) + ";domain=;path=/"
    }
    function removeWishlist(productId, action) {
        if (action == 'removeWishlist') {
            console.log(wishlist[productId])
            delete wishlist[productId];
        }
        document.cookie = 'wishlist=' + JSON.stringify(wishlist) + ";domain=;path=/"
    }
});
