$(function() {

  $('.input-img a img').click(function(){
    $('.output-img img').attr('src', this.src);
    $('.output').addClass("ui loading basic segment");

    // Clear border in old selection
    $(this).parent().parent().siblings().each(function(){
      $(this).children().removeClass("bordered");
    });

    // Add border to current selection
    $(this).parent().addClass("bordered");

    var args = {
      "image": {
        "url": this.src
      }
    };
  });
});
                          