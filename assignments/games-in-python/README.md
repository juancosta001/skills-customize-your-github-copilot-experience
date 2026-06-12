
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Python Hangman game that uses strings, loops, conditionals, and user input to let players guess a hidden word before they run out of attempts.

## 📝 Tasks

### 🛠️ Create the game engine

#### Description

Write the main Hangman game logic that selects a word randomly and manages the guessing process.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list
- Display the current word state with underscores for unguessed letters
- Allow the player to guess one letter at a time
- Track and display incorrect guesses remaining

### 🛠️ Handle win/lose conditions

#### Description

Add logic to determine when the player wins or loses, and display a clear result message.

#### Requirements
Completed program should:

- End the game when the word is fully guessed
- End the game when the player runs out of allowed guesses
- Show a win message including the secret word when the player guesses correctly
- Show a lose message and reveal the secret word when attempts are exhausted

### 🛠️ Improve player interaction

#### Description

Make the game easy to play by validating input and updating the player on progress after each guess.

#### Requirements
Completed program should:

- Reject invalid input such as multiple letters or non-letter characters
- Prevent repeated guesses from counting against the player
- Display the current progress and list of guessed letters after each turn
- Clearly show how many incorrect guesses remain
