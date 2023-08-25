$('.slider-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  asNavFor: '.slider-nav',
  vertical: true,
  infinite: false,
});

$('.slider-nav').slick({
  initialSlide: 0,
  centerMode: true,
  slidesToShow: 4,
  asNavFor: '.slider-for',
  vertical: true,
  dots: false,
  focusOnSelect: true,
  arrows: false,
});



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
