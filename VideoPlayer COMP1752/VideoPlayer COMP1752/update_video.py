import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

class UpdateVideos():
    def __init__(self, window):
        # Set the size of the window to 750x350 pixels
        window.geometry("750x350")
        # Set the title of the window to "Update Videos"
        window.title("Update Videos")
        # Set the background color
        window.configure(bg="#f0f0f0")

        # Create a button to update the rating, with a callback method
        update_rating_btn = tk.Button(
            window, text="Update Rating", bg="#FFC1C1", fg="grey", command=self.update_rating_clicked)
        # Place the button in the grid layout at row 0, column 0 with padding
        update_rating_btn.grid(row=1, column=1, padx=10, pady=10)

        # Create a label prompting the user to enter a video number
        enter_lbl = tk.Label(window, text="Enter Video Number", bg="#f0f0f0")
        # Place the label in the grid layout at row 0, column 1 with padding
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        # Create an entry widget for entering the video number
        self.video_number_txt = tk.Entry(window, width=5)
        # Place the entry widget in the grid layout at row 0, column 2 with padding
        self.video_number_txt.grid(row=0, column=1, padx=10, pady=10)

        # Create a label prompting the user to enter a new rating
        rating_lbl = tk.Label(window, text="Enter New Rating", bg="#f0f0f0")
        # Place the label in the grid layout at row 0, column 3 with padding
        rating_lbl.grid(row=0, column=2, padx=10, pady=10)

        # Create an entry widget for entering the new rating
        self.rating_txt = tk.Entry(window, width=5)
        # Place the entry widget in the grid layout at row 0, column 4 with padding
        self.rating_txt.grid(row=0, column=3, padx=10, pady=10)

        # Create a label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="#f0f0f0", fg="red")
        # Place the status label in the grid layout at row 1, spanning 5 columns
        self.status_lbl.grid(row=1, column=0, columnspan=5,
                             sticky="W", padx=10, pady=10)

        # Create a Text widget to display video details
        self.details_txt = tkst.ScrolledText(window, width=70, height=12, wrap="none", bg="#e0e0e0", fg="#000")
        # Place the Text widget in the grid layout at row 2, column 0, spanning 5 columns
        self.details_txt.grid(row=2, column=0, columnspan=5,
                              sticky="W", padx=10, pady=10)

    def update_rating_clicked(self):
        # Get the video number from the input field
        key = self.video_number_txt.get()
        try:
            # Convert the new rating to an integer
            new_rating = int(self.rating_txt.get())
            # Retrieve the video name from the library using the entered key
            name = lib.get_name(key)
            if name is not None:
                # Update the rating of the video in the library
                lib.set_rating(key, new_rating)
                # Retrieve the play count of the video
                play_count = lib.get_play_count(key)
                # Create a string with the updated video details
                details = f"Video Name: {name}\nNew Rating: {new_rating}\nPlay Count: {play_count}"
                # Update the details_txt Text widget with the new details
                self.details_txt.delete("1.0", tk.END)
                self.details_txt.insert("1.0", details)
                # Update the status label to indicate success
                self.status_lbl.configure(text=f"Video {key} rating updated", fg="green")
            else:
                # Update the status label if the video is not found
                self.status_lbl.configure(text=f"Video {key} not found")
        except ValueError:
            # Update the status label if the entered rating is not valid
            self.status_lbl.configure(text="Please enter a valid rating")

if __name__ == "__main__":
    # Create the main window
    window = tk.Tk()
    # Initialize the font manager
    fonts.configure()
    # Create an instance of the UpdateVideos class
    UpdateVideos(window)
    # Start the main event loop
    window.mainloop()
