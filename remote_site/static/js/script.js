// var BASE_URL = "http://127.0.0.1:8000"
var BASE_URL = "weatherdetectionsystem-production.up.railway.app"

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var csrftoken = getCookie('csrftoken');
var XMLrequest = new XMLHttpRequest();
var device_id = "";
var weatherNotes = {
  "Mostly Cloudy": "This refers to a sky condition where more than half of the sky is covered by clouds. While it may not be raining or storming, it can still make the day feel gloomy and dim. The clouds can act as a barrier to the sun's rays, making it feel cooler than it actually is. It's a good idea to dress in layers to stay comfortable in this weather. Additionally, outdoor activities such as sports, photography or stargazing may be affected due to reduced visibility and dimmer lighting.",
  "Fair": "This refers to a sky condition where the skies are mostly clear and the weather is calm. This type of weather is ideal for outdoor activities like hiking, picnics or going to the beach. The sunshine is abundant and there is little chance of rain, making it a great day to spend outside.",
  "Partly Cloudy": "This refers to a sky condition where the skies are a mix of sun and clouds. This can lead to fluctuating temperatures throughout the day, with periods of direct sunlight and periods of cloud cover. Dressing in layers is recommended for this type of weather, as it can be difficult to predict the temperature changes throughout the day. Outdoor activities such as sports or photography may be affected due to the changing lighting conditions.",
  "Cloudy": "This refers to a sky condition where the skies are covered with clouds and there is no direct sunlight. This type of weather can make it feel cooler than it actually is, and it can be difficult to predict when or if it will rain. Outdoor activities such as sports or photography may be affected due to the reduced visibility and dimmer lighting.",
  "Thunder": "This refers to a weather condition where there is lightning and thunder in the area. This type of weather can be dangerous and it's recommended to seek shelter indoors until the storm passes. It's important to avoid outdoor activities during thunderstorms, as they can be life-threatening.",
  "Light Rain": "This refers to a weather condition where there is a light drizzle or mist in the air. It may not be heavy enough to require an umbrella, but it can still make the ground slippery and affect outdoor activities such as sports or picnics.",
  "Light Rain Shower": "This refers to a weather condition where there are short bursts of light rain, usually lasting only a few minutes. It's a good idea to have an umbrella or raincoat handy, as these showers can occur unexpectedly. Outdoor activities may be interrupted briefly during these showers.",
  "Fog": "This refers to a weather condition where there is a thick mist or haze in the air. This can reduce visibility and make it difficult to drive or navigate outside. It's important to exercise caution when driving in foggy conditions, as it can be difficult to see other vehicles or obstacles in the road.",
  "Rain Shower": "This refers to a weather condition where there are short bursts of heavy rain, usually lasting only a few minutes. It's a good idea to have an umbrella or raincoat handy, as these showers can occur unexpectedly. Outdoor activities may need to be postponed during these showers.",
  "Light Drizzle": "This refers to a weather condition where there is a very light and fine rain, usually falling slowly over a long period of time. It may not be heavy enough to require an umbrella, but it can still make the ground slippery and affect outdoor activities such as sports or picnics.",
  "Rain": "This refers to a weather condition where there is a steady, heavy rainfall over a prolonged period of time. It's important to have an umbrella or raincoat handy, as well as to dress in waterproof clothing and shoes."
};

function drawLineChart(d, target) {
  var data = google.visualization.arrayToDataTable(d);

  var options = {
    hAxis: { title: d[0][0], titleTextStyle: { color: '#222', fontSize: 12, bold: true, italic: false } },
    vAxis: { title: d[0][1], titleTextStyle: { color: '#222', fontSize: 12, bold: true, italic: false } },
    legend: 'none'
  };

  var chart = new google.visualization.LineChart(document.getElementById(target));
  chart.draw(data, options);
}

fahrenheitUnit = (temperature) => temperature;
celsiusUnit = (temperature) => (temperature - 32) * 5 / 9;

function changeUnit() {
  var unit = document.getElementById("unitButton").innerHTML;
  if (unit == "View in Celsius") {
    document.getElementById("unitButton").innerHTML = "View in Fahrenheit";
    document.getElementsByClassName("unitSym")[0].innerHTML = "°C";
    document.getElementsByClassName("unitSym")[1].innerHTML = "°C";
    document.getElementsByClassName("unitSym")[2].innerHTML = "°C";
  } else {
    document.getElementById("unitButton").innerHTML = "View in Celsius";
    document.getElementsByClassName("unitSym")[0].innerHTML = "°F";
    document.getElementsByClassName("unitSym")[1].innerHTML = "°F";
    document.getElementsByClassName("unitSym")[2].innerHTML = "°F";
  }
}

