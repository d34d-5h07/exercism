def response(hey_bob):
    if hey_bob.replace(" ","").endswith("?") and not hey_bob.isupper():
        return "Sure."
    elif hey_bob.isupper() and not hey_bob.endswith("?"):
        return "Whoa, chill out!"
    elif hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!" 
    elif not hey_bob or hey_bob.isspace():
        return "Fine. Be that way!"
    else:
        return "Whatever."