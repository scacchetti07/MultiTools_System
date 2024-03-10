# MultiTools_System
Terminal system with 4 options (Person Register ; Calculator ; Notepad ; MP3 Player) and having your own login System!

# PERSON REGISTER
You can register any people in your space! (is not person's for login page) All of the register will save on a txt archive and you can review all of them any time.
Text box's
1. Name
2. Age
   A check box if the user has social media, if they say is not have, the register will stop and ask the user if they want to save this person. If they say YES, new text box will appears.
   1. Instagram user
   2. Twitter user
   3. Discord user
    And again, the system will ask the user if he want's to save the register.
If the user says, "N" the system will just show all the data tabulate, but if the user says 'S' will show again the tabulate data, but all the data will save on a txt file. 

# Calculator
In the calculator, didn't have anything special, but I add a factorial, sqrt and log calcs in this calculator, The user can's register how many number they want, and use for all the cals, for example:
On the logs fuction, you can choose the number you wants to calculate and choose the base of the log.

# Notepad
Is equals a normal notepad, but is on the terminal. You can edit and remove the file, Create a new txt file too, and all of the data will save on another special folder with you name login on the beginning of the system.

# MP3 Player
 > You can download any music of the Youtube (I use an API (Youte v3 API) to get the ID of the youtube video in base of what the users writes on the input.)
 > The user can create a playlist and edit how many times you want, putting and removing musics, and you can remove them to.
 > The user can view and edit all of the playlist's and choose a song to play (using pygame), inside of the playlist the user choices
 > Finally, you can choose a random song (using pygame) of all the playlist's you create on the system.
Ps: All of the song saves on a special folder with the user's name in a .mp4 file and will converting in the same time to .mp3 using 2 API's. (Pytube and MoviePy)

# Librarys and API's I used
> Os library (used to create the folders and manipulate the txt files)
> psutil library (used to kill the program when the users digit "1010" in the inputs, by a security code)
> Pygame API (used to play the mp3 song on mp3 player)
> Pytube and MoviePy (the first, used to download the youtube videos just audio file for a youtube link. The second, used to convert the pytube files (.mp4) to .mp3 files)
> Youtube v3 API (used to got the ID videos on youtube according wiht user's input.
