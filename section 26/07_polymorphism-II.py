# ============================================================
# FILE: polymorphism-II.py
# TOPIC: Polymorphism with Subclasses
# ============================================================
# LESSON OBJECTIVES
# 1. Identify common behavior in a superclass.
# 2. Give subclasses different implementations of the same method.
# 3. Use @property for a shared win_ratio calculation.
# 4. Use random.choice() to select an object without checking its type.
# 5. Predict output and complete your own examples.

import random


# ============================================================
# SECTION 1 — POLYMORPHISM AND THE "IS-A" RELATIONSHIP
# ============================================================
# A HumanPlayer IS A Player.
# A ComputerPlayer IS A Player.
# Both have games_played and victories.
# Both can respond to make_move(), but they do so differently.
#
# QUESTION 1:
# What matters more to the calling code: the exact player type,
# or whether the player can respond to make_move()?
# ANSWER:
#


# ============================================================
# SECTION 2 — DEFINE THE SHARED SUPERCLASS
# ============================================================
class Player:
    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories

    @property
    def win_ratio(self):
        return self.victories / self.games_played


# NOTE: For this lesson, assume games_played > 0.
# A zero value would raise ZeroDivisionError; handling that
# is a possible extension after the core exercise.
#
# QUESTION 2:
# If games_played = 30 and victories = 15,
# what does win_ratio return? Is it a percentage from 0 to 100,
# or a fraction from 0 to 1?
# ANSWER:
#


# ============================================================
# SECTION 3 — TWO SUBCLASSES, SAME METHOD NAME
# ============================================================
class HumanPlayer(Player):
    def make_move(self):
        print("Let player make the decision")


class ComputerPlayer(Player):
    def make_move(self):
        print("Run advanced algorithm to calculate best move")


# QUESTION 3:
# Which methods/attributes are inherited from Player?
# Which method is defined separately in each subclass?
# ANSWER:
#


# ============================================================
# SECTION 4 — CREATE SAMPLE PLAYERS
# ============================================================
# Uncomment this section when ready to run the examples.
# hp = HumanPlayer(30, 15)
# cp = ComputerPlayer(1000, 999)
#
# print(hp.win_ratio)
# print(cp.win_ratio)
#
# PREDICT THE TWO OUTPUTS BEFORE RUNNING:
# 1.
# 2.
#
# QUESTION 4:
# Why can both objects use win_ratio even though neither
# subclass defines that property?
# ANSWER:
#


# ============================================================
# SECTION 5 — SAME CALL, DIFFERENT BEHAVIOR
# ============================================================
# Uncomment after creating hp and cp above.
# hp.make_move()
# cp.make_move()
#
# PREDICT OUTPUT:
# 1.
# 2.
#
# EXPLAIN:
# Why does make_move() produce different messages?
# ANSWER:
#


# ============================================================
# SECTION 6 — RANDOMLY SELECT A STARTING PLAYER
# ============================================================
# Uncomment after creating hp and cp above.
# game_players = [hp, cp]
# starting_player = random.choice(game_players)
# starting_player.make_move()
#
# QUESTION 5:
# Can you predict with certainty which message will appear?
# Why does this code work without an if/else checking the type?
# ANSWER:
#


# ============================================================
# SECTION 7 — TRACE THE REFERENCES
# ============================================================
# Suppose random.choice(game_players) selects cp.
#
# game_players --> [hp object, cp object]
# starting_player --> cp object
#
# QUESTION 6:
# Does random.choice() create a brand-new Player object,
# or return a reference to an existing element of the list?
# ANSWER:
#
# If starting_player is cp, which make_move() implementation runs?
# ANSWER:
#


# ============================================================
# SECTION 8 — CODING CHALLENGE 1: ADD A NEW PLAYER TYPE
# ============================================================
# Create a subclass named RemotePlayer(Player).
# Its make_move() method should print:
# "Waiting for the remote player's move"
#
# Then instantiate it with 20 games played and 8 victories.
# Print its win_ratio and call make_move().

class RemotePlayer(Player):
    # Replace pass with your method.
    pass


# YOUR TEST CODE:
#
#
# PREDICTED OUTPUT:
#


# ============================================================
# SECTION 9 — CODING CHALLENGE 2: REUSABLE TURN FUNCTION
# ============================================================
# Write a function play_turn(player) that calls make_move()
# on the supplied object. Do not check the object's class.
#
# Test with HumanPlayer, ComputerPlayer, and RemotePlayer.

def play_turn(player):
    # Replace pass with your implementation.
    pass


# YOUR TEST CODE:
#
# QUESTION 7:
# Why is this an example of polymorphism?
# ANSWER:
#


# ============================================================
# SECTION 10 — CODING CHALLENGE 3: RANDOM MATCH
# ============================================================
# Create a list containing one instance of each player type.
# Use random.choice() to select a player.
# Print the selected player's win_ratio.
# Call play_turn() with the selected player.
#
# BONUS: Repeat the selection five times using a for loop.

def random_match_challenge():
    # Write your code here.
    pass


# Uncomment when finished:
# random_match_challenge()


# ============================================================
# SECTION 11 — FINAL REVIEW
# ============================================================
# Fill in the blanks:
#
# 1. Polymorphism allows different objects to respond to the
#    same ________ call.
# 2. Player is the ________ class.
# 3. HumanPlayer and ComputerPlayer are ________ classes.
# 4. The @property decorator makes win_ratio accessible
#    without writing parentheses: hp.________.
# 5. random.________(game_players) picks one list element.
# 6. The implementation of make_move() depends on the
#    selected object's ________.
# 7. Code that relies on supported behavior rather than
#    exact object types illustrates ________ typing.
#
# KEY TAKEAWAY:
# Player types share data and an interface, while each subclass
# supplies its own implementation of make_move(). Calling code
# can use the same method name without knowing the exact type.
#
# ============================================================
# END OF LESSON
# ============================================================
