<<<<<<< HEAD
# tennis-katas
=======
# Tennis katas

[![PyPI - Version](https://img.shields.io/pypi/v/tennis-katas.svg)](https://pypi.org/project/tennis-katas)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tennis-katas.svg)](https://pypi.org/project/tennis-katas)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install tennis-katas
```

## License

`tennis-katas` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
>>>>>>> a82e82e (first commit)


## Coding smells identified in the original code:

- Long methods (score) -> extracted methods

- Temporary field (tempScore) 

- Switch statements (IFs) -> Replaced switch statements with polymorphism

- Magic numbers (checking the score) -> Replaced this numbers with a class (ScoreSystem) that has a human-readable name(tennis game terms)  explaining the meaning of the number.

## Refactoring:

- Replacing the if-else statements we also follow the Open-Closed principle.

- Breaking the advantage or win to two seperate classes to follow also the Single responsibility principle.

## Minor changes:

- directly "returns" instead of assigning to variable first.