//register an event listener - find that eleement id (myA) and addan event listener - in this case click
//when inline it's onclick when in an event listener it's click
//one event per listener
//click it the event itself. can be other things, like submit
//after the click is what to do after click the function to call
document.getElementById("myA").addEventListener("click", stopLink);


//event part can be whatever we want it to be. we call it event so we know when we read it
//that it is the event we're looking at
function stopLink(event){
    let confirmed = confirm("are you sure")
    if (confirmed){
        console.log("off we go")
    } else{   
    event.preventDefault();
    console.log("Button Clicked");
    }
}
//another way to do it is via an anonymous inline function
//document.getElementById("myA").addEventListener("click", function(event){event.preventDefault();});