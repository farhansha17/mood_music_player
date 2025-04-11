import tkinter as tk
from tkinter import filedialog, messagebox
import os
import random
import pygame

class MoodMusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Mood-based Music Player")
        self.root.geometry("400x300")

        self.moods = ["Happy", "Sad", "Relaxed", "Energetic"]
        self.music_dirs = {}

        self.create_ui()
        pygame.mixer.init()

    def create_ui(self):
        tk.Label(self.root, text="Select Mood").pack(pady=10)
        self.mood_var = tk.StringVar(value=self.moods[0])
        self.mood_menu = tk.OptionMenu(self.root, self.mood_var, *self.moods)
        self.mood_menu.pack(pady=10)

        tk.Button(self.root, text="Choose Folder for Mood", command=self.choose_folder).pack(pady=10)
        tk.Button(self.root, text="Play Music", command=self.play_music).pack(pady=10)
        tk.Button(self.root, text="Stop Music", command=self.stop_music).pack(pady=10)

    def choose_folder(self):
        selected_mood = self.mood_var.get()
        folder = filedialog.askdirectory()
        if folder:
            self.music_dirs[selected_mood] = folder
            messagebox.showinfo("Success", f"Folder set for {selected_mood} mood.")

    def play_music(self):
        mood = self.mood_var.get()
        folder = self.music_dirs.get(mood)

        if not folder:
            messagebox.showerror("Error", f"No folder set for {mood} mood.")
            return

        songs = [file for file in os.listdir(folder) if file.endswith('.mp3')]

        if not songs:
            messagebox.showerror("Error", "No mp3 files found in the selected folder.")
            return

        selected_song = os.path.join(folder, random.choice(songs))
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()
        messagebox.showinfo("Playing", f"Playing: {os.path.basename(selected_song)}")

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MoodMusicPlayer(root)
    root.mainloop()