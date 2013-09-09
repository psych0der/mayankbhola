$(document).ready(function(){

var str=location.href.slice(0,-1).toLowerCase().split('/').pop();


$(".navbar li a").each(function() {
	//alert(this.href.slice(0,-1).toLowerCase().split('/').pop());
if (str.indexOf(this.href.slice(0,-1).toLowerCase().split('/').pop()) > -1) {
$("li.highlight").removeClass("highlight");
$(this).parent().addClass("highlight");

}

$("li.highlight").parents().each(function(){

if ($(this).is("li")){
$(this).addClass("highlight");
}


});


});



});