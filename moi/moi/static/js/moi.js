(function($) {

/** fullscreen scroll **/
$('.body-content').fullpage({
    navigation: true,
    navigation: 'right',
    scrollBar: true,
    css3: true,
    scrollingSpeed: 1200,
    autoScrolling: false,
    scrollOverflow: false,
    fitToSection: false,
    fixedElements: '#header',
    paddingTop: '65px',
    anchors: ['sec1', 'sec2', 'sec3', 'sec4', 'sec5', 'sec6', 'sec7']
});

$(document).on('click', '#moveDown', function() {
    $.fn.fullpage.moveTo(2);
});

// add anchors
var sectorArrays = ['health', 'education', 'economy', 'environment'];
sectorArrays.forEach(function(i) {
    var topStory = '.top-story.' + i;
    var anchorValue = "#" + $(topStory).closest('section').attr('data-anchor');
    var circleSector = ".circle-" + i;
    $('.four-circle').find(circleSector).attr('href', anchorValue);
})

/** switch evaluation image **/
function rotate() {
    var frameworkImg = '/media/images/about_evaluation_framework.original.png';
    var frameworkImgRet = '/media/original_images/about_evaluation_framework2x.png';
    var frameworkImgVert = '/media/original_images/about_evaluation_framework_vertical.png';
    var frameworkImgVertRet = '/media/original_images/about_evaluation_framework_vertical2x.png';

    $('img.img-responsive').each(function(index, elm) {
        var $imgSrc = $(this).attr('src');

        if ($imgSrc === frameworkImg || $imgSrc === frameworkImgRet) {
            if ($(window).width() < 768) { 
                var src = $(this).attr('src').replace($imgSrc, frameworkImgVert);
                $(this).attr('src', src).css({ 'width': '30%', 'min-width': '155px'});
            } 
        } else if ($imgSrc === frameworkImgVert || $imgSrc === frameworkImgVertRet) {
            if ($(window).width() >= 768) {
                var src = $(this).attr('src').replace($imgSrc, frameworkImg);
                $(this).attr('src', src).css({'width': '45%', 'min-width': '375px'});
            }
        }
    })
}
rotate();
$(window).on('resize', rotate);


/** retina images **/
$('img.img-responsive').each(function(index, elm) {
    var sourcePath = $(this).attr('src');
    if (!$(this).hasClass('no-retina')) {
        if (sourcePath.indexOf('original.png') > -1) {
           var imgSlug = sourcePath.match('/images(.*).original')[1];
           var retinaPath = '/media/original_images' + imgSlug + '2x.png';
           $(this).attr('data-at2x', retinaPath);
        } else if (sourcePath.indexOf('original_images') > -1) {
           var retinaPath = sourcePath.slice(0, -4) + '2x.png';
           $(this).attr('data-at2x', retinaPath);
        } 
        if ($( window ).width() >= 1025) {
           var retina2x = $(this).attr('data-at2x');
           $(this).attr('src', retina2x);
        }
    }
})

/** content taxonomy vertical line **/
if ($('.template-about').length > 0) {
    $('.measures-wrapper').each(function(k) {
        $(this).children().last().children('.vertical-line').hide()
    })
}

/** economic calculator **/
var $num = $('input#inputCalc')[0]
if ($num !== undefined) {
    $num.oninput = function() {
        var inputField = $num.value;
        var resultField = inputField * 2;
        if (inputField === '') {
          calcResult.value = '';
        } else {
          calcResult.value = '$' + numberWithCommas(resultField);
        }
        $('#calcResult').removeClass('animated bounceInLeft');
    }
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

$('.calculate-btn').click(function() {
    $('#calcResult').text(calcResult.value)
                    .show()
                    .addClass('animated bounceInLeft');
})


/** source toggle **/
$('.ts-source').click(function() {
    $(this).children().first().toggleClass('table');
});

$('.data-attr > .source').click(function() {
    $(this).parent().prev().toggleClass('inline-block')
});

/** search toggle **/
var $searchIcon = $('.fa-search');
var $searchField = $('.search-nav');
var $searchForm = $('.search-form');
var $mainNav = $('.main-nav');
var $mobileNav = $('button.navbar-toggle');
var $searchItem = $('li.search');

// ridiculous hack to prevent .focus()
// from scrolling on a fixed nav input field
$.fn.focusWithoutScrolling = function() {
    var x = $(document).scrollLeft();
    var y = $(document).scrollTop();
    this.select();
    setTimeout(function() {
        window.scrollTo(x, y);
    }, 0);
    return this;
}

$searchIcon.on('click', function() {
    $mainNav.toggleClass('no-view');
    $searchField.toggleClass('nav-view');
    $searchForm.focusWithoutScrolling();
});

// reshow menu on blur out
$searchForm.focusout(function() {
    if ($('.navbar-collapse.collapse.in').length) {
        setTimeout(function() {
            $mobileNav.click();
        }, 50);
    } else {
        $searchField.toggleClass('nav-view');
        $mainNav.toggleClass('no-view');
    }

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
        var start;
        var id = this.id;
        var number = parseInt(id.match(/\d+/)[0]);

        // starting from zero can set spans into a funk
        // this helps with easing the starting point - a bit
        if (number > 1 && number < 15) {
            start = 0;
        } else if (number.toString().length == 2 && number > 14 || number <= 110) {
            start = 10;
        } else if (number.toString().length == 3 && number > 110 || number <= 1100) {
            start = 100;
        } else if (number.toString().length == 4 && number > 1100 || number <= 10500) {
            start = 1000;
        } else if (number.toString().length == 5 && number > 10500 || number <= 102500) {
            start = 10000;
        } else {
            start = 100000;
        }

        var count = new CountUp(id, start, number, 0, 3, options);
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


/** jquery overrides **/
var $basicContentImg = $('.rich-text > p > img');
var $multiImg = $('.rich-text > p > img.multi');
if ($basicContentImg.length > 0) {
    $basicContentImg.parent().addClass('row no-text-row');
    if ($multiImg.length >= 2) {
        if ($basicContentImg.length == 2) {
            $multiImg.addClass('col-md-6 col-sm-6 col-xs-6')
        } else if ($multiImg.length == 3) {
            $multiImg.addClass('col-md-4 col-sm-4')
        } else if ($multiImg.length == 4) {
            $multiImg.addClass('col-md-3 col-sm-3 col-xs-6')
        }
    }
}

})(jQuery);
