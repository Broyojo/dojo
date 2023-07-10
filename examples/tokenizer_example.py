import dojo

tok = dojo.CharacterTokenizer()

tokens = tok.encode("hello!")
text = tok.decode(tokens)

print(tokens)
print(text)

print(tok.vocab)
