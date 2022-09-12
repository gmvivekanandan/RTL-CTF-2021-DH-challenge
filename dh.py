import sys

public_g = 5
public_p = 23

sys.stdout.write(f"g:{public_g}\n")
sys.stdout.write(f"p:{public_p}\n")
sys.stdout.flush()

alice_private_key = 4
public_A = pow(public_g, alice_private_key, public_p)
sys.stdout.write(
    f"Send your public message to BOB.Intercepted Alice's message: {public_A}\n")
sys.stdout.flush()
malicious_to_bob = int(input())

bob_private_key = 3
public_B = pow(public_g, bob_private_key, public_p)
sys.stdout.write(
    f"Send your public message to ALICE.Intercepted Bob's message: {public_B}\n")
sys.stdout.flush()
malicious_to_alice = int(input())

secret_2 = pow(malicious_to_bob, bob_private_key, public_p)

flag = "RTL{4c7d928f563796fbe0d5f1d094c348b5}"
enc_flag = [chr(ord(x) ^ secret_2) for x in flag]
sys.stdout.write(
    f"The message is encrypted.Bob sends message:{''.join(enc_flag)}\n")
sys.stdout.flush()
