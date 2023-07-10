from abc import abstractmethod, ABC


class Tokenizer(ABC):
    """
    An abstract tokenizer class

    A minimal tokenizer has:
    - a vocabulary: a mapping from token to id

    A minimal tokenizer can:
    - encode text
    - decode tokens
    """

    def __init__(self):
        pass

    @property
    @abstractmethod
    def vocab(self) -> dict[str, int]:
        pass

    @abstractmethod
    def encode(self, text: str) -> list[int]:
        pass

    @abstractmethod
    def decode(self, tokens: list[int]) -> str:
        pass


class CharacterTokenizer(Tokenizer):
    def __init__(self):
        pass

    @property
    def vocab(self) -> dict[str, int]:
        return {chr(i): i for i in range(128)}

    def encode(self, text: str) -> list[int]:
        return [ord(c) for c in text]

    def decode(self, tokens: list[int]) -> str:
        return "".join(chr(t) for t in tokens)
