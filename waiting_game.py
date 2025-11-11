import time
import random


def waiting_game():
    """ User presses Enter and starts the game.
        He/she is supposed to wait defined amount of time and press Enter again. """

    print('*' * 30)
    print("Welcome to the Waiting Game!")
    print(f"After pressing 'Enter' you need to wait for defined number of seconds and press 'Enter' again.")
    print('*' * 30)

    target_time = random.randint(0, 9)
    print(f"Your target time is {target_time} s.")
    input(" --- Press ENTER to begin --- ")
    start_time = time.time()  # Start time. Better time.perf_counter()
    input(f" .. press Enter again after {target_time} seconds ...")
    user_time = time.time() - start_time
    if abs(user_time - target_time) < 0.1:
        print(f"Congratulations! You won the game! Your time was {user_time:.3f}. Awesome!")
    elif user_time < target_time:
        print(f"Sorry, you were by {target_time-user_time:.3f} too quick. Better luck next time!")
    elif user_time > target_time:
        print(f"Sorry, you were by {user_time - target_time:.3f} too slow. Better luck next time!")


waiting_game()
