import random


def game_secret_word():
    is_running = True

    attempt_counter = 0

    user_attempt = 3

    user_points = 0

    secret_words = [
        "cake",
        "milk",
        "cook",
        "fast",
        "cave"
    ]
    secret_word = random.choice(secret_words)

    opened_characters = ""


    user_choose = input("Hello! Choose action!\n 1. Start the game SecretWords\n 2. Quit\n")

    print(secret_word)

    match user_choose:
        case "1":
            while is_running:
                print(f"You HAVE {user_attempt} amount of attempts")

                attempt = input("Okey! Enter A-Z or Secret word\n")

                user_attempt -= 1

                if len(attempt) > 1 and is_running == True:
                    print("You are chiter, you lose! Enter 1 character!")

                if attempt == secret_word:
                    user_points = 50 - user_points
                    is_running = False
                    print(f"You WIM! \n Your points : {user_points} !\n Goodbye!")
                else:
                    attempt_counter += 1

                    for character in secret_word:
                        print("LETTER_ONE_BY_ONE", character)

                        found_index = secret_word.index(character)

                        if attempt == character:
                            user_points += 10
                            print(f"You guessed one character of word! \n"
                                    f"You have {user_points} points\n")

                    if attempt_counter == 3:
                        print(f"You have no attempts. \n"
                              f"You lose, but you have {user_points} points")
                        is_running = False

        case "2":
            print("Goodbye!")
        case _:
            print("Error choose, begin again!")

game_secret_word()