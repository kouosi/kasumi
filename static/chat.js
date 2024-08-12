function constructHtmlOfContactList(data) {
    const contactList = document.getElementById("contact-list");

    const myProfileDiv = document.getElementById("my-profile");
    myProfileDiv.innerHTML = "";

    const titleProfileDiv = document.createElement("div");
    titleProfileDiv.className = "profile";

    const titleImg = document.createElement("img");
    titleImg.src = "https://i.pinimg.com/736x/bc/b6/10/bcb6102adfa68b562a96413551e8ea86.jpg";
    titleImg.alt = data.name;
    titleProfileDiv.appendChild(titleImg);

    const titleInfoDiv = document.createElement("div");
    titleInfoDiv.className = "info";

    const titleNameDiv = document.createElement("div");
    titleNameDiv.className = "name";
    titleNameDiv.textContent = data.name;
    titleInfoDiv.appendChild(titleNameDiv);

    const titleStatusDiv = document.createElement("div");
    titleStatusDiv.className = "status";
    titleStatusDiv.textContent = data.status;
    titleInfoDiv.appendChild(titleStatusDiv);
    myProfileDiv.appendChild(titleProfileDiv);
    myProfileDiv.appendChild(titleInfoDiv);

    data.contact.forEach(function(data) {
        const contactInfoDiv = document.createElement("div");
        contactInfoDiv.className = `contact-info ${data.is_active ? 'online' : 'offline'}`;
        contactInfoDiv.addEventListener("click", function() {
            getMessage(data.username)
        });

        const profileDiv = document.createElement("div");
        profileDiv.className = "profile";

        const img = document.createElement("img");
        // img.src = "/avatars/" + data.username;
        img.src = "https://i.pinimg.com/736x/bc/b6/10/bcb6102adfa68b562a96413551e8ea86.jpg";
        img.alt = data.name;
        profileDiv.appendChild(img);

        const infoDiv = document.createElement("div");
        infoDiv.className = "info";

        const nameDiv = document.createElement("div");
        nameDiv.className = "name";
        nameDiv.textContent = data.name;
        infoDiv.appendChild(nameDiv);

        const lastMessageDiv = document.createElement("div");
        lastMessageDiv.className = "last-message";

        const textDiv = document.createElement("div");
        textDiv.className = "text";
        textDiv.textContent = data.last_message_sent;
        lastMessageDiv.appendChild(textDiv);

        const timeDiv = document.createElement("div");
        timeDiv.className = "time";
        timeDiv.textContent = data.last_seen_time;
        lastMessageDiv.appendChild(timeDiv);

        infoDiv.appendChild(lastMessageDiv);
        contactInfoDiv.appendChild(profileDiv);
        contactInfoDiv.appendChild(infoDiv);
        contactList.appendChild(contactInfoDiv);
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

function updateChatScroll() {
    const chatContainer = document.getElementById("chat-content");
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

fetch("/api/contact_list/kouosi").then(e => e.json()).then(e => {
    constructHtmlOfContactList(e)
}).catch(e => console.error("Error fetching JSON:", e))

function getMessage(user) {
    fetch(`/api/chat_message/${user}/kouosi`).then(e => e.json()).then(e => {
        constructHtmlOfChatSample(e)
    }).catch(e => console.error("Error fetching JSON:", e))
    updateChatScroll();
}
