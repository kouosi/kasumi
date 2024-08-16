const login_btn = document.getElementById("login-btn");
const signup_btn = document.getElementById("signup-btn");
const reset_btn = document.getElementById("reset-btn");
const errbox = document.getElementById("form-errbox")

if (login_btn) {
    login_btn.addEventListener('click', function(event) {
        event.preventDefault();

        const email = document.getElementById("form-email").value;
        const password = document.getElementById("form-password").value;
        const password_hash = CryptoJS.SHA256(password).toString();

        fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, password_hash: password_hash })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                window.location.href = "/";
            } else {
                errbox.innerHTML = data.error;
                errbox.style.display = "block";
            }
        }).catch(error => console.error('Error:', error));
    });
}

if (signup_btn) {
    signup_btn.addEventListener('click', function(event) {
        event.preventDefault();

        const name = document.getElementById("form-name").value;
        const username = document.getElementById("form-username").value;
        const email = document.getElementById("form-email").value;
        const password = document.getElementById("form-password").value;
        const password_hash = CryptoJS.SHA256(password).toString();

        fetch('/api/signup', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: name, email: email, username: username, password_hash: password_hash })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                window.location.href = "/";
            } else {
                errbox.innerHTML = data.error;
                errbox.style.display = "block";
            }
        }).catch(error => console.error('Error:', error));
    });
}

if (reset_btn) {
    reset_btn.addEventListener('click', function(event) {
        event.preventDefault();

        const email = document.getElementById("form-email").value;
        const username = document.getElementById("form-username").value;

        fetch('/api/reset', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, username: username })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                // Redirect to dashboard or show success message
            } else {
                errbox.innerHTML = data.error;
                errbox.style.display = "block";
            }
        }).catch(error => console.error('Error:', error));
    });
}

localStorage.setItem('theme','dark');

function changeTheme() {
    const pds = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const stv = localStorage.getItem('theme');

    if (stv==='auto' || !stv) {
        document.documentElement.classList.toggle("light-mode", !pds);
        return 'auto'
    } else {
        document.documentElement.classList.toggle("light-mode", stv!=='dark');
        localStorage.setItem('theme', (stv!=='dark') ? 'dark' : 'light');
        return (stv!=='dark') ? 'dark' : 'light'
    }
}
changeTheme()

document.getElementById("toggle-theme").addEventListener('click', () => {
    localStorage.setItem('theme', changeTheme());
});
