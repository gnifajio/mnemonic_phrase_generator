# Mnemonic phrase generator by _Gnifajio_ ![]() ![]() ![](https://badgen.net/badge/release/v1.0/grey)

_A simple class for generating mnemonic phrases_

#### Installation

[]()

```sh
git clone https://github.com/gnifajio/mnemonic_phrase_generator.git
pip install -r requirements.txt
```

#### Usage

[]()

```python
from seed_generator import Mnemonic
mnem = Mnemonic()
phrase = mnem.generate()
address = mnem.get_address(phrase)
```

##### Syntax

[]()

```python
mnem = Mnemonic(word_count=12)
```

> `word_count` - number of words in a phrase

```python
address = mnem.get_address(phrase, derivation_path='44/60/0/0')
```

> `derivation_path` - derivation_path.


#### TODO

- Add a conversion system from a mnemonic phrase to a btc address.
- Add a function to generate a mnemonic phrase directly from entropy.
- Add more languages for phrase generation.
- Add autonymy.