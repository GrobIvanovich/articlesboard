$(document).ready(function() {
    $.ajaxSetup({ cache: false }); // This part addresses an IE bug.  without it, IE will only load the first number and will never refresh
    setInterval(function() {
        $.get('{% url "articles:notify_user" %}', function(data) {
            $.each($.parseJSON(data.notifications), function(index, element) {
                $('#notificationsBlock').append('<a class="dropdown-item" href="javascript:void(0)">' + element.n_type + '</a>');
            });
        });
    }, 3000); // the "3000" 
});