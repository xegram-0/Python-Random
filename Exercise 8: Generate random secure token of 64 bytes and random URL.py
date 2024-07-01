# Exercise 8: Generate random secure token of 64 bytes and random URL



import secrets
# token_hex vs token_bytes???
print(f"The secret token is {secrets.token_bytes(64)}")
print(f"The secret URL is {secrets.token_urlsafe(64)}")