document.getElementById('device_id').addEventListener('input', (e) => {
  device_id = e.target.value;
});

let myVar = setInterval(myTimer, 5000);
function myTimer() {
  try {
    XMLrequest.open('POST', 'send/', true);
    XMLrequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    XMLrequest.setRequestHeader('X-CSRFToken', csrftoken);
    console.log(csrftoken);
    XMLrequest.send('device_id=' + device_id);
    XMLrequest.onreadystatechange = function () {
      if (XMLrequest.readyState == 4 && XMLrequest.status == 200) {
        if (XMLrequest.responseText != "[]") {
          if(document.getElementById("temperature_section").style.visibility == "hidden"){
            document.getElementById("temperature_section").style.visibility = "visible";
          }
          if(document.getElementById("weather_section").style.visibility == "hidden"){
            document.getElementById("weather_section").style.visibility = "visible";
          }
          if(document.getElementById("humidity_pressure_rain_section").style.visibility == "hidden"){
            document.getElementById("humidity_pressure_rain_section").style.visibility = "visible";
          }

          var data = JSON.parse(XMLrequest.responseText);

          var temperature = [];
          var humidity = [];
          var pressure = [];
          var rain = [];
          var weather = [];
          var time = [];
          for (var i = 0; i < data.length; i++) {

            if (document.getElementById("unitButton").innerHTML == "View in Celsius") {
              temperature.push(fahrenheitUnit(data[i]['temperature']));
            } else {
              temperature.push(parseInt(celsiusUnit(data[i]['temperature'])));
            }
            humidity.push(data[i]['humidity']);
            pressure.push(data[i]['pressure']);
            rain.push(data[i]['rain']);
            weather.push(data[i]['weather']);
            time.push(data[i]['timestamp']);
          }

          document.getElementById("weather").innerHTML = weather[0];
          document.getElementById("temperature").innerHTML = temperature[0];
          document.getElementById("humidity").innerHTML = humidity[0] + '%';
          document.getElementById("pressure").innerHTML = pressure[0].toFixed(2) + 'in';
          document.getElementById("rain").innerHTML = rain[0] + '%';

          for (var t = 0; t < time.length; t++) {
            time[t] = time[t].slice(11, 19);
          }

          document.getElementById("minTemp").innerHTML = Math.min(...temperature);
          document.getElementById("maxTemp").innerHTML = Math.max(...temperature);
          document.getElementById("minHum").innerHTML = Math.min(...humidity) + '%';
          document.getElementById("maxHum").innerHTML = Math.max(...humidity) + '%';
          document.getElementById("minPres").innerHTML = Math.min(...pressure).toFixed(2) + 'in';
          document.getElementById("maxPres").innerHTML = Math.max(...pressure).toFixed(2) + 'in';
          document.getElementById("minRain").innerHTML = Math.min(...rain) + '%';
          document.getElementById("maxRain").innerHTML = Math.max(...rain) + '%';

          document.getElementById("weatherNote").innerHTML = weatherNotes[weather[0]];

          var temperatureMap = [['Time', 'Temperature'], [time[4], temperature[4]], [time[3], temperature[3]], [time[2], temperature[2]], [time[1], temperature[1]], [time[0], temperature[0]]];
          google.charts.setOnLoadCallback(drawLineChart(temperatureMap, 'temperature_chart_div'));
          var humidityMap = [['Time', 'Humidity'], [time[4], humidity[4]], [time[3], humidity[3]], [time[2], humidity[2]], [time[1], humidity[1]], [time[0], humidity[0]]];
          google.charts.setOnLoadCallback(drawLineChart(humidityMap, 'humidity_chart_div'));
          var pressureMap = [['Time', 'Pressure'], [time[4], pressure[4]], [time[3], pressure[3]], [time[2], pressure[2]], [time[1], pressure[1]], [time[0], pressure[0]]];
          google.charts.setOnLoadCallback(drawLineChart(pressureMap, 'pressure_chart_div'));
          var rainMap = [['Time', 'Rain'], [time[4], rain[4]], [time[3], rain[3]], [time[2], rain[2]], [time[1], rain[1]], [time[0], rain[0]]];
          google.charts.setOnLoadCallback(drawLineChart(rainMap, 'rain_chart_div'));
        }
      }
    }
  } catch (error) {
    null;
  }
}

handleVisibilityChange = () => {
  if (document.visibilityState === 'visible') {
    x = setInterval(myTimer, 5000);
  } else {
    clearInterval(x);
  }
}
document.addEventListener('visibilitychange', handleVisibilityChange);
