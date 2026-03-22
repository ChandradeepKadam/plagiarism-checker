function highlight(line, words) {
    words.forEach(word => {
        let regex = new RegExp(`\\b${word}\\b`, "gi");
        line = line.replace(regex, `<span class="highlight">${word}</span>`);
    });
    return line;
}

async function checkPlagiarism() {
    let f1 = document.getElementById("file1").files[0];
    let f2 = document.getElementById("file2").files[0];

    if (!f1 || !f2) {
        alert("Upload both files");
        return;
    }

    let form = new FormData();
    form.append("file1", f1);
    form.append("file2", f2);

    let res = await fetch("http://127.0.0.1:5000/compare", {
        method: "POST",
        body: form
    });

    let data = await res.json();

    document.getElementById("overall").innerText =
        "Overall Similarity: " + data.overall_similarity + "%";

    let left = "";
    let right = "";

    data.matches.forEach(m => {
        left += `<div>${highlight(m.line1, m.common_words)}</div>`;
        right += `<div>${highlight(m.line2, m.common_words)}</div>`;
    });

    document.getElementById("left").innerHTML = left;
    document.getElementById("right").innerHTML = right;
}