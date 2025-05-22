# Braille Autocorrect Web App

This is a web-based autocorrect and suggestion system for Braille input using QWERTY keys. It helps users who type Braille characters via a standard keyboard by offering autocorrection suggestions based on common Braille typing patterns.

## Approach

### QWERTY to Braille Mapping
- Braille dots 1–6 are mapped to QWERTY keys: `D`, `W`, `Q`, `K`, `O`, `P`.
- Each Braille character is represented as a 6-bit binary string (e.g., `101000` for 'b').

### Input Conversion
- User input is converted to a sequence of binary Braille patterns.

### Autocorrect Logic
- Uses **Levenshtein Distance** to compare input against a dictionary of valid words.
- Returns the word with the smallest edit distance (closest match).


## ⚙️ Optimizations

- Levenshtein Distance implemented with dynamic programming for efficiency.
- Modular functions to simplify testing and future extensions.

## Trade-offs

| Decision | Benefit | Trade-off |
|---------|---------|-----------|
| Levenshtein Distance | Good typo handling | Slower for large dictionaries |
| Binary Braille Representation | Simple and efficient | No Grade 2 Braille yet |
| Streamlit | Easy deployment | Requires internet browser |
| No ML | Lightweight | Doesn’t learn user preferences |

##  Future Improvements

- Trie/BK-tree for faster lookups in larger dictionaries.
- Learning from user feedback.
- Accessibility features like speech.


Created as a solution to the **Thinkerbell Labs Braille Autocorrect Task**.
