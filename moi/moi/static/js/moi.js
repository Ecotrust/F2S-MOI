(function($) {

/** fullscreen scroll **/
$('.body-content').fullpage({
    navigation: true,
    navigation: 'right',
    scrollBar: true,
    css3: true,
    scrollingSpeed: 1200,
    fixedElements: '#header',
});

$(document).on('click', '#moveDown', function() {
    $.fn.fullpage.moveSectionDown();
});


/** search toggle **/
var $searchIcon = $('.fa-search');
var $searchField = $('.search-nav');
var $searchForm = $('.search-form');
var $mainNav = $('.main-nav');
var $mobileNav = $('button.navbar-toggle');
var $searchItem = $('li.search');

$searchIcon.on('click', function() {
    $mainNav.toggleClass('no-view');
    $searchField.toggleClass('nav-view');
    $searchForm.focus();
});

// reshow menu on blur out
$searchForm.focusout(function() {
    $searchField.toggleClass('nav-view');
    $mainNav.toggleClass('no-view');
});

//mobile menu
// $mobileNav.on('click', function() {
//     $searchItem.toggleClass('nav-view');
//     $searchField.toggleClass('nav-view');
// });

/** countUp.js **/

    var $countNum = $('.count-up');

    //check if countUp element exits on page
    if ($countNum.length) {
        var options = {
            useEasing : false,
            useGrouping : true,
            separator : ',',
            decimal : '.',
            prefix : '',
            suffix : ''
        };

        var countUpArray = [];
        //add countUp functionality to each element
        $countNum.each(function(index, element) {
            var id = this.id;
            var number = id.match(/\d+/)[0];
            var count = new CountUp(id, 0, number, 0, 2.75, options);
            countUpArray.push(count);
        });

        //count-up if in view on load
        fireCountWhenInView();
    }

    //check scroll event and count-up
    $(window).scroll(function() {
        fireCountWhenInView()
    })

    function fireCountWhenInView() {
        $countNum.isInViewport()
            .each(function(index, elm) {
                $.each(countUpArray, function(index, val) {
                    if (elm === val.d) {
                        val.start();
                    }
                })
            })
    }

})(jQuery);
