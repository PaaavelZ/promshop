/*Navigation drop*/
$('ul.nav li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});

/*Burger menu */
function menu(x) {
	x.classList.toggle('anim');
}

/*Slider first*/
$('.slider-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  infinite: false,
  adaptiveHeight: true
});

$('.slider-nav').slick({
  centerMode: true,
  slidesToShow: 4,
  asNavFor: '.slider-for',
  vertical: true,
  dots: false,
  focusOnSelect: true,
  arrows: false,
});


/*Slider second*/
$('.slider-description-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  infinite: true,
  focusOnSelect: true,
});
$('a[data-slide]').click(function(e) {
  e.preventDefault();
  var slideno = $(this).data('slide');
  $('.slider-description-for').slick('slickGoTo', slideno - 1);
});
