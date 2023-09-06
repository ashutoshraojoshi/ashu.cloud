$(document).ready(function () {
    $('#category').change(function () {
        const selectedCategory = $(this).val();
        if (selectedCategory === 'all') {
            $('.col-md-6[data-category]').show();
        } else {
            $('.col-md-6[data-category]').hide();
            $(`.col-md-6[data-category="${selectedCategory}"]`).show();
        }
    });
});