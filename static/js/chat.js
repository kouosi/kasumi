function constructHtmlOfContactList(root_data) {
    const profile_pic = "https://i.pinimg.com/736x/bc/b6/10/bcb6102adfa68b562a96413551e8ea86.jpg";

    const contact_list_div = document.getElementById("contact-list");
    const main_profile_div = document.getElementById("my-profile");

    main_profile_div.innerHTML = `
        <div class="profile">
            <img src="${profile_pic}" alt="profile">
        </div>
        <div class="info">
            <div class="name">${root_data.display_name}</div>
            <div class="status">${root_data.status}</div>
        </div>
    ` /* End of template */

    root_data.contact.forEach(function(contact) {
        contact_list_div.innerHTML = `
            <div class="contact-info selected ${contact.is_active ? 'online' : ''}">
                <div class="profile">
                    <img src="${profile_pic}" alt="profile">
                </div>
                <div class="info">
                    <div class="name">${contact.display_name}</div>
                    <div class="last-message">
                        <div class="text">${contact.last_message_sent}</div>
                        <div class="time">${contact.last_seen_time}</div>
                    </div>
                </div>
            </div>
    ` /* End of template */

        // contactInfoDiv.addEventListener("click", function() {
        //     getMessage(data.username)
        // });
    })
}

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

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function updateChatScroll() {
    const chatContainer = document.getElementById("chat-content");
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

let username = getCookie("username")
let session_id = getCookie("session")

fetch('/api/contact', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username: username, session_id: session_id })
}).then(e => e.json()).then(e => {
    constructHtmlOfContactList(e)
}).catch(e => console.error("Error fetching JSON:", e))

function getMessage(user) {
    fetch(`/api/chat_message/${user}/kouosi`).then(e => e.json()).then(e => {
        constructHtmlOfChatSample(e)
    }).catch(e => console.error("Error fetching JSON:", e))
    updateChatScroll();
}
