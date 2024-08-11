# Our Api documentation

## For contact list
- `username` : username is a unique id for both database and user it can be alphabet and number must be lowercase with no space
- `is_active` : It is the active status of user if it user is accive it will return true else false
- `name` : name is user name that shows on contact list and message and can be every valid unicode 
- `last_seen_time` : Last seen time is a time where user opened the chat window it may be in mins hour days week 
- `is_last_message_seen` : It is a seen status of last message seen it returns true if last message is seen else false
- `last_message_sent` : It is a last message send by either side of user

### Example
```json
{
    "username": "suyesh",
    "is_active": true,
    "name": "Suyesh Nuchan",
    "last_seen_time": "1h",
    "is_last_message_seen": true,
    "last_message_sent": "My project is done"
}
```

## For chat window
- `is_active` : It is the active status of user if it user is accive it will return true else false
- `name` : name is user name that shows on contact list and message and can be every valid unicode 
- `last_online_time` : Last online time is a time where user was online it may be in mins hour days week 
- `last_seen_id` : It is a id of message that the another user has seen so far it must be valid id
- `message` : It is a array of messages with `message` property

### message property
- `username`: message sender unique id
- `message_id`: the id of message 
- `messsage`: it is a message sent by user that can be text, url or file with `nuchan` encoding

### nuchan encoding
`nuchan` encoding is a encoding used for message encoding where we represent with text for text with semiclon: for link is it is link and for file it is file

### Example
```json
{
    "username": "suyesh",
    "is_active": true,
    "name": "Suyesh Nuchan",
    "last_online_time": "1h",
    "last_seen_id": 23445,
    "message": [
        {"username": "inogen", "id": "ldkfj", "message": "text: HIelskldfj url=>https://suyesh.com text"},
    ]
}
```
