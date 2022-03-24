# Mnemonic phrase generator by _Gnifajio_ ![]() ![]() ![](https://badgen.net/badge/release/v1.0/grey)

_Простой класс для генерации мнемонической фразы_

#### Установка

[]()

```sh
git clone https://github.com/gnifajio/mnemonic_phrase_generator.git
pip install -r requirements.txt
```

#### Использование

[]()

```python
from seed_generator import Mnemonic
mnem = Mnemonic()
phrase = mnem.generate()
address = mnem.get_address(phrase)
```

##### Синтаксис

[]()

```python
mnem = Mnemonic(word_count=12)
```

> `word_count` - количество слов в фразе.

```python
address = mnem.get_address(phrase, derivation_path='44/60/0/0')
```

> `derivation_path` - путь деривации.

#### TODO
- Добавить функцию для генерации мнемонической фразы напрямую из энтропии.
- Добавить больше языков для генирации фразы.
- Добавить автонономность.