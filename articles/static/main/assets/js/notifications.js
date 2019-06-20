$(document).ready(function() {
    $.ajaxSetup({ cache: false });
    var count = 0;
    $.get('/accounts/profile/notifyuser', function(data) {
        // $('#notificationsBlock').html('<ul class="list-unstyled" id="notificationsList"></ul>');
        
        $.each($.parseJSON(data.notifications), function(index, element) {
        	// console.log(element.sender);
           
            $('#notificationsList').append('<li><a class="btn btn-primary ntf" href="' + element.sender + '">' + element.n_type + '</a><div style="display:none" class="row">' + element.content + '</div></li>')
            count++;
        });
    }).done(function() {
	    console.log('Notifications: ' + count);
	    if (count > 0){
	    	$('.notification').html(count);
		}
		else {
			$('.notification').css('display', 'none');
		}
	});
});
