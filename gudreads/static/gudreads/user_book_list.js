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
				success: function() {
					location.reload()
				},
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

$('#id_book_name').on('input', function() {
	let bookQuery = $(this).val()
	if (bookQuery.length > 2) {
		$.ajax({
			url: 'ajax/autocomplete',
			data: {
				query: encodeURIComponent(bookQuery),
			},
			success: function(results) {
				const resultsArr = JSON.parse(results)
				$('#id_book_name').autocomplete({
					source: resultsArr,
					select: function(event, ui) {
						$('#id_book_name').val(ui.item.value)
						$('#id_book_author').val(ui.item.author)
						$('#id_book_image').val(ui.item.image)
					},
				})
			},
		})
	}
})
