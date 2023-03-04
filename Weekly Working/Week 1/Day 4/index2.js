document.getElementById('loc').addEventListener('mousedown', mouseEvent, true)

//proving the vent can be whatever
function mouseEvent(e){
    //e again - location of the click
   document.getElementById('out').innerHTML = (`X-co-ordinate ${e.pageX} - Y-co-ordinate ${e.pageY}`)


}
