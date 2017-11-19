$(document).click(function () {
    var audioElement = document.createElement('audio');
    audioElement.setAttribute('src', '../static/concreteandgoldalbum/01. T-Shirt.mp3');

    audioElement.addEventListener('ended', function() {
        this.play();
    }, false);


    $('#play').click(function() {
        audioElement.play();
        $("#status".text("Status: Playing");
                });
});
