## AI and Difficulty in Go Fish
#### Author: Layla A.

This document is designed to outline the various stages of AI difficulty that the minigame bot will offer for go fish. This is achieved through improvements in decision making as higher difficulty levels are chosen.

### Easy (Level 1)

An Easy level bot will do little more than blindly pick cards with no additional logic to its behavior. It will not actively seek out potential matches and it will not make informed guesses based on previous turns.

This difficulty level can be compared to playing Go Fish against a young child and is not meant to pose a significant challenge.

Easy (Level 1) logic will flow as follows:

1. AI will examine the unique card values in their hand and create an option set.

2. AI will randomly pick a value from this option set and ask the User for this card.

### Normal (Level 2)

The Normal level of difficulty will introduce informed decision making logic by weighting guesses based on its own hand in addition to looking back at previous turns. The bot will assemble a weighted option space based on scoring the efficacy of its potential moves and select from the best options.

This level will, however, also feature several limitations to this process to distinguish it from a Hard (Level 3) bot, which include:

* Only using the most recent N turns for assessing game state.

* Randomize its selection from the top N weighted options.

* Temporarily revert back to Easy (Level 1) logic when the last move resulted in a correct guess.

This difficulty level can be compared to playing Go Fish against an average young adult with an understanding of the rules, but little in terms of reliable experience with making optimal guesses.

Normal (Level 2) logic will flow as follows:

1. AI will examine the card values in their hand and assemble an option space of guesses where multiple cards of the same value are favored with a higher starting score.

2. AI will look through the past N turns of guesses and modify option space scores based on the probability of a card being in the User's hand. Probability in this context is calculated based on the amount of times a user has drawn since the last guess of this value. An additional (much heavier) layer of weighting is applied onto cards that the User has guessed but has not yet matched.

3. AI will sort the option space based on efficacy scoring and then randomly select between the top N guesses.

4. If the guess is correct, the AI will temporarily switch its difficulty level to Easy (Level 1) for the subsequent guess.