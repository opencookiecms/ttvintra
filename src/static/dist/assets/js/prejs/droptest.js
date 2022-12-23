"use strict";
function ShowHideDiv() {
    var chkYes = document.getElementById("chkYes");
    var lug = document.getElementById("lug");
    lug.style.display = chkYes.checked ? "block" : "none";
}
