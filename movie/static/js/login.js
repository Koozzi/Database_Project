/*TAKEN FROM https://dribbble.s3.amazonaws.com/users/85793/screenshots/1294312/signin_1x.png*/

//just a bit of fun and practice

$(".username").on("input", function() {
  if ($(this).val().length > 0)
  {
    $('.username-icon').addClass('color');
    $(this).closest('.input').addClass('border-color');
  }
  else
  {
    $('.username-icon').removeClass('color');
    $(this).closest('.input').removeClass('border-color');
  }
});

$(".password").on("input", function() {
  if ($(this).val().length > 0)
  {
    $('.password-icon').addClass('color');
    $(this).closest('.input').addClass('border-color');
  }
  else
  {
    $('.password-icon').removeClass('color');
    $(this).closest('.input').removeClass('border-color');
  }
});
