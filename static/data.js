// Initialization
var station_list = document.getElementsByClassName("station");

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

var append_data = function(data, station_id) {
  var element = document.getElementById(station_id);
  var list_trains = data[station_id];

  var uptown_trains = [];
  var downtown_trains = [];

  for( var i = 0; i < list_trains.length; i++ ) {
      if (list_trains[i][3] == "downtown") {
          downtown_trains.push(list_trains[i]);
      }
      else {
          uptown_trains.push(list_trains[i]);
      }
  }


};

for( var i = 0; i < station_list.length; i++ ) {
  console.log(station_list[i].id);

}
