import tkinter as tk
from tkinter import ttk
from collections import Counter, defaultdict

class WordFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Finder")
        self.root.geometry("600x500")
        
        # Load dictionary
        self.dictionary_by_length = defaultdict(list)
        with open("words.txt", "r") as f:
            for word in f:
                word = word.strip().lower()
                self.dictionary_by_length[len(word)].append(word)
        
        # Create UI
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = ttk.Label(self.root, text="Word Finder", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Input frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(padx=10, pady=10, fill="x")
        
        ttk.Label(input_frame, text="Enter letters:").pack(side="left", padx=5)
        self.letters_entry = ttk.Entry(input_frame, width=30, font=("Arial", 12))
        self.letters_entry.pack(side="left", padx=5, fill="x", expand=True)
        self.letters_entry.bind("<Return>", lambda e: self.search())
        
        # Minimum length frame
        length_frame = ttk.Frame(self.root)
        length_frame.pack(padx=10, pady=5, fill="x")
        
        ttk.Label(length_frame, text="Minimum word length:").pack(side="left", padx=5)
        self.min_length_var = tk.IntVar(value=6)
        self.min_length_spin = ttk.Spinbox(
            length_frame, 
            from_=2, 
            to=20, 
            textvariable=self.min_length_var, 
            width=5
        )
        self.min_length_spin.pack(side="left", padx=5)
        
        # Search button
        self.search_btn = ttk.Button(self.root, text="Search", command=self.search)
        self.search_btn.pack(pady=10)
        
        # Results frame
        results_frame = ttk.LabelFrame(self.root, text="Results", padding=10)
        results_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Results text widget with scrollbar
        scrollbar = ttk.Scrollbar(results_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.results_text = tk.Text(
            results_frame, 
            height=20, 
            width=70, 
            yscrollcommand=scrollbar.set,
            font=("Courier", 10)
        )
        self.results_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.results_text.yview)
    
    def search(self):
        self.results_text.delete("1.0", "end")
        
        letters = self.letters_entry.get().lower().strip()
        min_length = self.min_length_var.get()
        
        if not letters:
            self.results_text.insert("end", "Please enter some letters.")
            return
        
        letter_count = Counter(letters)
        found_any = False
        
        # Search from longest to minimum
        for length in range(len(letters), min_length - 1, -1):
            found_words = []
            
            for word in self.dictionary_by_length[length]:
                word_count = Counter(word)
                if all(word_count[char] <= letter_count[char] for char in word_count):
                    found_words.append(word)
            
            if found_words:
                found_any = True
                self.results_text.insert("end", f"Words with {length} letters:\n")
                for word in sorted(found_words):
                    self.results_text.insert("end", f"  {word}\n")
                self.results_text.insert("end", "\n")
        
        if not found_any:
            self.results_text.insert("end", "No valid words found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordFinderApp(root)
    root.mainloop()
