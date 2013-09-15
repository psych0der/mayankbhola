$(document).ready(function(){

/*var str=location.href.slice(0,-1).toLowerCase().split('/').pop();
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
});*/

$(".hello").lettering();

var controller = $.superscrollorama({
			playoutAnimations: true
});
controller.addTween('#action1', TweenMax.from( $('#action1'), .6, {css:{opacity: 0}}));

controller.addTween('#action2', TweenMax.from( $('#action2'), .10, {css:{fontSize:'3px'}, ease:Quad.easeInOut}));
controller.addTween('#action3', TweenMax.from( $('#action3'), .10, {css:{opacity:0}, ease:Quad.easeInOut}));

controller.addTween('#action4', TweenMax.from( $('#action4'), .25, {css:{right:'2000px'}, ease:Quad.easeInOut}));
controller.addTween('#action5', TweenMax.from( $('#action5'), .25, {css:{left:'3000px'}, ease:Quad.easeInOut}));

controller.addTween('#action6', TweenMax.fromTo( $('#action6'), .30, {css:{opacity:0, 'letter-spacing':'80px'}, immediateRender:true, ease:Quad.easeInOut}, {css:{opacity:1, 'letter-spacing':'14px'}, ease:Quad.easeInOut}), 0, 100);
controller.addTween('#action7', TweenMax.fromTo( $('#action7'), .25, {css:{opacity:0, fontSize:'20px'}, immediateRender:true, ease:Quad.easeInOut}, {css:{opacity:1, fontSize:'2.1em'}, ease:Quad.easeInOut}));
controller.addTween('#action8', TweenMax.from( $('#action8'), .30, {css:{opacity:0,'-moz-transform':'rotate(720deg)','-webkit-transform': 'rotate(720deg)','-o-transform': 'rotate(720deg)',
                '-ms-transform':'rotate(720deg)',right:'2000px'}, ease:Quad.easeInOut}));
controller.addTween('#action9', TweenMax.from( $('#action9'), .6, {css:{opacity: 0}}));

});
