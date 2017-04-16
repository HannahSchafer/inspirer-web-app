$(document).ready(function(){

$("#loader").hide();

// function to print the tweets that Sparro is analyzing for sentiment + spinning wheel

function printTweets(event) {

    $.post("/show-tweets.json", function(results) {
        console.log(results);
        console.log('999999999');
        console.log(results);
        var tweet = results[tweet];
        tw = $("#tweet").html(tweet);
        // for (i=0; i<results.length; i++){
        //     var tweet = results.tweet[0];
        //     var sentiment = results.tweet[1];
        //     tw = $("#tweet").html(tweet);
        //     sent = $("#sentiment").html(sentiment);

        // }
        
        $("#loader").show();

    });
}

// function to print the d3 gauge graph showing percentage postitive/negative + spinning wheel
function showGauge(event) {

    $.post("/show-avg-sent.json", function(results) {
        var avg = results.percentage;
        $("#average").html(avg);
        $("#loader").show();

    });
}

// function to animate quote onto the page
function typeQuote(quote) {
    console.log(quote);
      $("#element").typed({
        strings: [quote],
        typeSpeed: 20
    });
    console.log("hello world")
}


// function to show quote
function showQuote(event) {
    
    $.post("/inspire-process.json", function(results) {
                                        var quote_content = results.quote;
                                        typeQuote(quote_content);
                                        // sent.hide();
                                        // tw.hide();
                                        $("#loader").hide();
                                       
                            
    });
}

// event listener
$("#get-quote").bind('click', printTweets);
$("#get-quote").bind('click', showGauge);
$("#get-quote").bind('click', showQuote);















});

//if/else statement to parse results if adding more than 'quote'