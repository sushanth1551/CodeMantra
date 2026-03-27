chat_history = []

def add_to_history(user, bot):
    chat_history.append({"user": user, "bot": bot})

def get_context():
    context = ""
    for chat in chat_history[-5:]:
        context += f"User: {chat['user']}\nBot: {chat['bot']}\n"
    return context