$(document).ready(function(){



// Show quote
function showQuote(event) {
    
    $.post("/inspire-process.json", function(results) {
                                        var quote_content = results.quote;
                                        $('#text-area').html(quote_content);  

    });
}

// event listener
$("#get-quote").on('click', showQuote);

});

//if/else statement to parse results if adding more than 'quote'