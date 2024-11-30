### Hanafuda Game Overview

> With AI generation

Hanafuda is a traditional Japanese card game played with a deck of 48 cards, divided into 12 suits, each representing a month of the year. Each suit has four cards, and the goal is to form specific card combinations to score points.

### Basic Rules

1. **Deck Composition**: 12 suits, each with 4 cards.
2. **Card Types**:
   - **Brights (20 points)**: 🌕
   - **Animals (10 points)**: 🐦
   - **Ribbons (5 points)**: 🎀
   - **Chaff (1 point)**: 🍂
3. **Gameplay**:
   - Players draw and play cards to form combinations.
   - Points are scored based on the combinations formed.
4. **Winning**: The player with the highest points at the end of the game wins.

### Implementation Plan

1. **Define Card and Deck Classes**:
   - Create a `Card` class to represent individual cards.
   - Create a `Deck` class to manage the deck of cards.

2. **Initialize the Game**:
   - Shuffle the deck and deal cards to players.

3. **Gameplay Loop**:
   - Players take turns drawing and playing cards.
   - Check for combinations and update scores.

4. **Scoring System**:
   - Implement a scoring system based on the card combinations.

5. **End Game**:
   - Determine the winner based on the scores.
