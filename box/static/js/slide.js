$(document).ready(function () {
	setInterval("switchSlide()", 9000);
	$('.slideshow img:gt(0)').hide();
});

function switchSlide() {
	$('.slideshow img:first').fadeOut(2000).next().show().end().appendTo('.slideshow');
}
