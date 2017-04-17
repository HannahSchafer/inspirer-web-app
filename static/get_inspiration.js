$(document).ready(function(){



$("#loader").hide();
$("#give").hide();



// function to print the tweets that Sparro is analyzing for sentiment + spinning wheel

function printTweets(event) {

    $.post("/show-tweets.json", function(results) {
        var tweet_sents = Object.values(results);
        // console.log(tweet_sents)
        for (var tweet_list of tweet_sents) {
            var tweet = tweet_list[0];
            var sent = tweet_list[1];
            $(".tweet").after('"'+tweet+'"' + "<br>");
            $(".sentiment").after(sent + "<br>");
            
        };

// setInterval(printTw, 10000);
            
        //     // console.log(tweet, sent);
        //     console.log('999999999');
        // }
        // var tweet = results[tweet];
        // tw = $("#tweet").html(tweet);
        // for (i=0; i<results.length; i++){
        //     var tweet = results.tweet[0];
        //     var sentiment = results.tweet[1];
        //     tw = $("#tweet").html(tweet);
        //     sent = $("#sentiment").html(sentiment);

        // }
        $("#give").show();
        $("#loader").show();
    
        // if i get results and have done everything i want to do with them, then
        //start timer for the next function

    });
}




// function to print the d3 gauge graph showing percentage postitive/negative + spinning wheel
function showGauge(event) {

    $.post("/show-avg-sent.json", function(results) {
        var avg = results.percentage;
        $("#average").show(avg);
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
 
}


// function to show quote
function showQuote(event) {
    
    $.post("/inspire-process.json", function(results) {
                                        var quote_content = results.quote;
                                        typeQuote(quote_content);
                                        $("#loader").hide();
                                        $("#give").hide();
                                        $("#tweet-container").hide();

                                       
                            
    });
}





// event listener
$("#get-quote").bind('click', printTweets);
// $("#get-quote").bind('click', showGauge);
$("#get-quote").bind('click', showQuote);



// pass the one event it an anonymous function that runs print tweets
// then pass it the showquote function after a few seconds
// add new callback











});

//if/else statement to parse results if adding more than 'quote'