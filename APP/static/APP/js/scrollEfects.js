
// init controller
var controller = new ScrollMagic.Controller();

new ScrollMagic.Scene({
    triggerElement: "#row",
    offset: 50,
    triggerHook: 0.9,
})
    .setClassToggle("#row", "visible")
    .addTo(controller);



new ScrollMagic.Scene({
    triggerElement: "#gatillo",
    offset: 50,
    triggerHook: 0.9,
})
    .setClassToggle("#gatillo", "visible")
    .addTo(controller);



new ScrollMagic.Scene({
    triggerElement: "#animales",
    offset: 50,
    triggerHook: 0.9,
})
    .setClassToggle("#animales", "visible")
    .addTo(controller);

