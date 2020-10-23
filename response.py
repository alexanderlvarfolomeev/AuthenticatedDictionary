from hashlib import sha256
from typing import Union


def hash_fun(x: bytes, y: bytes) -> bytes:
    return sha256(bytes(min(x, y) + max(x, y))).digest()


class AuthenticResponse:
    def __init__(self, timestamp: bytes, item, proof, result: bool):
        self.timestamp = timestamp
        self.item = item
        self.proof = proof
        self.result = result

    def subject_contained(self):
        return self.result

    def validates_against(self, timestamp: Union[bytes, None] = None):
        if timestamp is None:
            timestamp = self.timestamp
        acc = bytes(self.proof[0])
        for value in self.proof[1:]:
            acc = hash_fun(acc, bytes(value))
        return timestamp == acc
