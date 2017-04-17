$(document).ready(function(){



$("#loader").hide();
$("#give").hide();

// function to print the tweets that Sparro is analyzing for sentiment + spinning wheel

function printTweets(callback) {

    $.post("/show-tweets.json", function(results) {
        var tweet_sents = Object.values(results);
        // console.log(tweet_sents)
        for (var tweet_list of tweet_sents) {
            var tweet = tweet_list[0];
            var sent = tweet_list[1];
            $(".tweet").after('"'+tweet+'"' + "<br>");
            $(".sentiment").after(sent + "<br>");
            
        };

        $("#give").show();
        $("#loader").show();
    
        if (callback) {
            callback();
        }

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


// function to animate tweets onto the page
function typeTweet(tweet) {
    console.log(tweet);
      $("#element").typed({
        strings: [quote],
        typeSpeed: 20
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
$("#get-quote").bind('click', function() {
    printTweets(function() {
        setTimeout(showQuote, 5000)
    });
})
// // $("#get-quote").bind('click', showGauge);














});

