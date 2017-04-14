function typeQuote(quote) {
    console.log(quote);
      $(".element").typed({
        strings: [quote],
        typeSpeed: 0
    });
    console.log("hello world")
}

$(document).ready(function(){



// Show quote
function showQuote(event) {
    
    $.post("/inspire-process.json", function(results) {
                                        var quote_content = results.quote;
                                        typeQuote(quote_content);
                                        // $('#text-area').typed({
                                        // stringsElement: quote_content,
                                        // typeSpeed: 0
                              

    });
}

// event listener
$("#get-quote").on('click', showQuote);

});

//if/else statement to parse results if adding more than 'quote'