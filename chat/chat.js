function convertJSONToHTML(e) {
    alert("TODO: implement")
}

fetch("/test/chatsample.json").then(e => e.json()).then(e => {
    convertJSONToHTML(e)
}).catch(e => console.error("Error fetching JSON:", e))