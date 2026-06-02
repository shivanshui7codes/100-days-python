import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
while wanna_play == "y":
    print("\n" * 100)
    print(logo)
    my_random_cards = random.choices(cards, k=2)
    my_current_score = sum(my_random_cards)
    print(f"Your cards: {my_random_cards}, current score: {my_current_score}")

    comp_random_cards = random.choices(cards, k=2)
    comp_current_score = sum(comp_random_cards)
    print(f"Computer's first card: {comp_random_cards[0]}")


    def final_hand(m_card, m_score, c_card, c_score):
        return f"Your final hand: {m_card}, final score: {m_score}\nComputer's final hand: {c_card}, final score: {c_score}"


    if my_current_score <= 20:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while another_card == "y":
            my_random_cards.append(random.choice(cards))
            my_current_score = sum(my_random_cards)

            if 11 in my_random_cards and my_current_score > 21:
                my_random_cards[my_random_cards.index(11)] = 1
                my_current_score = sum(my_random_cards)
            print(f"Your cards: {my_random_cards}, current score: {my_current_score}")

            if my_current_score > 21:
                print("Busted! You lose!")
                break
            elif my_current_score == 21:
                print("Blackjack! You win!")
                break

            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        else:
            while comp_current_score < 17:
                comp_random_cards.append(random.choice(cards))
                comp_current_score = sum(comp_random_cards)
            print(final_hand(my_random_cards, my_current_score, comp_random_cards, comp_current_score))

            if comp_current_score > 21:
                print("Opponent went over. You win")

            elif comp_current_score == 21:
                print("Opponent got BlackJack! You Lose")

            elif my_current_score > comp_current_score:
                print("You WIN!")

            elif my_current_score < comp_current_score:
                print("You Lose!")

            else:
                print("It's a Draw")


    elif my_current_score == 21:
        print(final_hand(my_random_cards, my_current_score, comp_random_cards, comp_current_score))
        print("You Win")

    else:
        print(final_hand(my_random_cards, my_current_score, comp_random_cards, comp_current_score))
        print("Busted")

    wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
