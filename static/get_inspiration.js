$(document).ready(function(){

// Show quote


function showQuote(event) {
    
    var twitter_handle = $('#twitter_handle').val();

    $.get("/inspire-process.json", {"twitter_handle"=twitter_handle}, function(results) {
                                        var quote_content = results;
                                        $('#text-area').html(quote_content);  

    });
}

// event listener
$("#get-quote").on('click', showQuote);






});