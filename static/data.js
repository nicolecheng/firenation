// Initialization
var station_list = document.getElementById("list_station");

var result = [];
// Data Retrieval - By Year
var get_data = function(year) {
    var ret;
    $.ajax({
	url: '/data/' + year,
	dataType: 'json',
	async: false,
	success: function(data){
	    result = data.result;
	    console.log(result);
	}
    });
    return result;
};

/***
var add(){
   dic = get_data(2017);
   for station in dic{
       display = document.createElement("div");
       display.id = station;
       display.addEventListener("click", geter);
   }
}

var geter = function(){
      dic = get_data(2017);
      trains = dic[this.id];
      for train in trains{
         info = document.createElement();
      }
   }
}

***/


//shows the data (popularity of the genre) accroding to year using divs as bar graph
var data_years = function(year) {
  while (data.lastChild){
        data.removeChild(data.lastChild);
    }

  var graph = d3.select("#data");
    graph.selectAll("div")
        .data(info)
        .enter()
        .append("div")
        .style("width", "200px")
        .style("height", function(d) {
           return d * 5 + "px";
        })
         .style("background-color", function(d,i) {
           return colors[i];
         })
         .text( function(d, i) {
            return text[i] + " " + info[i] + "%";
         });
};

var changedate = function(e) {
    e.preventDefault();

    var target = yearw / 2; // Target X Coordinate
    var deltax = target - e.target.getAttribute("x");
    // console.log(target); // Debugging
    // console.log(deltax); // Debugging

    for (i = 0; i < years.length; i++) {
	years[i].setAttribute("x", parseInt(years[i].getAttribute("x")) + deltax);
    }

    // ADD DATA BINDING HERE
    data_years(e.target.innerHTML);
    console.log(e.target.innerHTML);

};

for (i = 1997; i < 2018; i++) {
    var t = document.createElementNS(ns, "text");
    t.setAttribute("x", x);
    t.setAttribute("y", y);
    t.setAttribute("font-family", "Quicksand");
    t.setAttribute("font-size", "36px");
    t.setAttribute("text-anchor", "middle");
    t.setAttribute("fill", "Black");
    t.textContent = String(i);
    year.appendChild(t);
    years.push(t);
    t.addEventListener("click", changedate);
    x += 125;
}
data_years('1997');

console.log("Loaded js.");
