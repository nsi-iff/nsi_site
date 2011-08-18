/*
*	Code to display coderwall.com badges 
*/

$(document).ready(function(){
        var member = $('#github_user').text();
        var coderwallJSONurl ="http://www.coderwall.com/" + member + ".json?callback=?";
        var height = 75;
        var width = 75;

        $.getJSON(coderwallJSONurl, function(data) {
        $("<a href='http://coderwall.com/" + member + "' id='coderwall_link'>Coderwall Achievements</a> <br /><br />").appendTo("#coderwall");
          $.each(data.data.badges, function(i, item) {
            $("<img/>").attr("src", item.badge)
              .attr("float", "left")
              .attr("title", item.name + ": " + item.description)
              .attr("alt", item.name)
              .attr("height", height)
              .attr("width", width)
              .appendTo("#coderwall")
              .hover(
                  function(){
                      $(this).css("opacity","0.6");
                  },
                  function(){
                      $(this).css("opacity","1.0");
                  }
              )
            });
        });
});
