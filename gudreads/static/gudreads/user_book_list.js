const showRatings = () => {
	$('.ui.rating').rating({
		maxRating: 5,
		onRate: function(rating) {
			const bookId = $(this).data('id')
			$.ajax({
				url: `update/${bookId}`,
				data: {
					rating,
				},
				success: '',
			})
		},
	})
	$('.ui.rating').rating('setting', 'clearable', true)
}

$(document).ready(showRatings)

$('.delete-button').click(function() {
	const bookId = $(this).data('id')
	$.ajax({
		url: `delete/${bookId}`,
		success: function() {
			location.reload()
		},
	})
})
