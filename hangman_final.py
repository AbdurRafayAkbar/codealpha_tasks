import random
words_list=[
    "Python",
    "Elephant",
    "Galaxy",
    "Wizard",
    "Football",
    "Chocolate",
    "Butterfly",
    "Sunshine",
    "Adventure",
    "Mountain",
    "Rainbow",
    "Castle",
    "Dolphin",
    "Unicorn",
    "Dragon",
    "Vacation",
    "Volcano",
    "Hurricane"
]
selected_word=random.choice(words_list)
guessed_word=["_"]*len(selected_word)

final_guess=""
attempts=6
while attempts>0:
    print(" ".join(guessed_word))
    user_guess=input("Guess a letter : ").lower()
    if user_guess in final_guess:
        print("Already guessed the letter. Try Again")

    elif user_guess in selected_word:
        final_guess+=user_guess
        for index,letter in enumerate(selected_word):
            if letter==user_guess:
                guessed_word[index]=user_guess  
    elif "_" not in guessed_word:
        print("Congatulations you have found the word ")
    

    else:
        print("The letter",user_guess," is not in the word")
        attempts-=1
        print("attempts remaining = ",attempts)
else:
    print("The word was ",selected_word)
    print("Game Over")