var fill = 1;

$(document).ready(function(){
	$(".longer").attr('rowspan', "3")

	$('#submit').click(enterData);
});


function enterData(){
	switch ($("#starttime").val()){
		case "8:00a":
			addBox("#eightAMtoeight50");
			break;
		case "9:05a":
			addBox("#nine05tonine55");
			break;
		case "10:10a":
			addBox("#ten10to11");
			break;
		case "11:15a":
			addBox("#eleven15totwelve05");
			break;
		case "12:20p":
			addBox("#twelve20toone10");
			break;
		case "1:25p":
			addBox("#one25totwo15");
			break;
		case "2:30p":
			addBox("#two30tothree20");
			break;
		default:
			addBox("#ten10to11");
			
	}
	
	fill++;
	$("#classname").val("");
	$("#classsec").val("");
	$("#starttime").val("");
	$("#endtime").val("");
	$("#days").val("");
	$("#location").val("");
}

function addBox(row){
	if ($("#days").val() == "Sat")
		$(row+" td.sat").addClass("filled" + fill).html(makeBox());
	else if ($("#days").val() == "Sun")
		$(row+" td.sat").addClass("filled" + fill).html(makeBox());
	else {
		console.log("got here");
		if ($("#days").val().indexOf("M") >= 0) 
			$(row+" td.mon").addClass("filled" + fill).html(makeBox()); 
		if ($("#days").val().indexOf("T") != -1) 
			$(row+" td.tues").addClass("filled" + fill).html(makeBox());
		if ($("#days").val().indexOf("W") != -1) 
			$(row+" td.wed").addClass("filled" + fill).html(makeBox());
		if ($("#days").val().indexOf("R") != -1) 
			$(row+" td.thurs").addClass("filled" + fill).html(makeBox());
		if ($("#days").val().indexOf("F") != -1) 
			$(row+" td.fri").addClass("filled" + fill).html(makeBox());
	}
}

function makeBox(){
	var s = "";
	s += "<h4>" + $("#classname").val() + "</h4>"
	s += "<h5>" + $("#classsec").val() + "</h5>"
	s += "<h6>" + $("#starttime").val() + " - " + $("#endtime").val() + "</h6>"
	s += "<h5>" + $("#location").val() + "</h5>"
	return s;
}