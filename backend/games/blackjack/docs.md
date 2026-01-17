# Blackjack

This is a simplified Blackjack implementation.

Core mechanics:
1. A shuffled 52-card deck is created.
2. Player and dealer each receive two cards.
3. Player may “Hit” (draw a card) or “Stand”.
4. When the player stands, the dealer draws until reaching at least 17.
5. Hand values follow standard Blackjack rules:
   - Number cards = face value
   - J, Q, K = 10
   - Ace = 1 or 11 (whichever is better)

The game state is stored in-memory on the backend for simplicity.
