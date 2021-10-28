
// import hello from "static/js/index.js"

$(function(){
   $(".li_test").css("display", "none");
   $(".bt_pages").click(function(e){
      $(".li_test").css("display", "list-item");
      // let page_id = $(this).attr("id");
      let current_page_id = document.URL.split("?page=")[1];
      let url = '/apps/ajax_app/index/';
      // let csrfTokenElement = document.querySelector("input[name=csrfmiddlewaretoken]");
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
         url: `${url}`,
         data: JSON.stringify(data),
         success: function(response){
            console.log("okeeeeeeeeeeeee")
            alert(`page id: ${page_id}`);
         },
         error: function(response){
            console.log(response);
         }
      })
   });
});