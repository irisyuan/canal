$("#student-start").click(function() {
		$("#start-apply").hide();
		$("#landing-caption").hide();
		$("#student-apply").css({'display':'table'});


});

function clickHandler(e){
    e = e || window.event;
    $("#student-identify").hide();
    var elements = document.getElementsByClassName('student-choose');
    for(var i = 0; i < elements.length; i++){
        elements[i].style.display = 'none'; // Hide all elements.
    }

    e.target.style.display = 'inline'; // Show the clicked element.
    
}