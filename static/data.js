// Initialization
var station_list = document.getElementsByClassName("station");

var result = [];
// Data Retrieval
var get_data = function(station) {

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

for( var i = 0; i < station_list.length; i++ ) {
  console.log(station_list[i].id);

}
