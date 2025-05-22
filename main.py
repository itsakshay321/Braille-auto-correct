
import tkinter as tk
from tkinter import messagebox

# Mapping of QWERTY keys to Braille dots
QWERTY_TO_BRAILLE_INDEX = {'D': 0, 'W': 1, 'Q': 2, 'K': 3, 'O': 4, 'P': 5}

# Sample Braille dictionary (add more as needed)
BRAILLE_DICTIONARY = {
    'a': '100000',
    'b': '101000',
    'c': '110000',
    'd': '110100',
    'e': '100100',
    'f': '111000',
    'g': '111100',
    'h': '101100',
    'i': '011000',
    'j': '011100',
    'k': '100010',
    'l': '101010',
    'm': '110010',
    'n': '110110',
    'o': '100110',
    'p': '111010',
    'q': '111110',
    'r': '101110',
    's': '011010',
    't': '011110',
    'u': '100011',
    'v': '101011',
    'w': '011101',
    'x': '110011',
    'y': '110111',
    'z': '100111'
}

# Sample words for suggestion
SAMPLE_WORDS = ['cat', 'bat', 'rat', 'hello', 'world', 'code', 'braille']

def convert_to_braille_pattern(pressed_keys):
    pattern = ['0'] * 6
    for key in pressed_keys.upper():
        if key in QWERTY_TO_BRAILLE_INDEX:
            pattern[QWERTY_TO_BRAILLE_INDEX[key]] = '1'
    return ''.join(pattern)

def convert_word_to_braille_sequence(word):
    return [BRAILLE_DICTIONARY.get(letter, '000000') for letter in word.lower()]

def calculate_edit_distance(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    dp = [[0]*(len2+1) for _ in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[len1][len2]

def suggest_closest_word(user_input):
    input_sequence = convert_word_to_braille_sequence(user_input)
    best_match = None
    smallest_distance = float('inf')
    for word in SAMPLE_WORDS:
        word_sequence = convert_word_to_braille_sequence(word)
        distance = calculate_edit_distance(input_sequence, word_sequence)
        if distance < smallest_distance:
            smallest_distance = distance
            best_match = word
    return best_match

def on_submit():
    user_input = entry_input.get()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a word.")
        return
    suggestion = suggest_closest_word(user_input)
    label_result.config(text=f"Suggestion: {suggestion}")

# GUI Setup
window = tk.Tk()
window.title("Braille Auto-Correct System")

frame = tk.Frame(window, padx=20, pady=20)
frame.pack()

label_title = tk.Label(frame, text="Enter Braille Word (QWERTY Format):", font=("Arial", 12))
label_title.pack()

entry_input = tk.Entry(frame, font=("Arial", 12), width=30)
entry_input.pack(pady=10)

btn_submit = tk.Button(frame, text="Suggest Word", command=on_submit, font=("Arial", 12))
btn_submit.pack(pady=5)

label_result = tk.Label(frame, text="", font=("Arial", 14), fg="blue")
label_result.pack(pady=10)

window.mainloop()
