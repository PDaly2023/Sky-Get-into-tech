function myFunct2(){
 document.getElementById('demo').innerHTML = `I've changed with funcion2`
} 

function myFunct(){
     document.getElementById('demo').innerHTML = `I've changed with function1`
 }   

//work for conditionals
let age = 44;
if (age <50) {
     console.log("you are too young for our policy");
 } else if (age == 50) {
     console.log(" you can get an earlybird discount");
 } else {
     console.log("you can apply for our policy");
 }

document.getElementById("form1").addEventListener("submit", validation);

function validation(event) {
   
        let box1 = document.getElementById("email").value;
        let box2 = document.getElementById("password").value;
            if (box1.length < 2){
                alert("validation failed false");
                event.preventDefault();
            } else {
                if (box2.length < 2){
                    alert("validation failed false");
                    event.preventDefault();
            } else {
                alert("validation passed true");
            }
    }
}



