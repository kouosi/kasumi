from .models import db, User, Contact, Message
from random import randint

def addUser(username, status, name):
    user = User(username=username, status=status, name=name, is_active = True if status == "Online" else False)
    if db.session.query(User).filter_by(username=username).count() < 1:
        db.session.add(user)
        db.session.commit()
    else:
        print(f"=> already exist user for {username} not adding")
    return user

def addContact(c_username, username, last_message_sent, is_last_message_seen):
    contact = Contact(
        username=username,
        current_username=c_username,
        last_message_sent=last_message_sent,
        is_last_message_seen=is_last_message_seen
    )
    if db.session.query(Contact).filter_by(username=username).count() < 1:
        db.session.add(contact)
        db.session.commit()
    else:
        print(f"=> already exist contacts for {username} not adding")
    return contact

    sender_username = db.Column(db.String(80), nullable=False)
    receiver_username = db.Column(db.String(80), db.ForeignKey(
        "user.username"), nullable=False)
def addMessage(username, rusername, message):
    contact = Message(
        message_id=randint(1, 2<<32),
        sender_username = username,
        receiver_username = rusername,
        message=message,
    )
    db.session.add(contact)
    db.session.commit()

def test():
    alish = addUser("alish", "Offline", "Alish Chaulagain")
    kouosi = addUser("kouosi", "Busy", "Kouosi Tsuamine")
    pawan = addUser("pawan", "Online", "Pawan Shrestha")
    sushant = addUser("sushant", "Online", "Sushant Mdhr")
    suyesh = addUser("suyesh", "Online", "Suyesh Nuchan")
    vipran = addUser("vipran", "Offline","Vipran Dahal")

    addContact(kouosi.username, pawan.username, "How are you pawan", True)
    addContact(kouosi.username, alish.username, "How are you alish", True)

    # for i in range(1,300):
    #     if(i%2==0):
    #         addMessage(pawan.username, kouosi.username, str(randint(1, 10000))*4)
    #     else:
    #         addMessage(kouosi.username, pawan.username, str(randint(1,10000))*5)
