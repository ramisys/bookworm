# 📚 Bookworm Word Finder

A beginner-friendly Python word generator inspired by **Bookworm Adventures Deluxe**. Enter a jumble of letters and the app searches a dictionary text file to find every valid word that can be built from those letters.

## ✨ Description

Bookworm Word Finder is a small desktop application built with **Python** and **Tkinter**. It accepts a set of letters from the user, compares them against a dictionary file, and displays all valid words that can be formed.

The results are grouped by word length so it is easy to spot the longest possible word first.

## 🚀 Features

- Generate valid words from a jumble of letters
- Find the longest possible word first
- Filter results by minimum word length
- Sort words alphabetically within each length group
- Load words from a plain text dictionary file
- Simple desktop interface with no extra setup required

## 🧠 How It Works

1. The program reads every word from `words.txt`.
2. Each word is stored by its length for faster lookup.
3. When you enter letters, the app counts how many times each letter appears.
4. It compares those counts against the dictionary words.
5. Any word that can be built from the available letters is shown in the results panel.
6. Results are displayed from the longest words down to the minimum length you choose.

## 🛠 Requirements

- Python 3.8 or newer
- Tkinter (usually included with standard Python installations)
- A dictionary text file named `words.txt`

### Dictionary Source

The bundled `words.txt` file comes from the [dwyl/english-words](https://github.com/dwyl/english-words) repository.

## 📦 Installation

1. Clone or download this repository.
2. Make sure `app.py` and `words.txt` are in the same folder.
3. Confirm that Python is installed on your computer.

```bash
python --version
```

4. Run the application.

```bash
python app.py
```

## ▶️ Usage

1. Launch the app.
2. Type your jumbled letters into the input box.
3. Set the minimum word length if needed.
4. Click **Search** or press **Enter**.
5. Review the matching words in the results area.

Example input:

```text
letters: aelrts
minimum length: 4
```

## 🖥 Example Output

```text
Words with 6 letters:
  alerts
  alters
  artels
  laster
  ratels
  salter

Words with 5 letters:
  alert
  rates
```

Your results will depend on the letters you enter and the contents of `words.txt`.

## 🗂 Project Structure

```text
bookworm/
├── app.py       # Tkinter application and word search logic
├── words.txt    # Dictionary word list
└── README.md    # Project documentation
```

## 🔮 Future Improvements

- Add support for custom dictionary files
- Highlight the single longest word automatically
- Ignore duplicate words in the dictionary
- Add crossword-style hint mode
- Package the app as a standalone executable
- Improve the interface with modern styling

## 📄 License

This project is intended for educational and personal use.

If you plan to publish or share it publicly, add a license such as the **MIT License** and include a `LICENSE` file in the repository.