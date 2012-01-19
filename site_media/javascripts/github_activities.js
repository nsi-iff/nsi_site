// jQuery plugin to show github user's activities
// https://github.com/bernardofire/github-activities

(function($) {
    function parse(feed, container, settings) {
        if (feed.entries.length > 0) {
            $(feed.entries).each(function(key, entry){
                var content = entry.contentSnippet;
                //convert special chars and remove unnecessary "   ..." from content
                var description = $('<a />').html(content).text().trim().replace(new RegExp("[\n ]+...$"),'');
                var title = entry.title;
                if (settings.hide_username)
                    title = title.replace(new RegExp('^' + entry.author + ' '), '');
                var li_entry = $('<li />').text(title);
                var div_entry = $('<a />').append(li_entry);
                div_entry.attr({
                    'href': entry.link,
                    'target': '_blank',
                    'title': description
                });
                $(container).append(div_entry);
            });
        }
    }

    $.fn.extend({
        activities:
            function(options) {
                var defaults = {
                    'username': '',
                    'hide_username': false,
                }

                var settings = $.extend(defaults, options);

                return this.each(function() {
                    var container = $(this)
                    $.ajax({
                        url: 'http://ajax.googleapis.com/ajax/services/feed/load?v=1.0&num=10&callback=?&q=' + encodeURIComponent('http://github.com/' + settings.username + '.atom'),
                        async: true,
                        dataType: 'json',
                        success: function(data) {
                            parse(data.responseData.feed, container, settings);
                        }
                    });
                });
        }
    });
})(jQuery);

$(document).ready(function() {
    var github_link = $('#github_user').text().split('/');
    var member = github_link[github_link.length-1]
    $('ul.activities').activities({ 'username': member, 'hide_username': true });
});
