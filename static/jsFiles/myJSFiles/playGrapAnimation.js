$(document).ready(function() {



    window.onload = function(){

        function graph1(){

            var dataPoints1 = [];
            var dataPoints2 = [];

            var chart = new CanvasJS.Chart("currentTestingGraph", {
                backgroundColor: "",
                zoomEnabled: true,
                title: {
                    text: "Currently Testing People Status"
                },
                axisX: {
                    title: "chart updates every 3 secs"
                },
                axisY:{
                    prefix: ""
                }, 
                toolTip: {
                    shared: true
                },
                legend: {
                    cursor:"pointer",
                    verticalAlign: "top",
                    fontSize: 22,
                    fontColor: "dimGrey",
                    itemclick : toggleDataSeries
                },
                data: [{ 
                    type: "line",
                    xValueType: "dateTime",
                    yValueFormatString: "####",
                    xValueFormatString: "hh:mm:ss TT",
                    showInLegend: true,
                    name: "People Tested",
                    dataPoints: dataPoints1,
                    color: "green"
                    },
                    {				
                        type: "line",
                        xValueType: "dateTime",
                        yValueFormatString: "####",
                        showInLegend: true,
                        name: "People With Severe Disease" ,
                        dataPoints: dataPoints2,
                        color: "red",
                }]
            });

            function toggleDataSeries(e) {
                if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                    e.dataSeries.visible = false;
                }
                else {
                    e.dataSeries.visible = true;
                }
                chart.render();
            }

            var updateInterval = 3000;
            // initial value
            var yValue1 = 600; 
            var yValue2 = 605;

            var time = new Date;
            // starting at 9.30 am

            time.setHours(time.getHours());
            time.setMinutes(time.getMinutes());
            time.setSeconds(time.getSeconds());
            time.setMilliseconds(time.getMilliseconds());

            function updateChart(count) {
                count = count || 1;
                var deltaY1, deltaY2;
                for (var i = 0; i < count; i++) {
                    time.setTime(time.getTime()+ updateInterval);
                    deltaY1 = .5 + Math.random() *(-.5-.5);
                    deltaY2 = .5 + Math.random() *(-.5-.5);

                // adding random value and rounding it to two digits. 
                // yValue1 = Math.round((yValue1 + deltaY1)*100)/100;
                // yValue2 = Math.round((yValue2 + deltaY2)*100)/100;
                yValue1 = Math.round(Math.random() * (820 - 740) + 740);
                yValue2 = Math.round(Math.random() * (732 - 659) + 659);

                // pushing the new values
                dataPoints1.push({
                    x: time.getTime(),
                    y: yValue1
                });
                
                dataPoints2.push({
                    x: time.getTime(),
                    y: yValue2
                });
                }
                dataPoints1.shift();
                dataPoints2.shift();

                // updating legend text with  updated with y Value 
                chart.options.data[0].legendText = " People Tested - " + yValue1;
                chart.options.data[1].legendText = " People With Severe Disease - " + yValue2; 
                chart.render();
            }
            // generates first set of dataPoints 
            updateChart(100);	
            setInterval(function(){updateChart()}, updateInterval);


            
        }
        graph1();
    }

});