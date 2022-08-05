import pygame
from tkinter import *
      #filedialog from tkinter : has open and save dialog functions
      #askdirectory from filedialog : presents user with pop up to choose directory
from tkinter.filedialog import askdirectory
import os

musicplayer=Tk()
musicplayer.title("My Music Player")
musicplayer.geometry("+450+350")

directory=askdirectory()
os.chdir(directory)       #changes current directory.It has single argument as new directory path.
songlist=os.listdir()     #returns a list containing the names of the entries in the directory given by path
                          #tkinter Listbox function to create a list of songs 
playlist=Listbox(musicplayer,font="Helvetica 12 bold",bg="yellow",selectmode=SINGLE)
                          #inserting songs in playlist->Listbox
for item in songlist:
      pos=0
      playlist.insert(pos,item)
      pos=pos+1

pygame.init()          #initialising pygame module
pygame.mixer.init()    #pygame.mixer moule is used to load and play sounds.This method need to be initialised

           #function to play song
def play():
      pygame.mixer.music.load(playlist.get(ACTIVE))   #loads the selected song from playlist
      var.set(playlist.get(ACTIVE))                   #sets song title at the top of music-player
      pygame.mixer.music.play()

           #function to stop song
def ExitMusicPlayer():
      pygame.mixer.music.stop()

           #function to pause song
def pause():
      pygame.mixer.music.pause()

           #function to unpause song
def unpause():
      pygame.mixer.music.unpause()

        #buttons for play,stop,pause and unpause
button1=Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="PLAY",bg="red",fg="white",command=play)
button2=Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="STOP",bg="purple",fg="white",command=ExitMusicPlayer)
button3=Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="PAUSE",bg="green",fg="white",command=pause)
button4=Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="UNPAUSE",bg="blue",fg="white",command=unpause)

var=StringVar()
songtitle=Label(musicplayer,textvariable=var,font="Helvetica 12 bold")

songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
playlist.pack(fill="both",expand="True")

musicplayer.mainloop()