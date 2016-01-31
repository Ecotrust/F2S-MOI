(function($) {
/** search toggle **/
$('.fa-search').on('click', function() {
    $('.main-nav').fadeToggle(200);
    $('.search-nav').fadeToggle(600);
    $('.search-form').focus();
});

$('.search-form').focusout(function() {
    $('.search-nav').fadeToggle(200);
    $('.main-nav').fadeToggle(400);
});

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
