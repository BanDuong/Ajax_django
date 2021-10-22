
// import hello from "static/js/index.js"

$(function(){

   $(".bt_pages").click(function(e){
      let page_id = $(this).attr("id");
      let url = '/apps/ajax_app/index/';
      // $(`#${id_page}`).attr("href",`?${id_page}`);
      let data = {
         "key": "value",
         "id": page_id,
      };
      // debugger;
      $.ajax({
         type: "POST",
         url: `${url}?page=${page_id}`,
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