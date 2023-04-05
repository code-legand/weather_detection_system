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
    XMLrequest.open('GET', 'http://127.0.0.1:8000/send', true);
    XMLrequest.send();
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
        }
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
