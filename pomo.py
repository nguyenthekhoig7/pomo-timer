import tkinter as tk
import time
import pygame

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer App")
        self.master.geometry("300x150")

        self.time_entry = tk.Entry(self.master, font=("Helvetica", 20))
        self.time_entry.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_button.pack(side="right", padx=10)

        self.timer_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.timer_label.pack(pady=10)

        self.is_running = False
        self.remaining_time = 0

    def convert_time_str_to_seconds(self, time_str): # mm:ss --> ss
        if ':' in time_str:
            minutes, seconds = map(int, time_str.split(":"))
            total_seconds = minutes * 60 + seconds
        else:
            total_seconds = int(time_str)
        return total_seconds

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
            self.remaining_time = int(self.convert_time_str_to_seconds(self.time_entry.get()))    
            # self.remaining_time = int(self.time_entry.get())
            self.do_countdown()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")

    def do_countdown(self):
        if self.remaining_time <= 0:
            self.timer_label.config(text="Time's up!")
            self.play_sound()
            self.is_running = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
        else:
            self.timer_label.config(text=str(self.remaining_time))
            self.remaining_time -= 1
            self.master.after(1000, self.do_countdown)

    def play_sound(self):
        # Replace "path/to/sound/file.wav" with the actual path to your sound file
        pygame.init()
        pygame.mixer.Sound("data/wind_chimes.mp3").play()

root = tk.Tk()
app = TimerApp(root)
root.mainloop()