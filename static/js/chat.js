const user_search = document.querySelector('.user-search-container');
const user_search_box = document.getElementById('user-search-box');
const user_search_result = document.getElementById('user-search-results');
const user_search_close = document.getElementById('user-search-close');

const username = getCookie("username")
const session_id = getCookie("session")

/* Fetch Contact List */
getContactList()

user_search_box.addEventListener('input', function() {
    let query = this.value;
    if (query.length === 0) { user_search_result.innerHTML = ''; return; }

    fetch(`/search?q=${query}`)
        .then(response => response.json())
        .then(data => {
            constructHtmlOFSearchBox(data);
        });
});

/* Handle cookies */
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function deleteAllCookies() {
    document.cookie.split(';').forEach(cookie => {
        const eqPos = cookie.indexOf('=');
        const name = eqPos > -1 ? cookie.substring(0, eqPos) : cookie;
        document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:00 GMT';
    });
}

/* Check Json error */
function checkError(root_data) {
    if (!root_data.success) {
        alert(root_data.message);
        if (root_data.tohome) {
            deleteAllCookies();
            window.location.href = "/"
        }
    }
}

/* Construct out chat info*/
function constructHtmlOFSearchBox(data) {
    user_search_result.innerHTML = '';
    data.users.forEach(item => {
        user_search_result.innerHTML += `
            <div class="result-item user-search" data-username="${item.username}">
                <img class="profile" src="/static/profiles/${item.profile}">
                <div class="description">
                    <div class="name">${item.name}</div>
                    <div class="about">${item.about}</div>
                </div>
            </div>
        `; /* template end */

        document.querySelectorAll('.result-item').forEach(item => {
            item.addEventListener('click', handleNewMsg);
        });
    });
}

/* Construct our left contact list from json */
function constructHtmlOfContactList(root_data) {
    checkError(root_data);

    const contact_list_div = document.getElementById("contact-list");
    const main_profile_div = document.getElementById("my-profile");

    main_profile_div.innerHTML = `
        <div class="profile">
            <img src="/static/profiles/${root_data.profile_pic}" alt="profile">
        </div>
        <div class="info">
            <div class="left">
                <div class="name">${root_data.display_name}</div>
                <div class="status">${root_data.status}</div>
            </div>
            <div id="new-message-btn" onclick="showUserSearch()" class="right">
                <i class="fa-solid fa-plus"></i>
            </div>
        </div>
    `; /* End of template */

    if (root_data.contact.length != 0) {
        contact_list_div.innerHTML = ""
    }

    /* Render each contact list items */
    root_data.contact.forEach(function(contact) {
        contact_list_div.innerHTML += `
            <div class="contact-info ${contact.is_active ? 'online' : ''}"
                onclick="getMessage('${contact.username}')">
                <div class="profile">
                    <img src="/static/profiles/${contact.profile_pic}" alt="profile">
                </div>
                <div class="info">
                    <div class="name">${contact.display_name}</div>
                    <div class="last-message">
                        <div class="text">${contact.last_message_sent}</div>
                        <div class="time">${contact.last_seen_time}</div>
                    </div>
                </div>
            </div>
        `; /* End of template */
    })
}

/* Construct Chat from json */
function constructHtmlOfChatSample(data) {
    const contactList = document.getElementById("chat-content");
    const mainchat_window = document.getElementById("chat-title");
    const username = data.username;

    mainchat_window.className = "chat-title";
    mainchat_window.innerHTML = ""
    contactList.innerHTML = ""

    if (data.is_active) {
        mainchat_window.className += " online";
    }
    const userProfileDiv = document.createElement("div");
    userProfileDiv.className = "profile"

    const userProfileImg = document.createElement("img");
    userProfileImg.src = "https://i.pinimg.com/736x/bc/b6/10/bcb6102adfa68b562a96413551e8ea86.jpg";
    userProfileImg.alt = data.username;
    userProfileDiv.appendChild(userProfileImg)

    const userNameDiv = document.createElement("div");
    userNameDiv.className = "title";
    userNameDiv.innerHTML = `${data.name}<div class="last-active">${data.last_online_time}</div>`;

    mainchat_window.appendChild(userProfileDiv);
    mainchat_window.appendChild(userNameDiv);

    data.message.forEach(function(data) {
        const contactInfoDiv = document.createElement("div");
        if (username == data.username) {
            contactInfoDiv.className = "chat-text chat-right";
        } else {
            contactInfoDiv.className = "chat-text chat-left";
        }
        contactInfoDiv.innerHTML = data.message;
        contactList.appendChild(contactInfoDiv);
    })
}

/* Update chat scroll to bottom */
function updateChatScroll() {
    const chatContainer = document.getElementById("chat-content");
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

/* Show user search box */
function showUserSearch() {
    user_search.style.display = "block"
}

/* Show user search box */
function hideUserSearch() {
    user_search.style.display = "none";
    user_search_box.value = "";
    user_search_result.innerHTML = "";
}

/* Handle New user search click event */
function handleNewMsg(event) {
    hideUserSearch();
    let username1 = event.currentTarget.getAttribute('data-username')
    fetch('/api/newmsg', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            username: username,
            new_username: username1,
            session_id: session_id
        })
    }).then(e => e.json())
        .then(e => {
            checkError(e);
            getContactList()
        })
        .catch(e => console.error("Error fetching JSON:", e))
}

/* Get Contact List */
function getContactList() {
    fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: username, session_id: session_id })
    }).then(e => e.json()).then(e => {
        constructHtmlOfContactList(e)
    }).catch(e => console.error("Error fetching JSON:", e))
}

/* Get Message for user */
function getMessage(secondary_username) {
    fetch('/api/message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            primary_username: username,
            secondary_username: secondary_username,
            session_id: session_id
        })
    }).then(e => e.json()).then(e => {
        constructHtmlOfChatSample(e)
    }).catch(e => console.error("Error fetching JSON:", e))
    updateChatScroll();
}

user_search_close.addEventListener("click", () => {
    hideUserSearch();
})

// let debounceTimeout;
// function debounce(fn, delay = 500) {
//     return function(...args) {
//         clearTimeout(debounceTimeout);
//         debounceTimeout = setTimeout(() => { fn.apply(this, args); }, delay);
//     };
// }
//
// const processInput = debounce(handleNewMsg, 500);
// document.addEventListener('DOMContentLoaded', () => {
//     user_search_box.addEventListener('input', debounce(handleNewMsg, 500));
// })
