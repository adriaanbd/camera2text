var position = []

var canvas = document.getElementById('canvas'),
    ctx = canvas.getContext('2d'),
    rect = {},
    drag = false;


function init() {
    imageObj = new Image();
    imageObj.onload = function () { ctx.drawImage(imageObj, 0, 0,500,500); };
    imageObj.src = './static/dog-cat.png';
    canvas.addEventListener('mousedown', mouseDown, false);
    canvas.addEventListener('mouseup', mouseUp, false);
    canvas.addEventListener('mousemove', mouseMove, false);
}

function mouseDown(e) {
    rect.startX = e.pageX - this.offsetLeft;
    rect.startY = e.pageY - this.offsetTop;
    drag = true;
}

function mouseUp() {
    drag = false;
    console.log(position)
}

function mouseMove(e) {
    if (drag) {
      rect.w = (e.pageX - this.offsetLeft) - rect.startX;
      rect.h = (e.pageY - this.offsetTop) - rect.startY ;
      ctx.clearRect(0,0,canvas.width,canvas.height);
      ctx.drawImage(imageObj, 0, 0,500,500);
      position = draw();
    }
}

function draw() {
    ctx.beginPath();
    ctx.rect(rect.startX, rect.startY, rect.w, rect.h);
    ctx.strokeStyle = 'blue';
    ctx.lineWidth = 3;
    ctx.stroke();
    return [rect.startX, rect.startY, rect.w, rect.h];
}




init();
console.log(position);
