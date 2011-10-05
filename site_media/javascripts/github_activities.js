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
  xunda = feed;
  if (feed.entries.length > 0) {
    $('div.github_activities span.text_highlight').show();
    var div_activities = $('ul.activities');
    $(feed.entries).each(function(key, entry){
      var author = entry.author;
      var title = entry.title;
      var link = entry.link;
      var content = entry.contentSnippet;
      //remove author from start of entry title
      var author_regexp = new RegExp("^" + author + " ");
      title = title.replace(author_regexp, '');
      //convert special chars and remove unnecessary "   ..." from content
      var description = $('<a />').html(content).text().trim().replace(new RegExp("[\n ]+...$"),'')

      var li_entry = $('<li />').text(title)
      var div_entry = $('<a />').append(li_entry)
      div_entry.attr('href', link);
      div_entry.attr('target', '_blank');
      div_entry.attr('title', description);
      div_activities.append(div_entry);
    });
  }
}

$(document).ready(function(){
  var github_feed = $('span#github_feed').text();
  parseRSS(github_feed, placeActivities);
});

