$(document).ready(function () {
    // function click show modal detail
    $(document).on("click", "#tb_images", function(){
        $(".modal_detail").css("visibility", "visible").focus();
        $("body").css("overflow-y", "hidden");
        let pad_top = parseInt($("html").height()) * 0.08 + $(window).scrollTop();
        $(".modal").css({"padding-top": `${pad_top.toString()}px`, "padding-left": "30%"});
        $(".modal_detail").css("height", `${$("html").height()}px`);

        // transmit data into modal detail
        let data_html = "";
        let img_class = $(this).attr("class");
        console.log(img_class);
        const arr_content = $(`.${img_class}`);
        console.log(arr_content[0]);
        for(let index = 0; index < arr_content.length; index++){
             data_html+=`
                <tr><td>${arr_content[index].textContent}</td></tr>
            `
        }
        $(".tb_modal_content").empty().append(data_html);
    });

    // function hidden modal detail
    $("span.close").click(function () {     // click X to hidden modal
        $(".modal_detail").css("visibility", "hidden");
        $("body").css("overflow-y", "scroll");
    });
    $(document).on('keyup', function(event) {   // press button Esc to hidden modal
       if (event.key == "Escape") {
           $(".modal_detail").css("visibility", "hidden");
           $("body").css("overflow-y", "scroll");
       }
   });
});