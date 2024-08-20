const login_btn = document.getElementById("login-btn");
const signup_btn = document.getElementById("signup-btn");
const reset_btn = document.getElementById("reset-btn");
const errbox = document.getElementById("form-errbox")

if (login_btn) {
    login_btn.addEventListener('click', function(event) {
        event.preventDefault();

        const form = document.getElementById("form");
        if (form.checkValidity()) {
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
                    errbox.innerHTML = data.message;
                    errbox.style.display = "block";
                }
            }).catch(error => console.error('Error:', error));
        } else {
            form.reportValidity();
        }
    });
}

if (signup_btn) {
    signup_btn.addEventListener('click', function(event) {
        event.preventDefault();

        const form = document.getElementById("form");
        if (form.checkValidity()) {
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
                    errbox.innerHTML = data.message;
                    errbox.style.display = "block";
                }
            }).catch(error => console.error('Error:', error));
        } else {
            form.reportValidity();
        }
    });
}

if (reset_btn) {
    reset_btn.addEventListener('click', function(event) {
        event.preventDefault();

        const form = document.getElementById("form");
        if (form.checkValidity()) {
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
                    errbox.innerHTML = data.message;
                    errbox.style.display = "block";
                }
            }).catch(error => console.error('Error:', error));
        } else {
            form.reportValidity();
        }
    });
}

const toggle_theme_btn = document.getElementById("toggle-theme");
function setTheme(isBtn) {
    let current_theme = localStorage.getItem('ui.theme') || 'dark';
    let new_theme = (current_theme === 'dark') ? 'light' : 'dark';
    if (isBtn) {
        document.documentElement.classList.toggle("light-mode", new_theme === 'light');
        localStorage.setItem('ui.theme', new_theme);
    } else {
        document.documentElement.classList.toggle("light-mode", current_theme === 'light');
    }
    let theme_btn_icon = document.querySelector("#toggle-theme .fa-solid");
    theme_btn_icon.classList.toggle("fa-sun", current_theme === 'light');
    theme_btn_icon.classList.toggle("fa-moon", current_theme === 'dark');
    toggle_theme_btn.classList.toggle("clicked", current_theme === 'dark');
}

toggle_theme_btn.addEventListener('click', () => { setTheme(true); });
setTheme(false); // for refresh window
