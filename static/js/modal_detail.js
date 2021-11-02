$(function () {
    // function click show modal detail
    $(document).on("click", "#tb_images", function(){
        $(".modal_detail").css("visibility", "visible").focus();
        $("body").css("overflow-y", "hidden");
        let pad_top = parseInt($("html").height()) * 0.08 + $(window).scrollTop();
        $(".modal").css({"padding-top": `${pad_top.toString()}px`, "padding-left": "30%"});
        $(".modal_detail").css("height", `${$("html").height()}px`);

        // transmit data into modal detail
        let data_html = ""
        for( let index = 0; index < $(".pr-2").length; index++){
            data_html+=`
                <tr><td>${$(".pr-2")[index].textContent}</td></tr>
            `
        }
        $(".tb_modal_content").empty().append(data_html);
    });

    // function hidden modal detail
    $("span.close").click(function () {
        $(".modal_detail").css("visibility", "hidden");
        $("body").css("overflow-y", "scroll");
    });
});