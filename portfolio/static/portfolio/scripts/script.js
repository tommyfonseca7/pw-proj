let weather = {
    "apiKey": "c0d0e1106874e7d82b3c0aaddacbe41f",

    fetchWeather: function(city) {
        fetch("https://api.openweathermap.org/data/2.5/weather?q=" + city  +"&units=metric&appid=" + this.apiKey 
        ).then((response) => response.json())
        .then((data) => this.displayWeahter(data));
    },

    displayWeahter : function(data) {
        const {name} = data;
        const { icon, description } = data.weather[0];
        const { temp, humidity } = data.main;
        const { speed } = data.wind;
        document.querySelector(".city").innerText = "Weather in " + name;
        document.querySelector(".weather-icon").src = "https://openweathermap.org/img/wn/" + icon + ".png";
        document.querySelector(".weather-desc").innerText = description;
        document.querySelector(".temp").innerText = temp + "° C";
        document.querySelector(".humidity").innerText = "Humidity: " + humidity + "%";
        document.querySelector(".wind").innerText = "Wind speed: " + speed + "%";
    },

    search: function() {
        this.fetchWeather(document.querySelector(".search-bar").value)
    },
};

document.querySelector(".search button")
.addEventListener("click", function() {
    weather.search();
} )

document.querySelector(".search-bar")
.addEventListener("keyup", function(event) {
    if (event.key == "Enter") {
        weather.search();
    }
} )

weather.fetchWeather("Lisboa");


function displayTime(){
    var dateTime = new Date();
    var hrs = dateTime.getHours();
    var min = dateTime.getMinutes();
    var sec = dateTime.getSeconds();;
    document.getElementById('hours').innerHTML = hrs;
    document.getElementById('minutes').innerHTML = min;
    document.getElementById('seconds').innerHTML = sec;
    

}
setInterval(displayTime, 10);