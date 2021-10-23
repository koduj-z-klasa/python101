$(document).ready(function(){
    $('#contents ul.simple').clone().insertAfter('div.wy-menu ul.current li.current a.current');
    $('div.wy-menu ul.current li.current ul.simple').css('padding-left','3.8em');
    //$('div.wy-menu ul.current li.current ul.simple').css('margin-left','2.5em');
    $('div.wy-menu ul.current li.current ul.simple li').css('list-style-type','disc');
    $('div.wy-menu ul.current li.current ul.simple li a').css('padding-left','0.5em');
    $('div.wy-menu ul.current li.current ul.simple li a').css('margin-left','-0.5em');
    
});

$(document).on('click', 'div.wy-menu ul.current li.current ul.simple li a', function(){
    $('div.wy-menu ul.current li.current ul.simple li a').each(function(){
       $(this).css('background-color','#E3E3E3'); 
    });
    $(this).css('background-color','#c9c9c9');
});
