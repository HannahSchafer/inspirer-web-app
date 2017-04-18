$(document).ready(function(){


 $("#set-reminder-submit").on("submit", function(event) {
    event.preventDefault();
    var form_data = $("#set-reminder-submit").serialize()
    $.post('/set-reminder.json', form_data, function() {
        $('#reminder-modal').modal('hide');
    });

 });











  });