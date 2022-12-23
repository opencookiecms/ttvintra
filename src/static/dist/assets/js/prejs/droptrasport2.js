"use strict";
function RemoveDnone() {
    const flightmode = document.getElementById("flightmodeselect");
    const dnone = document.getElementById("yarn");

    if (flightmode.classList.contains('active')) {
        dnone.classList.add('d-none');
    } else {
        dnone.classList.remove('d-none');
      
    }
   
    console.log("yes");
}

function AddDnone() {
    const ccarmode = document.getElementById("ccartmodeselect");
    const selfcarmode = document.getElementById("selfcarmodeselect");
    const busmode =  document.getElementById("busmodeselect");
    const trainmode = document.getElementById("trainmodeselect");
    const dnone = document.getElementById("yarn");

    if (ccarmode.classList.contains('active')) {
        dnone.classList.remove('d-none');
   
    } 
    if (selfcarmode.classList.contains('active')) {
        dnone.classList.add('d-none');
   
    } 
    else {
        dnone.classList.add('d-none');
      
    }
   
    console.log("yes");
}




