
// import hello from "static/js/index.js"

$(function(){

   $("#bt_next").click(function(e){
      let url = `/apps/ajax_app/index/${$(this).attr("href")}`;
      let data = {
         "key": "value",
      };
      // debugger;
      $.ajax({
         type: "POST",
         url: url,
         data: JSON.stringify(data),
         success: function(response){
            console.log("move page");
         },
         error: function(response){
            console.log(response);
         }
      })
   });
});