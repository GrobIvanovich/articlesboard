$(document).ready(function() {
    $.ajaxSetup({ cache: false });
    var count = 0;
    $('#notificationsList').html('');
    $.get('/accounts/profile/notifyuser', function(data) {
        // $('#notificationsBlock').html('<ul class="list-unstyled" id="notificationsList"></ul>');
        
        $.each($.parseJSON(data.notifications), function(index, element) {
        	// console.log(element.sender);
           
            $('#notificationsList').append('<li><a class="btn btn-info ntf" href="' + element.sender + '"><font color="white">' + element.n_type + '</font></a><div style="display:none" class="row">' + element.content + '</div></li>')
            count++;
        });
    }).done(function() {
	    // console.log('Notifications: ' + count);
	    if (count > 0){
	    	$('.notification').html(count);
		}
		else {
			$('.notification').css('display', 'none');
            $('#notificationsList').html('<h6 class="dropdown-item" style="cursor: default;">У вас нет новых оповещений</h6>');
		}
	});
});
