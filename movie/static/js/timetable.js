$(document).ready(function() {

    $(".timeselect").click(function() {
        var s = $(this).attr('value');
        // $(".timerender").text(s);
        $(".summit").val(s);
    });

});