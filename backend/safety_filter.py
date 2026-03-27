def is_safe(prompt):
    banned_words = ["hack", "steal", "password", "attack"]

    for word in banned_words:
        if word in prompt.lower():
            return False

    return True