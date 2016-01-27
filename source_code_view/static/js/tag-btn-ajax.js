var myHilitor;
$(document).ready(function() {
  myHilitor = new Hilitor("sourceCode");
  $("body").on('click', '.tag-btn', function(e) {
    tagId = $(this).attr("id");
    myHilitor.remove();
    myHilitor.apply(tagId);
  });
});
