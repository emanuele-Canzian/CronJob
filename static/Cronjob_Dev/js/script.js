$(document).ready(function () {

    $(function () {
        $('.radio-button').on('change', function () {
            var cron = $(this).val();
            $('.disabled-radio').not('#' + cron).prop('disabled', true);
            $('.' + cron).prop('disabled', false);

            console.log($('.disabled-radio').not('#' + cron).prop('disabled', true));
            console.log($('.' + cron).prop('disabled', false));
        });
    });


});

  function showBorder() {
        var x = document.getElementById("border2");
        if (x.style.display === "flex") {
            x.style.display = "none";
        } else {
            x.style.display = "flex";
        }
    }
