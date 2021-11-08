
// import hello from "static/js/index.js"

$(document).ready(function(){
   // paginator page
   let max_pages = $("#next").attr("name");
   $(`#page-range-1`).css("background-color", "#4bf5e5"); // add background-color paging start
   $(document).on("click", ".bt_pages", function(){
   // $(".bt_pages").click(function(e){
      let id_next_or_pre = $("tr.main_content").attr("id").replace("current-page-","");    // get current id page
      $(`#page-range-${id_next_or_pre}`).css("background-color", "");    // remove background-color paging
      let bt = $(this).attr("id").replace("page-range-","");
      if (bt === "previous"){                            // id next or previous page
         id_next_or_pre = parseInt(id_next_or_pre) - 1;
         if(id_next_or_pre < 1){
            id_next_or_pre = 1;
         }
      }else if (bt === "next"){
         id_next_or_pre = parseInt(id_next_or_pre) + 1;
         if(id_next_or_pre > max_pages){
            id_next_or_pre = max_pages;
         }
      }else{
         id_next_or_pre = parseInt(bt);
      }
      let url = '/apps/ajax_app/index/';
      let csrf_token = document.cookie.split("=")[1];
      let data = {
         "id_next_or_pre": id_next_or_pre,
      };
      // debugger;
      $.ajax({
         type: "POST",
         headers: {
            "X-CSRFToken": csrf_token
         },
         // cache: false,
         url: url,
         data: JSON.stringify(data),
         dataType: "html",
      }).done(function(response){
         $(`#page-range-${id_next_or_pre}`).css("background-color", "#4bf5e5"); // add background-color paging
         $(".tb-body").empty().append(response);
      }).fail(function(response){
         console.log(response);
      });
   });
});