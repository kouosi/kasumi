/* Toggle signin and signup*/
function toggleInUp() {
    let signin = document.getElementById("signin") // default one
    let signup = document.getElementById("signup")

    if (signin.style.display != "none") {
        signin.style.display = "none"
        signup.style.display = "block"
    } else {
        signin.style.display = "block"
        signup.style.display = "none"
    }
}

function notImplemented() {
    alert("Not Implemented")
}
