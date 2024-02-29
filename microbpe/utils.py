def get_bytes(text):
  return list(map(int, text.encode("utf-8")))

def get_byte_pair_freqs(bytes):
  n = len(bytes)

  ptr_1 = 0
  ptr_2 = 1

  freqs = {}
  while ptr_2 < n:
    pair = (bytes[ptr_1], bytes[ptr_2])
    freqs[pair] = freqs.get(pair, 0) + 1
    ptr_1 += 1
    ptr_2 += 1
  return freqs

def merge_byte_pairs(bytes, pair, new_id):
  n = len(bytes)

  ptr_1 = 0
  ptr_2 = 1

  new_bytes = []
  while ptr_2 < n:
    curr_pair = (bytes[ptr_1], bytes[ptr_2])
    if curr_pair == pair:
      new_bytes.append(new_id)
      ptr_1 += 2
      ptr_2 += 2
    else:
      new_bytes.append(bytes[ptr_1])
      ptr_1 += 1
      ptr_2 += 1
  new_bytes.append(bytes[ptr_1])
  return new_bytes

def merge_until_vocab_size(bytes, vocab_size):
  merges = {}

  starting_id = 256
  num_merges = vocab_size - starting_id
  curr_id = starting_id
  merged_bytes = bytes
  freqs = get_byte_pair_freqs(merged_bytes)
  while num_merges > 0:
    most_common_pair = max(freqs, key=freqs.get)
    merged_bytes = merge_byte_pairs(merged_bytes, most_common_pair, curr_id)
    merges[most_common_pair] = curr_id

    freqs = get_byte_pair_freqs(merged_bytes)
    curr_id += 1
    num_merges -= 1
  return merged_bytes, merges