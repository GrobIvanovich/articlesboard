$(document).ready(function() {
    $.ajaxSetup({ cache: false });
    // setInterval(function() {
        $.get('/accounts/profile/notifyuser', function(data) {
        	// $('#notificationsBlock').html('');
            $.each($.parseJSON(data.notifications), function(index, element) {
            	// $.each($('#notificationsBlock').children(), function(ch_index, child){
            	// 	if (element.content == $(child + ' #notificationsContent').html()){
        
            	// 	}
            	// });
            	console.log(element.sender);
                $('#notificationsBlock').html(
                	'<a class="dropdown-item" href="' + element.sender + '/">' +
	                	'<div class="row">' + 
	                		element.n_type + 
                		'</div>' +
	                	'<div class="row" name="notificationsContent">' + 
	                		'<div style="display: none">' + element.content + '</div>' +
	            		'</div>' +
	            		'<div class="row">' +
	                		'<small>' + element.created_at + '</small>' + 
	            		'</div>'+
                	'</a>'
                	);
            });
        });
    // }, 3000);
});