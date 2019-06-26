$(document).ready(function() {
	var data_to_send = {
		username: '',
		csrfmiddlewaretoken: $('#csrf_token').children().val()
	}
	$('#id_receiver').on('input', function() {
		data_to_send.username = $('#id_receiver').val();
		if (data_to_send.username != ''){
			$.post('autocomplete/', data_to_send, function(data, status) {
			}).done(function(data) {
				$('#suggestions').css('display', 'block');
				var users_list = '';
				users_list += '<ul class="list-unstyled">';
				$.each($.parseJSON(data.users), function(index, element) {
					users_list += '<li><a href="#" onclick="suggestion_click(this)">' + element.username + '</a></li>';
				});
				users_list += '</ul>';
				$('#suggestions').html(users_list);
			}).fail(function() {
				console.log('autocomplete failed');
			});
		}
		else {
			$('#suggestions').html('');
		}
	});
});