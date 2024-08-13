import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

class CreateVideoList:
    def __init__(self, window):
        # Initializes an empty playlist
        self.playlist = []

        # Sets the size of the window to 800x350 pixels
        window.geometry("750x400")
        # Sets the title of the window to "Create Video List"
        window.title("Create Video List")

        # Creates a label prompting the user to enter a video number
        enter_lbl = tk.Label(window, text="Enter Video Number:")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="E")

        # Creates an entry widget next to the label
        self.input_txt = tk.Entry(window, width=10)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        # Creates a frame to hold the buttons and center them
        button_frame = tk.Frame(window, bg="#F0F0F0")
        button_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky="N")

        # Creates a button to add a video to the playlist and assigns its callback method
        add_video_btn = tk.Button(button_frame, text="Add Video to Playlist", bg="#FFC1C1", fg="grey", command=self.add_video_clicked)
        add_video_btn.grid(row=0, column=0, padx=5)

        # Creates a button to play the playlist and assigns its callback method
        play_videos_btn = tk.Button(button_frame, text="Play Playlist", bg="#FFC1C1", fg="grey", command=self.play_playlist_clicked)
        play_videos_btn.grid(row=0, column=1, padx=5)

        # Creates a button to reset the playlist and assigns its callback method
        reset_playlist_btn = tk.Button(button_frame, text="Reset Playlist", bg="#FFC1C1", fg="grey", command=self.reset_playlist_clicked)
        reset_playlist_btn.grid(row=0, column=2, padx=5)

        # Creates a ScrolledText widget to display the playlist
        self.playlist_txt = tkst.ScrolledText(window, width=70, height=10, wrap="none")
        self.playlist_txt.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="W")

        # Creates a label to show the status
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="W")

    def add_video_clicked(self):
        # Gets the video number entered by the user
        key = self.input_txt.get()
        # Retrieves the video details from the library using the entered key
        video = self.get_video_details(key)
        if video:
            # Adds the video to the playlist if it exists
            self.playlist.append(key)
            # Updates the display of the playlist
            self.update_playlist_display()
            # Updates the status label to indicate the video was added
            self.status_lbl.configure(text=f"Video '{video['name']}' added to playlist!", fg="green")
        else:
            # Updates the status label to indicate the video was not found
            self.status_lbl.configure(text=f"Video number {key} not found!", fg="red")

        # Clear entry field after adding
        self.input_txt.delete(0, tk.END)

    def get_video_details(self, key):
        if key in lib.library:
            item = lib.library[key]
            return {
                "number": key,
                "name": item.name,
                "director": item.director,
                "rating": item.rating
            }
        return None

    def update_playlist_display(self):
        # Creates a string with the details of all videos in the playlist
        content = "\n".join([f"Video Number: {key}\nName: {self.get_video_details(key)['name']}\nDirector: {self.get_video_details(key)['director']}\nRating: {self.get_video_details(key)['rating']}\n" for key in self.playlist])
        # Deletes all text from the playlist_txt ScrolledText widget
        self.playlist_txt.delete("1.0", tk.END)
        # Inserts the playlist content into the playlist_txt ScrolledText widget
        self.playlist_txt.insert("1.0", content)

    def play_playlist_clicked(self):
        # Increments the play count for each video in the playlist
        for key in self.playlist:
            lib.increment_play_count(key)
        # Updates the status label to indicate the playlist was played
        self.status_lbl.configure(text="Playlist played. Play counts updated.", fg="green")

    def reset_playlist_clicked(self):
        # Resets the playlist to an empty list
        self.playlist = []
        # Updates the display of the playlist
        self.update_playlist_display()
        # Updates the status label to indicate the playlist was reset
        self.status_lbl.configure(text="Playlist reset.", fg="green")

if __name__ == "__main__":
    # Creates the main window
    window = tk.Tk()
    # Configures the fonts (assuming this is a predefined function)
    fonts.configure()
    # Initializes the CreateVideoList application
    CreateVideoList(window)
    # Starts the Tkinter main event loop
    window.mainloop()
