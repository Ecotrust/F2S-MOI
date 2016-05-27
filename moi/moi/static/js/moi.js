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
    paddingTop: '95px',
    anchors: ['sec1', 'sec2', 'sec3', 'sec4', 'sec5', 'sec6', 'sec7']
});

function scrollArrow (pos) {
    $('html, body').animate({
       scrollTop: $(pos).offset().top - 60
    }, 1050);
}

$(document).on('click', '.moveDown', function() {
    if ($(this).hasClass('white-arrow')) {
        var pos = '.sec-2';
        scrollArrow(pos)
    } else {
        var pos = '.sec-3';
        scrollArrow(pos)
    }
});



// add anchors
var sectorArrays = ['health', 'education', 'economy', 'environment'];
sectorArrays.forEach(function(i) {
    var topStory = '.top-story.' + i;
    var anchorValue = "#" + $(topStory).closest('section').attr('data-anchor');
    var circleSector = ".circle-" + i;
    $('.four-circle').find(circleSector).attr('href', anchorValue);
})

/** switch image **/
function rotate() {
    var imgArray = [],
        elm,
        $templateAbout = $('.template-about'),
        $ecoTopStory = $('.top-story.economy'),
        $healthTopStory = $('.top-story.health');

    function changeImg(elm) {
        $(elm).each(function(index, elm) {
            var $imgSrc = $(this).attr('src');

            if ($imgSrc === imgArray[0] || $imgSrc === imgArray[1]) {
                if (window.outerWidth < 768) {
                    var src = $(this).attr('src').replace($imgSrc, imgArray[3]);
                    $(this).attr('src', src).css({ 'max-width': '190px', 'min-width': '155px'});
                }
            } else if ($imgSrc === imgArray[3] || $imgSrc === imgArray[4]) {
                if (window.outerWidth >= 768) {
                    var src = $(this).attr('src').replace($imgSrc, imgArray[0]);
                    $(this).attr('src', src).css({'max-width': '100%', 'min-width': '375px'});
                }
            }
        })
    }

    if ($templateAbout.length) {
        elm = $templateAbout.find('img.img-responsive');
        imgArray = [
            '/media/images/about_evaluation_framework.original.png',
            '/media/original_images/about_evaluation_framework2x.png',
            '/media/original_images/about_evaluation_framework_vertical.png',
            '/media/original_images/about_evaluation_framework_vertical2x.png'
        ]

        changeImg(elm);
    } else {
        if ($ecoTopStory.length) {
            elm = $ecoTopStory.find('img.img-responsive');
            imgArray = [
                '/media/images/econ_full.original.png',
                '/media/original_images/econ_full2x.png',
                '/media/original_images/econ_full_vert.png',
                '/media/original_images/econ_full_vert2x.png'
            ]

            changeImg(elm);
        } if ($healthTopStory.length) {
            elm = $healthTopStory.find('img.img-responsive');
            imgArray = [
                '/media/images/health_full_horizontal.original.png',
                '/media/original_images/health_full_horizontal2x.png',
                '/media/original_images/health_full_vert.png',
                '/media/original_images/health_full_vert2x.png'
            ]

            changeImg(elm);
        }
    }
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
           if (sourcePath.indexOf('2x') > -1) {
            var retinaPath = sourcePath;
           } else {
            var retinaPath = sourcePath.slice(0, -4) + '2x.png';
           }
           $(this).attr('data-at2x', retinaPath);
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
if ($('.economic-calculator').length) {
    var $num = $('input#inputCalc')[0]
    $('.keys span').on('click', function() {
        if (this.id === 'del' && $num.value.length > 0) {
            $num.value = $num.value.slice(0, -1);
            if ($num.value === '') {
                calcResult.value = '';
            }
        } else {
            var intVal = parseInt(this.id)
            $num.value = $num.value + intVal;
        }

        if ($num.value.length > 0 && $num.value !== "0") {
            $num.oninput();
        }

    });


    $num.oninput = function() {
        var inputField = $num.value;
        var resultField = inputField * 2;
        if (inputField === '') {
          calcResult.value = '';
        } else {
          calcResult.value = '$' + numberWithCommas(resultField);
        }
        $('#calcResult, #calcResult-text').removeClass('animated bounceInUp');
    }


    function numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    $('.calculate-btn').click(function() {
        if (calcResult.hasOwnProperty('value') && (calcResult.value !== '' || calcResult.value.length > 0 )) {
            $('#calcResult').html('<span id="equal-sign">=</span><span id="result-val">   '+calcResult.value+'</span>');
            $('#calcResult, #calcResult-text').show()
                            .addClass('animated bounceInUp');
        }
    })
}


/** source toggle **/
$('.ts-source span').click(function() {
    $(this).siblings('.ts-source-full').toggleClass('table');
});

$('.data-attr > .source').click(function() {
    $(this).parent().prev().toggleClass('inline-block')
});

/** search toggle **/
// var $searchIcon = $('.fa-search');
// var $searchField = $('.search-nav');
// var $searchForm = $('.search-form');
var $mainNav = $('.main-nav.dropdown');
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

// $searchIcon.on('click', function() {
//     $mainNav.toggleClass('no-view');
//     $searchField.toggleClass('nav-view');
//     $searchForm.focusWithoutScrolling();
// });

// reshow menu on blur out
// $searchForm.focusout(function() {
//     if ($('.navbar-collapse.collapse.in').length) {
//         setTimeout(function() {
//             $mobileNav.click();
//         }, 50);
//     } else {
//         $searchField.toggleClass('nav-view');
//         $mainNav.toggleClass('no-view');
//     }

// });

//mobile menu
$mobileNav.on('click', function() {
    setTimeout(function(){
        $mainNav.find('a.dropdown-toggle').click();
        if ($mainNav.hasClass('open')) {
            $('button.navbar-toggle').find('i.fa').toggle();
        }
    }, 200);
});

/** about page are external links **/
if ($('.template-about').length) {
    $('a').filter('[href^="http://"],[href^="https://"]')
          .attr('target', '_blank');
}


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
        } else if (number.toString().length == 6 && number > 102500 || number <= 250000) {
            start = 100000;
        } else if (number.toString().length == 6 && number > 250000) {
            start = number - 150000;
        } else if (number.toString().length == 7) {
            start = number - number/3;
        } else {
            start = number - number/4;
        }

        var count = new CountUp(id, start, number, 0, 1.25, options);
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
                    setTimeout(function() {
                        val.start();
                    }, 500);
                }
            })
        })
}


/** jquery overrides **/
var $basicContentImg = $('.rich-text > p > img');
if ($basicContentImg.length > 0) {
    $basicContentImg.parent().addClass('row no-text-row');
    var $multiImgParent = $('.no-text-row');
    $multiImgParent.each(function() {
        var $multiImg = $(this).find('.multi');
        if ($multiImg.length == 2) {
            $multiImg.addClass('col-md-6 col-sm-6 col-xs-6')
        } else if ($multiImg.length == 3) {
            $multiImg.addClass('col-md-4 col-sm-4')
        } else if ($multiImg.length == 4) {
            $multiImg.addClass('col-md-3 col-sm-3')
        }
    });
}

})(jQuery);
