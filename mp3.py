import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x500")
canvas.config(bg = 'black')

rootpath = "C:\\Users\lenovo\Desktop\mp3"
pattern = "*.mp3"

mixer.init()

def select():
    label.config(text = listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def play_next():
    next_song = listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def play_prev():
    next_song = listbox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":
         mixer.music.pause()
         pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"
    
listbox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100, font = ('ds-digital', 14))
listbox.pack(padx = 16, pady = 16)

label = tk.Label(canvas, text = '', bg = 'black', fg = 'cyan', font = ('ds-digital', 18))
label.pack(pady = 16)

top = tk.Label(canvas, bg = "black")
top.pack(padx = 16, pady = 16, anchor = 'center')

prevButton = tk.Button(canvas, text = "Prev", command = play_prev) 
prevButton.pack(pady = 16, in_ = top, side = 'left')

stopButton = tk.Button(canvas, text = "Stop", command = stop)
stopButton.pack(pady = 16, in_ = top, side = 'left', )

playButton = tk.Button(canvas, text = "Play", command = select)
playButton.pack(pady = 16, in_ = top, side = 'left')

pauseButton = tk.Button(canvas, text = "Pause", command = pause_song)
pauseButton.pack(pady = 16, in_ = top, side = 'left')

nextButton = tk.Button(canvas, text = "Next", command = play_next)
nextButton.pack(pady = 16, in_ = top, side = 'left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert('end', filename)


canvas.mainloop()