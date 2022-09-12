## Description

Alice and Bob are communicating through a encrypted channel. To be more secure they exchange keys first and then exchange messages. Cam you crack the message to find out the flag.

## Short explanation

- The challenge focuses on Diffie Hellman key exchange.(**MITM**)
- Alice sends her public key to Bob.
- Attacker intecepts and send his own public key to Bob.
- Bob sends his public key to Alice.
- Attacker intercepts and sends his own public key to Alice.
- Bob calculates secret with attacker's public key and xor's the flag with the secret and sends to Alice.
- Attackers calculates secret by using Bob's public and xor's the message to get the flag.
