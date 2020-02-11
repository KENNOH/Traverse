$(function() {
	// body...
	$('#listing').change(function() {
		// body...
		$.ajax({
			type: "POST",
            url: "/filter_packages/",
			data: {
				search_text : $('#listing').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType:'html'
		});

	});
});

function searchSuccess(data,textStatus,jqXHR) 
{
    $('#results').html(data);
}
