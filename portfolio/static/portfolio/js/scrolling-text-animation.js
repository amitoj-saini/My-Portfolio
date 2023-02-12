function scrollText(wordcontainers, i) {
    wordcontainers.forEach((wordcontainer) => {
        wordcontainer.style.display = "none";
        wordcontainer.classList = wordcontainer.classList.value.replace(" scroll-text-animation-start scroll-text-animation-end", "");
    });
    i = ((wordcontainers.length <= i) ? 0 : i);
    let wordcontainer = wordcontainers[i];
    wordcontainer.style.display = "inline";
    wordcontainer.classList += " scroll-text-animation-start";
    setTimeout(() => {
        wordcontainer.classList += " scroll-text-animation-end";
        setTimeout(() => scrollText(wordcontainers, i+1), 300);
    }, 2000);
}

window.addEventListener("load", () => {
    let animations = document.querySelectorAll(".scrolling-text-animation");
    animations.forEach((animation) => {
        // initialize animation container (offset is also needed (15px))
        animation.style.position = "relative";
        animation.style.overflow = "hidden";
        animation.style.top = "15px";
        let wordcontainers = animation.querySelectorAll("span");
        scrollText(wordcontainers, 0) // initialize recursive function
    });
});