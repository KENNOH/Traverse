
$(function () {
	// body...
	$('#location').change(function () {
		// body...
		$.ajax({
			type: "POST",
			url: "/filtering_packages/",
			data: {
				search_text: $('#location').val(),
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess1,
			dataType: 'html'
		});

	});
});

function searchSuccess1(data, textStatus, jqXHR) {
	$('#results1').html(data);
}