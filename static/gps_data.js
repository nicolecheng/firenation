// Initialization
var station_list = document.getElementsByClassName("station");
var train_name = document.getElementById("train_name").value
var result = [];
// Data Retrieval
var get_data = function(station_id) {
    $.ajax({
    	url: '/data/' + station_id + "/",
    	dataType: 'json',
    	async: false,
    	success: function(data){
    	    result = data.result;
    	    //console.log(result);
	       }
       });

    return result;
};

var add_node = function(list, element) {
  var node = document.createElement("li");
  node.innerHTML = list[4] + ' train from ' + list[2] + '. <span class="label label-default">' + (Math.round(list[1] * 100)/100).toString() + ' mi away <span class="glyphicon glyphicon-road"></span></span> ';
  node.innerHTML += '<span class="label label-default">' + Math.round(parseInt(list[0])).toString() + ' min <span class="glyphicon glyphicon-time"></span></span>';
  element.appendChild(node);
};

var append_data = function(data, station_id) {
  var list_trains = data[station_id];
  var element = document.getElementById(station_id).children[1].children[0];

  for( var i = 0; i < list_trains.length; i++ ) {
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

   append_data(get_data(station_id), station_id);
};

for( var i = 0; i < station_list.length; i++ ) {
  // console.log(station_list[i].id);
  document.getElementById(station_list[i].id).addEventListener("click", update_info);
}
