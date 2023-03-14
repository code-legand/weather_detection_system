let myVar = setInterval(myTimer ,1000);
function myTimer() {
    var  XMLrequest = new XMLHttpRequest();
    XMLrequest.open('GET', 'http://localhost:5000/send', true);
    XMLrequest.send();
    XMLrequest.onreadystatechange = function() {
        if (XMLrequest.readyState == 4 && XMLrequest.status == 200) {
            var data = JSON.parse(XMLrequest.responseText);
            document.getElementById("demo").innerHTML += data['device_id'];
        }
    }
}
