var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("navig").style.top = "0";
    } else {
        document.getElementById("navig").style.top = "-60px";
    }
    prevScrollpos = currentScrollPos;
}