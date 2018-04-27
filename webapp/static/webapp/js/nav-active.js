// Add your javascript here
$(function() {

  $(".nav.navbar-nav li").on("click", function() {
    $(".nav.navbar-nav li").removeClass("active");
    $(this).addClass("active");
  });

});
