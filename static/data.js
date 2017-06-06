// Initialization
var station_list = document.getElementsByClassName("station");
var train_name = document.getElementById("train_name").value
var result = [];
// Data Retrieval
var get_data = function(station_id) {
    $.ajax({
    	url: '/data/' + train_name + "/" + station_id + "/",
    	dataType: 'json',
    	async: false,
    	success: function(data){
    	    result = data.result;
          append_data(result, station_id);
        },
      error: function(data){
    	    result = data.result;
          append_data(result, station_id);
        },
      });
};

var add_node = function(list, element) {
  var node = document.createElement("li");
  node.className = "list-group-item";
  node.innerHTML = '<b>' + list[4] + '</b> train from ' + list[2] + '<br><span class="label label-default">' + (Math.round(list[1] * 100)/100).toString() + ' mi away <span class="glyphicon glyphicon-road"></span></span>';
  node.innerHTML += '  <span class="label label-default">' + Math.round(parseInt(list[0])).toString() + ' min <span class="glyphicon glyphicon-time"></span></span>';
  element.appendChild(node);
};

var append_data = function(data, station_id) {
  // console.log(station_id);
  // console.log(station_id.split("_").join(" "));
  // console.log(data);
  var list_trains = data[station_id.split("_").join(" ")];
  var element = document.getElementById(station_id).children[1].children[0];

  var length = (list_trains.length > 14)? 14 : list_trains.length;

  for( var i = 0; i < length; i++ ) {
      if (list_trains[i][3] == "uptown") {
          add_node(list_trains[i], element.children[0]);
      }
      else if (list_trains[i][3] == "downtown") {
          add_node(list_trains[i], element.children[1]);
      }
  }

};

var update_info = function(e) {
  var station_id;
  // console.log(e.target);

  if (e.target.tagName.toLowerCase() != "li") {
    station_id = e.target.parentElement.id;
  }
  else {
    station_id = e.target.id;
  }
  // console.log(station_id);

  var element = document.getElementById(station_id).children[1].children[0];
  while (element.children[0].children.length > 1) {
    element.children[0].removeChild(element.children[0].lastChild);
  }
  while (element.children[1].children.length > 1) {
    element.children[1].removeChild(element.children[1].lastChild);
  }

   get_data(station_id);
};

for( var i = 0; i < station_list.length; i++ ) {
  // console.log(station_list[i].id);
  document.getElementById(station_list[i].id).addEventListener("click", update_info);
}
