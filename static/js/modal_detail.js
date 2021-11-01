$(function () {
    // function click show modal detail
    $(".tb_images").click(function () {
        $(".modal_detail").css("visibility", "visible");
        $("body").css("overflow-y", "hidden");
    });

    // function hidden modal detail
    $("span.close").click(function () {
        $(".modal_detail").css("visibility", "hidden");
        $("body").css("overflow-y", "scroll");
    });
});