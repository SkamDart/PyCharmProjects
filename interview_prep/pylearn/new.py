s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

from collections import defaultdict

def findRepeatedDnaSequences(s):
    n = len(s) - 9
    repeated_sequences = defaultdict(int)

    for i in range(n):
        repeated_sequences[s[i:i + 10]] += 1

    return list(map(lambda x: x[0], filter(lambda x: x[1] > 1, repeated_sequences.items())))

def find_repeated_dna_sequences(s):
    n = len(s) - 9
    repeated_sequences = defaultdict(int)

    for i in range(n):
        seq_slice = slice(i, i + 10)
        seq = s[seq_slice]
        repeated_sequences[seq] += 1

    return [seq for seq, frequency in repeated_sequences.items() if frequency > 1]

def superpow(a, b):
    """
    https://leetcode.com/problems/super-pow/
    :param a:
    :param b:
    :return:
    """
    if a % 1337 == 0:
        return 0
    else:
        return a ** (int(''.join([str(i) for i in b]))) % 1337

print(superpow(2, [3]))
print(superpow(2, [1, 0]))
