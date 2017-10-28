$(document).ready(function() {

$.post( "/getresults/", {}, function( data ) {

var doughnutChart = document.getElementById("chart").getContext("2d");

        var set = data.stats;

        var data1 =[]
        var labels1 =[]

        colors = ["#FFA693", "#9DAFE5", "#FF9DC3", "#F5E38D", "#9CE59D"];
        
        for (var i = 0; i < set.length; i++) {
            data1.push(set[i].total);
            labels1.push(set[i].category);
        };

        var data = {
            datasets: [{
                data: data1,
                backgroundColor: colors
            }],
            labels: labels1
        };
        
        window.myDoughnut = new Chart(doughnutChart,{
            type: 'doughnut',
            data: data,
            options: {
            segmentStrokeColor : "#fff",
            tooltipTitleFontFamily: "'Roboto','Helvetica Neue', 'Helvetica', 'Arial', sans-serif",// String - Tooltip title font declaration for the scale label        
            percentageInnerCutout : 50,
            animationSteps : 15,
            segmentStrokeWidth : 4,
            animateScale: true,
            percentageInnerCutout : 60,
            responsive : true,
            }
        });

});

});