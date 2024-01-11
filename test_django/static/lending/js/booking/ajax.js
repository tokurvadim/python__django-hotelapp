$(document).ready(function() {
            $("#form_booking").submit(function(event) {
                event.preventDefault();
                let formData = $(this).serialize();
                $.ajax({
                    url: $(this).attr("action"),
                    type: $(this).attr("method"),
                    data: formData,
                    success: function(response) {
                        $("#form_message").attr('style', `font-size: 1.1rem; color: ${response.color};`);
                        $("#form_message").html(response.message);
                    },
                    error: function(response) {
                        $("#form_message").attr('style', `font-size: 1.1rem; color: red;`);
                        $("#form_message").html('Ошибка сервера');
                    }
                });
            });
        });