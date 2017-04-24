

var options = {
        legend: {
            display: true,
            labels: {
                fontColor: 'rgb(0, 0, 0)'
            }
        }
};

    


// Donut chart of user's overall moods (positive/negative)
var ctx_donut = $('#donutChart').get(0).getContext('2d');


$.get("/mood-donut.json", function (data) {
var myDonutChart = new Chart(ctx_donut, {
    type: 'doughnut',
    data: data,
    options: options
});

$('#donutLegend').html(myDonutChart.generateLegend());

});


// Line Chart of user's mood over time
    var ctx_line = $("#lineChart").get(0).getContext("2d");

    $.get("/mood-line.json", function (data) {
      var myLineChart = new Chart.Line(ctx_line, {
                                    type: 'line',
                                    data: data,
                                    options: {
                                        scales: {
                                            yAxes: [{
                                                ticks:{
                                                    max: 2,
                                                    min: -2,
                                                    beginAtZero:true


                                                }
                                            }]
                                        }
                                    }
                                    // scaleOverride : true,
                                    // scaleStartValue : 0 ,
                                });
      $("#lineLegend").html(myLineChart.generateLegend());
    });


// Bar Chart of user's mood over time

var ctx_bar = $("#barChart").get(0).getContext("2d");

$.get("/mood-bar.json", function (data) {
var myBarChart = new Chart.Bar(ctx_bar, {
    type: 'bar',
    data: data,
    options: options
});

$("#barLegend").html(myBarChart.generateLegend());
    });


