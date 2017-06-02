// Initialization

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

var station_list = document.getElementsByClassName("station");

for( var i = 0; i < station_list.length; i++ ) {
  console.log(station_list[i].id);
}
