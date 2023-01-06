window.addEventListener("load", (e) => {
    let divs = document.querySelectorAll(".typethis");
    divs.forEach((div) => {
        let words = [];
        let wordspans = div.querySelectorAll("span.word");
        let writingdiv = div.querySelector("span.writing");
        wordspans.forEach((wordspan) => words.push(wordspan.innerText));
        div.setAttribute("word", "0");
        div.setAttribute("letter", "0");
        let timeout = 0;
        setInterval(() => {
            writingdiv.removeAttribute("style");
            let word = div.getAttribute("word");
            let letter = div.getAttribute("letter");
            word = parseInt(word);
            letter = parseInt(letter);
            if ((words[word].length - 1) < letter) {
                writingdiv.style.background = "var(--blue)";
                writingdiv.style.borderRadius = "2px";
                letter = 0;
                word = ((words.length == word + 1) ? 0 : word + 1 );
            } else {
                letter += 1;
            }

            if (letter != 0){
                let letters = words[word].substr(0, letter);
                writingdiv.innerHTML = letters;
                let cursor = document.createElement("span");
                cursor.classList = "cursor";
                cursor.innerText = "|";
                cursor.style.color = "var(--oposite-color)";
                writingdiv.appendChild(cursor);
            } else {
                writingdiv.querySelector(".cursor").remove();
            }

            div.setAttribute("word", word.toString());
            div.setAttribute("letter", letter.toString());
        }, 370);
    });
});