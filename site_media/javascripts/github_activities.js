function parseRSS(url, callback) {
  $.ajax({
    url: document.location.protocol + '//ajax.googleapis.com/ajax/services/feed/load?v=1.0&num=10&callback=?&q=' + encodeURIComponent(url),
    async: true,
    dataType: 'json',
    success: function(data) {
      callback(data.responseData.feed);
    }
  });
}

function placeActivities(feed) {
  $('div.github_activities span.text_highlight').show();
  var div_activities = $('ul.activities');
  $(feed.entries).each(function(key, entry){
    var author = entry.author;
    var title = entry.title;
    var link = entry.link;
    //remove author from start of entry title
    var author_regexp = new RegExp("^" + author + " ");
    title = title.replace(author_regexp, '');
    var div_entry = $('<a />').append($('<li />').text(title))
    div_entry.attr('href', link);
    div_entry.attr('target', '_blank');
    div_activities.append(div_entry);
  });
}

$(document).ready(function(){
  var github_feed = $('span#github_feed').text();
  parseRSS(github_feed, placeActivities);
});

