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

function animate(i)
                {
                    
                    if(i<91)
                    {
						$('#web').val(parseInt(i)).trigger('change');
						$('#php').val(parseInt(i)).trigger('change');
                    }

                    if(i<86)
                    {
						$('#c').val(parseInt(i)).trigger('change');
						
                    }

                    if(i<89)
                    {
						$('#py').val(parseInt(i)).trigger('change');
					
                    }

                    if(i<81)
                    {
						$('#shell').val(parseInt(i)).trigger('change');
					
                    }
				}

                 
                 function animateKnob(i)
                 {
                   
                   animate(i);
                    
                     if(i<100)
                    {
                      var t=  setTimeout(animateKnob,4,i+1);
                    }

				}

              

$(".hello").lettering();

var controller = $.superscrollorama({
			playoutAnimations: true
});
controller.addTween('#action1', TweenMax.from( $('#action1'), .6, {css:{opacity: 0}}));
controller.addTween('#fade', TweenMax.from( $('#fade'), .6, {css:{opacity: 0}}));
controller.addTween('#fade1', TweenMax.from( $('#fade1'), .6, {css:{opacity: 0}}));
controller.addTween('#fade2', TweenMax.from( $('#fade2'), .6, {css:{opacity: 0}}));
controller.addTween('#fade3', TweenMax.from( $('#fade3'), .6, {css:{opacity: 0}}));

controller.addTween('#aka', TweenMax.from( $('#aka'), .10, {css:{opacity:0}, ease:Quad.easeInOut}));

controller.addTween('#mayank', TweenMax.from( $('#mayank'), .25, {css:{right:'2000px'}, ease:Quad.easeInOut}));
controller.addTween('#bhola', TweenMax.from( $('#bhola'), .25, {css:{left:'3000px'}, ease:Quad.easeInOut}));

controller.addTween('#action2', TweenMax.from( $('#action2'), .10, {css:{fontSize:'3px'}, ease:Quad.easeInOut}));
controller.addTween('#action3', TweenMax.from( $('#action3'), .10, {css:{opacity:0}, ease:Quad.easeInOut}));

controller.addTween('#action4', TweenMax.from( $('#action4'), .25, {css:{right:'2000px'}, ease:Quad.easeInOut}));
controller.addTween('#action5', TweenMax.from( $('#action5'), .25, {css:{left:'3000px'}, ease:Quad.easeInOut}));

controller.addTween('#action6', TweenMax.fromTo( $('#action6'), .30, {css:{opacity:0, 'letter-spacing':'80px'}, immediateRender:true, ease:Quad.easeInOut}, {css:{opacity:1, 'letter-spacing':'14px'}, ease:Quad.easeInOut}), 0, 100);
controller.addTween('#action7', TweenMax.fromTo( $('#action7'), .25, {css:{opacity:0, fontSize:'20px'}, immediateRender:true, ease:Quad.easeInOut}, {css:{opacity:1, fontSize:'2.1em'}, ease:Quad.easeInOut}));
controller.addTween('#action8', TweenMax.from( $('#action8'), .30, {css:{opacity:0,rotation:720,right:'2000px'}, ease:Quad.easeInOut}));
controller.addTween('#action9', TweenMax.from( $('#action9'), .6, {css:{opacity: 0}}));

controller.addTween('#action10', TweenMax.fromTo( $('#action10'), .25, {css:{opacity:0, fontSize:'20px'}, immediateRender:true, ease:Quad.easeInOut}, {css:{opacity:1, fontSize:'2.1em'}, ease:Quad.easeInOut}));
controller.addTween('#action11', TweenMax.from( $('#action11'), .30, {css:{opacity:0,rotation:720,right:'2000px'}, ease:Quad.easeInOut}));
controller.addTween('#action12', TweenMax.from( $('#action12'), .6, {css:{opacity: 0}}));
controller.addTween('#action13', TweenMax.from( $('#action13'), .25, {css:{left:'3000px'}, ease:Quad.easeInOut}));


controller.addTween('#action14', TweenMax.from( $('#action14'), .25, {css:{right:'2000px'}, ease:Quad.easeInOut}));
controller.addTween('#action15', TweenMax.from( $('#action15'), .25, {css:{left:'3000px'}, ease:Quad.easeInOut}));

controller.addTween('#action16', TweenMax.fromTo( $('#action16'), .30, {css:{opacity:0, 'letter-spacing':'90px'}, immediateRender:true, ease:Quad.easeInOut}, {css:{opacity:1, 'letter-spacing':'3px'}, ease:Quad.easeInOut}), 0, 100);
controller.addTween('#action17', TweenMax.fromTo( $('#action17'), .25, {css:{opacity:0, fontSize:'20px'}, immediateRender:true, ease:Quad.easeInOut}, {css:{opacity:1, fontSize:'1.2em'}, ease:Quad.easeInOut}));

controller.addTween('#social2', TweenMax.from( $('#social2'), .20, {css:{fontSize:'1px'}, ease:Quad.easeInOut}));

controller.addTween('#skills', TweenMax.from($('#skills'), .30, {css:{opacity:0, fontSize:'20px'}, ease:Bounce.easeOut, onComplete : function(){

animateKnob(0);
}}));



 $(".knob").knob();


});
