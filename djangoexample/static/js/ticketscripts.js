function onTicketScriptSubmit(form)
{
	
}




Dropzone.options.ticketFileUpload = 
	{
		init: function() {
			document.getElementById('id_autofiles').value = ""
		    this.on("complete",function(file,response){
		    	
				
			});
		    this.on("success",function(file,response)
		    		{
		    	
		    	var returned = JSON.parse(response);
		    
				var t =  document.getElementById('ticket-add')
				a = document.getElementById('id_autofiles');
				a.value += returned['uid'];
				a.value += ","
		  });
		}
	}