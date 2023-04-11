// let myVar = setInterval(myTimer ,1000);
// function myTimer() {
//     var  XMLrequest = new XMLHttpRequest();
//     XMLrequest.open('GET', 'http://localhost:5000/send', true);
//     XMLrequest.send();
//     XMLrequest.onreadystatechange = function() {
//         if (XMLrequest.readyState == 4 && XMLrequest.status == 200) {
//             var data = JSON.parse(XMLrequest.responseText);
//             document.getElementById("demo").innerHTML += data['device_id'];
//         }
//     }
// }
function drawChart(d, target) {

    // var data = google.visualization.arrayToDataTable([
    //     ['Year', 'Sales', 'Expenses'],
    //     ['2004',  1000,      400],
    //     ['2005',  1170,      460],
    //     ['2006',  660,       1120],
    //     ['2007',  1030,      540]
    //   ]);
    // console.log(d);
    var data = google.visualization.arrayToDataTable(d);

    var options = {
      title: 'Company Performance',
      curveType: 'function',
        legend: { position: 'bottom' }
        
    };

    var chart = new google.visualization.LineChart(document.getElementById(target));

    chart.draw(data, options);
  }

function drawAreaChart(d) {

  var data = google.visualization.arrayToDataTable(d);

  var options = {
    title: 'Visual Representation of Data',
    hAxis: {title: d[0][0],  titleTextStyle: {color: '#333'}},
    vAxis: {minValue: 0}
  };

  var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}


function drawBarChart(d) {

  var data = google.visualization.arrayToDataTable(d);

  var options = {
    chart: {
      title: 'Visual Representation of Data',
    },
    bars: 'horizontal' // Required for Material Bar Charts.
  };

  var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}


function drawColumnChart(d) {

  var data = google.visualization.arrayToDataTable(d);

  var options = {
    chart: {
      title: 'Visual Representation of Data',
    }
    
  };

  var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}


function drawPieChart(d) {

  var data = google.visualization.arrayToDataTable(d);

  var options = {
    title: 'Visual Representation of Data',
  };

  var chart = new google.visualization.PieChart(document.getElementById('chart_div'));

  chart.draw(data, options);
}


function drawLineChart(d, target) {

  var data = google.visualization.arrayToDataTable(d);

  var options = {
    // title: 'Visual Representation of Data',
    // curveType: 'function',
    hAxis: {title: d[0][0],  titleTextStyle: {color: '#222', fontSize: 12, bold: true, italic: false}},
    vAxis: {title: d[0][1], titleTextStyle: {color: '#222',  fontSize: 12, bold: true, italic: false}},
    legend: 'none'
  };

  var chart = new google.visualization.LineChart(document.getElementById(target));

  chart.draw(data, options);
}


function drawScatterChart(d) {

  var data = google.visualization.arrayToDataTable(d);

  var options = {
    title: 'Visual Representation of Data',
    hAxis: {title: d[0][0],  titleTextStyle: {color: '#333'}},
    vAxis: {title: d[0][1], titleTextStyle: {color: '#333'}},
    legend: 'none'
  };

  var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

  chart.draw(data, options);
}


function drawHistogramChart(d) {

  var data = google.visualization.arrayToDataTable(d);

  var options = {
    title: 'Visual Representation of Data',
    legend: { position: 'none' },
  };

  var chart = new google.visualization.Histogram(document.getElementById('chart_div'));
  chart.draw(data, options);
}


function drawCandlestickChart(d) {
  var data = google.visualization.arrayToDataTable(d.slice(1), true);

  var options = {
    legend:'none'
  };

  var chart = new google.visualization.CandlestickChart(document.getElementById('chart_div'));

  chart.draw(data, options);
}


fahrenheitUnit = (temperature) => temperature;
celsiusUnit = (temperature) => (temperature - 32) * 5 / 9;
function changeUnit() {
    var unit = document.getElementById("unitButton").innerHTML;
    if (unit == "View in Celsius") {
        document.getElementById("unitButton").innerHTML = "View in Fahrenheit";
        document.getElementById("unitSym").innerHTML = "°C";
    } else {
        document.getElementById("unitButton").innerHTML = "View in Celsius";
        document.getElementById("unitSym").innerHTML = "°F";
    }
}

let myVar = setInterval(myTimer, 5000);
function myTimer() {
    var XMLrequest = new XMLHttpRequest();
    XMLrequest.open('POST', 'http://127.0.0.1:8000/send', true);
    XMLrequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    XMLrequest.send('device_id=1');
    XMLrequest.onreadystatechange = function () {
        if (XMLrequest.readyState == 4 && XMLrequest.status == 200) {
            var data = JSON.parse(XMLrequest.responseText);
            document.getElementById("device_id").innerHTML = data['device_id'];
            document.getElementById("weather").innerHTML = data['weather'];
            document.getElementById("humidity").innerHTML = data['humidity'] + '%';
            document.getElementById("pressure").innerHTML = data['pressure'] + 'in';
            document.getElementById("rain").innerHTML = data['rain'] + '%';

            if (document.getElementById("unitButton").innerHTML == "View in Celsius") {
                document.getElementById("temperature").innerHTML = fahrenheitUnit(data['temperature']);
            } else {
                document.getElementById("temperature").innerHTML = int(celsiusUnit(data['temperature']));
            }

            // google.charts.setOnLoadCallback(drawChart);
            var data = [['Time', 'Temperature'], ['2020', 10], ['2021', 15], ['2022', 30], ['2023', 25], ['2024', 40]];
            google.charts.setOnLoadCallback(drawLineChart(data, 'temperature_chart_div'));

        }
    }
    // below 2 lines only for testing
    var data = [['Time', 'Temperature'], ['2020', 10], ['2021', 15], ['2022', 30], ['2023', 25], ['2024', 40]];
    google.charts.setOnLoadCallback(drawLineChart(data, 'temperature_chart_div'));
    var data = [['Time', 'Humidity'], ['2020', 10], ['2021', 15], ['2022', 30], ['2023', 25], ['2024', 40]];
    google.charts.setOnLoadCallback(drawLineChart(data, 'humidity_chart_div'));
    var data = [['Time', 'Pressure'], ['2020', 10], ['2021', 15], ['2022', 30], ['2023', 25], ['2024', 40]];
    google.charts.setOnLoadCallback(drawLineChart(data, 'pressure_chart_div'));
    var data = [['Time', 'Rain'], ['2020', 10], ['2021', 15], ['2022', 30], ['2023', 25], ['2024', 40]];
    google.charts.setOnLoadCallback(drawLineChart(data, 'rain_chart_div'));
}

handleVisibilityChange = () => {
    if (document.visibilityState === 'visible') {
        x = setInterval(myTimer, 5000);
    } else {
        clearInterval(x);
    }
}
document.addEventListener('visibilitychange', handleVisibilityChange);
