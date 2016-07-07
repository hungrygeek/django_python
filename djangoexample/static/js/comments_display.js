


$(document).ready(function(){
	
	$("[comment_button]").click(function(event){
		var hidcform = $("#cgrouphform")
		hidcform.insertAfter(event.target)
		//hidcform.show();
		hidcform.slideDown();
		
		hidcform.find("#id_parent").attr("value", event.target.attributes.getNamedItem("comment_button").nodeValue)
	});
});