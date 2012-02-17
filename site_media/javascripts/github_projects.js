function github_project() {
    var html = '<div class="row individual-project">';
            html += '<span class="span16">';
                html += '<div class="project-data">';
                    html += '<h3><a href="${url}">${name}</a></h3>';
                    html += '<p>${description}</p>';
                    html += "<div class='project-infos'>";
                        html += "<span>watchers: ${watchers}</span>";
                        html += "<span>fork: ${forks}</span>";
                        html += "<span>homepage: <a href='${homepage}'</a>${homepage}</span>";
                    html += "</div>";
                html += '</div>';
            html += "</span>";
        html += "</div>";
        html += '<br />';
    return html;
}

$.template("github_project", github_project());

$.ajax({
    url:"http://github.com/api/v2/json/repos/show/nsi-iff?callback=?",
    dataType: "json",
    success: function(data) {
        $.each(data.repositories, function(index, project){
            $.tmpl("github_project", project).appendTo(".box-projects .content.container");
        });
    }
});

