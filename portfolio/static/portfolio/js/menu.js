window.addEventListener("load", () => {
    let menuicon = document.querySelector("#menuicon");
    let navbar = document.querySelector("#top-bar");
    let menu = document.querySelector("#menu");
    menuicon.setAttribute("menustatus", "closed")
    menuicon.addEventListener("click", () => {
        let menustatus = menuicon.getAttribute("menustatus");
        menustatus = (menustatus == "closed");
        menuicon.setAttribute("menustatus", ((menustatus) ? "opened" : "closed"));
        if (menustatus) {
            // opening menu
            menu.style.display = "block";
            menu.style.animation = "openmenu 1s";
            navbar.style.backgroundColor = "var(--secondary)";
            menuicon.classList = "menu-icon bi bi-x"
        } else {
            // closeing menu
            menu.style.display = "none";
            menu.style.animation = "closemenu 1s";
            navbar.style.backgroundColor = "";
            menuicon.classList = "menu-icon bi bi-list";
        }

    });
});