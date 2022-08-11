"use strict";
function ShowHotelDivYes() {
    var chkYes = document.getElementById("chkYes");
    var lug = document.getElementById("hotels");
    lug.style.display = chkYes.checked ? "block" : "block";
    night.value = '';
    console.log("yes");
}

function ShowHotelDivNo() {
    
    var chkNo = document.getElementById("chkNo")
    var lug = document.getElementById("hotels");
    var night = document.getElementById("id_numbernights");
    lug.style.display = chkNo.checked ? "none":"none";
    night.value = 0;
    
    console.log("jot");
}
