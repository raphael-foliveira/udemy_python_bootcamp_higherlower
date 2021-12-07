from art import logo, vs
from game_data import data
from random import choice


def choose_random_item() -> dict:
    new_item: dict = choice(data)
    data.remove(new_item)
    if len(data) > 1:
        return new_item
    else:
        print(f"No more data to play! You beat the game!")
        print("Do you want to play again?")
        play_again(input("(y)es or (n)o: "))


def compare_followers(item_a: dict, item_b: dict):
    if item_a['follower_count'] > item_b['follower_count']:
        return item_a
    elif item_a['follower_count'] < item_b['follower_count']:
        return item_b


def check_answer(player_choice, winner_item):
    if player_choice == winner_item:
        return True
    else:
        return False


def play_again(answer):
    if answer.lower() == "y":
        play(choose_random_item(), choose_random_item(), 0)
    else:
        exit(0)


def play(itema, itemb, player_score):
    print(logo)
    print(f"A: {itema['name']}, {itema['description']} from {itema['country']},"
          f" has {itema['follower_count']} followers on instagram.")
    print(vs)
    print(f"B: {itemb['name']}, {itemb['description']} from {itemb['country']}.")

    winner = compare_followers(itema, itemb)

    print("Who do you think has the most followers?")
    player_input = input("(a) or (b): ")
    if player_input == "a":
        player_input = itema
    elif player_input == 'b':
        player_input = itemb

    print(f"B: {itemb['name']} has {itemb['follower_count']} followers on instagram.")

    if check_answer(player_input, winner):
        print((50 * "\n") + "Correct answer!")
        new_player_score = player_score + 1
        print(f"Current score: {new_player_score}")
        new_itema = winner
        new_itemb = choose_random_item()
        play(new_itema, new_itemb, new_player_score)
    else:
        print("You lose!")
        print(f"You scored: {player_score}")
        print("Do you want to try again?")
        play_again(input("(y)es or (n)o: "))


play(choose_random_item(), choose_random_item(), 0)





