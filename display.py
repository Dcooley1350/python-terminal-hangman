def display_game_status(status):
    word = ""
    for n in range(len(status)):
        word += status[n]
        if n < len(status):
            word += " "
    print(word)