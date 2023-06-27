$(document).ready(function () {
    $('#text-input').on('input', function () {
        var text = $(this).val();
        $.ajax({
            url: '/encode',
            method: 'POST',
            data: { text: text },
            success: function (response) {
                $('#encoded-text').text(response);
            }
        });
    });
});

$(document).ready(function () {
    $('#morse-input').on('input', function () {
        var text = $(this).val();
        $.ajax({
            url: '/decode',
            method: 'POST',
            data: { text: text },
            success: function (response) {
                $('#decoded-text').text(response);
            }
        });
    });
});