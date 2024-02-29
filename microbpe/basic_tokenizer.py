
from utils import merge_until_vocab_size, get_bytes, get_byte_pair_freqs, merge_byte_pairs
class BasicTokenizer():
  def __init__(self) -> None:
    self.merges = {}
    self.vocab_size = 255

  def train(self, text, vocab_size, verbose=False):
    bytes = get_bytes(text)
    _, merges =  merge_until_vocab_size(bytes, vocab_size)
    self.merges = merges
    self.vocab_size = vocab_size

  def encode(self, text):
    bytes = get_bytes(text)
    freqs = get_byte_pair_freqs(bytes)
    while True:
      most_common_pair = max(freqs, key=freqs.get)
      if most_common_pair not in self.merges:
        return bytes
      bytes = merge_byte_pairs(bytes, most_common_pair, self.merges[most_common_pair])
      freqs = get_byte_pair_freqs(bytes)

  def decode(self, ids):
    pass