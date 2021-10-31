
// import hello from "static/js/index.js"

$(function(){
   $(".bt_pages").click(function(e){
      let current_page_id = $("tr.main_content").attr("id");
      let url = '/apps/ajax_app/index/';
      let csrf_token = document.cookie.split("=")[1];
      let data = {
         "current_page_id": current_page_id,
      };
      debugger;
      $.ajax({
         type: "POST",
         headers: {
            "X-CSRFToken": csrf_token
         },
         cache: false,
         url: url,
         data: JSON.stringify(data),
         dataType: "html",
      }).done(function(response){
         $(".main_content").empty();
         $(".tb_content").append(response);
      }).fail(function(response){
         console.log(response);
      });
   });
});