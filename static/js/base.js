
// import hello from "static/js/index.js"

$(function(){
   // paginator page
   $(".bt_pages").click(function(e){
      let id_next_or_pre = $("tr.main_content").attr("id");
      let bt = $(this).attr("id");
      if (bt === "previous"){
         id_next_or_pre = parseInt(id_next_or_pre) - 1;
      }else if (bt === "next"){
         id_next_or_pre = parseInt(id_next_or_pre) + 1;
      }else{
         id_next_or_pre = parseInt(bt);
      }
      let url = '/apps/ajax_app/index/';
      let csrf_token = document.cookie.split("=")[1];
      let data = {
         "id_next_or_pre": id_next_or_pre,
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
         $(".main_content").remove();
         $(".tb_content").append(response);
      }).fail(function(response){
         console.log(response);
      });
   });
});