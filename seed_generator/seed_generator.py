from requests import get as rget
import hashlib
import secrets
import binascii


class Mnemonic:
    def __init__(self, word_count=12):
        self.checksum_bit_count = word_count // 3
        total_bit_count = word_count * 11
        self.generated_bit_count = total_bit_count - self.checksum_bit_count
        self.bip39wordlist = rget('https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt').text.strip().split('\n')


    def generate(self):
        entropy = secrets.randbits(self.generated_bit_count)
        entropy = bin(entropy)[2:].zfill(self.generated_bit_count)
        entropy_hash = self.get_hash(entropy)
        indices = self.pick_words(entropy, entropy_hash)
        words = [self.bip39wordlist[indices[i]] for i in range(0, len(indices))]
        word_string = ' '.join(words)
        return word_string


    def pick_words(self, entropy, entropy_hash):
        generated_bit_count = len(entropy)
        generated_char_count = generated_bit_count // 4
        entropy_hex = '0x{0:0{1}x}'.format(int(entropy, 2), generated_char_count)
        checksum_char_count = self.checksum_bit_count // 4
        bit = entropy_hash[0:checksum_char_count]
        check_bit = int(bit, 16)
        checksum = bin(check_bit)[2:].zfill(self.checksum_bit_count)
        source = str(entropy) + str(checksum)
        groups = [source[i:i + 11] for i in range(0, len(source), 11)]
        totalbits = hex(int(str('0b') + entropy + str(checksum), 2))
        indices = [int(str('0b') + source[i:i + 11], 2) for i in range(0, len(source), 11)]
        return indices


    def get_hash(self, entropy):
        generated_bit_count = len(entropy)
        generated_char_count = generated_bit_count // 4
        entropy_hex = '0x{0:0{1}x}'.format(int(entropy, 2), generated_char_count)
        entropy_hex_no_padding = entropy_hex[2:]
        entropy_bytearray = bytearray.fromhex(entropy_hex_no_padding)
        bits = hashlib.sha256(entropy_bytearray).hexdigest()
        return bits
