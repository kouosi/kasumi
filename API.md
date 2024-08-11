# Our Api documentation

## For contact list
- `username` : It is a unique id for both database and user. It must start with alphabet and can contain both alphabet or number from second. It must be lower case with no space.
- `status`: It is the status that user set it must be less than 16 characters
- `name`: It is the name of current user that is logged in to.
- `contact`: It is the array of `contact info property` which gives contact list

### contact info property
- `username` : It is a unique id for both database and user. It must start with alphabet and can contain both alphabet or number from second. It must be lower case with no space.
- `is_active` : It is the active status of user if it user is active it will return true else false
- `name` : It is name of user that shows on contact list and message and should be valid Unicode
- `last_seen_time` : It is a time where user opened the chat window. It may be in mins:`m` hour:`h` days:`d` week:`w` and year:`y`
- `is_last_message_seen` : It is seen status of last message sent. It returns true if last message is seen else false
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
- `username`: It is a message sender unique id
- `is_active` : It is the active status of user if user is active it will return true else false
- `name` : It is name of user that shows on contact list and message and should be valid Unicode
- `last_online_time` : It is a time where user was online it may be in mins:`m` hour:`h` days:`d` week:`w` month:`m` and year:`y`
- `last_seen_id` : It is a id of message that the another user has seen so far it must be valid message id
- `message` : It is a array of messages with `message` property

### message property
- `username`: It is a message sender unique id
- `message_id`: It is a unique id of message
- `message`: it is a message sent by user that can be text, URL or file with `Nuchan` encoding

### Nuchan encoding
`Nuchan` encoding is a encoding used for message encoding where we represent with text for text with semicolon: for link is it is link and for file it is file

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
