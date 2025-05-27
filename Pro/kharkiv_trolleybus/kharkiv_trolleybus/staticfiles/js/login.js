function circle() {
    var canvas = document.getElementById('circle');
    var objCanvas = canvas.getContext('2d');
    objCanvas.beginPath();
    objCanvas.arc(150, 75, 50, 0, 2 * Math.PI, false);
    objCanvas.fillstyle = "white";
    objCanvas.fill();
    objCanvas.LineWidth = 1;
    objCanvas.strokeStyle = "green";
    objCanvas.stroke();
}

circle();