# Caesar Cipher

The Caesar cipher is a classic substitution cipher where each letter
is shifted forward or backward in the alphabet by a fixed number of positions.

How this implementation works:
1. The alphabet is defined as A–Z.
2. Each letter in the message is shifted by a numeric key.
3. Encryption shifts forward; decryption shifts backward.
4. Non-letter characters (spaces, punctuation, numbers) remain unchanged.
5. In "Hacker Mode", the system tries all 26 possible keys.
