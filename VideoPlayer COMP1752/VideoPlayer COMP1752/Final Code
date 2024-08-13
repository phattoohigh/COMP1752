import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
import csv
import os
import webbrowser

class VideoManager:
    def __init__(self, window):
        self.window = window
        self.csv_file = 'videos.csv'

        # Set window size and title
        window.geometry("800x550")
        window.title("Video Manager")
        window.configure(bg="#f0f0f0")

        # Create and configure tabs
        self.tab_control = ttk.Notebook(window)
        self.tab_control.pack(expand=1, fill="both")

        # Create tabs
        self.library_tab = tk.Frame(self.tab_control, bg="#f0f0f0")
        self.create_tab = tk.Frame(self.tab_control, bg="#f0f0f0")
        self.update_tab = tk.Frame(self.tab_control, bg="#f0f0f0")
        self.tab_control.add(self.library_tab, text="Video Library")
        self.tab_control.add(self.create_tab, text="Create Video")
        self.tab_control.add(self.update_tab, text="Update Video")

        # Initialize tabs
        self.init_library_tab()
        self.init_create_tab()
        self.init_update_tab()

        # Status label outside of the tabs
        self.status_lbl = tk.Label(window, text="", font=("Arial", 10), bg="#f0f0f0", fg="red")
        self.status_lbl.pack(side="bottom", fill="x", pady=5)

    def init_library_tab(self):
        # Search functionality
        search_lbl = tk.Label(self.library_tab, text="Search Videos:", font=("Arial", 12), bg="#f0f0f0")
        search_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.search_txt = tk.Entry(self.library_tab, width=50, font=("Arial", 12))
        self.search_txt.grid(row=0, column=1, padx=10, pady=10)

        search_btn = tk.Button(self.library_tab, text="Search", font=("Arial", 12, "bold"), bg="#FFC1C1", fg="black", command=self.search_videos)
        search_btn.grid(row=0, column=2, padx=10, pady=10)

        # Listbox to display videos
        self.listbox = tk.Listbox(self.library_tab, width=70, height=15, selectmode=tk.SINGLE, font=("Arial", 12), bg="#e0e0e0", fg="#000")
        self.listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Add Select, Play, and Delete buttons
        select_btn = tk.Button(self.library_tab, text="Select", font=("Arial", 12, "bold"), bg="#FFC1C1", fg="black", command=self.selected_item)
        select_btn.grid(row=2, column=0, pady=10)

        play_btn = tk.Button(self.library_tab, text="Play", font=("Arial", 12, "bold"), bg="#FFC1C1", fg="black", command=self.play_selected)
        play_btn.grid(row=2, column=1, pady=10)

        delete_btn = tk.Button(self.library_tab, text="Delete", font=("Arial", 12, "bold"), bg="#FFC1C1", fg="black", command=self.delete_selected)
        delete_btn.grid(row=2, column=2, pady=10)

        self.display_videos_library()

    def search_videos(self):
        search_query = self.search_txt.get().lower()
        self.listbox.delete(0, tk.END)

        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for index, row in enumerate(reader, start=1):
                    if len(row) == 3:  # Ensure row has the expected number of columns
                        video_name, director_name, rating = row
                        if search_query in video_name.lower() or search_query in director_name.lower():
                            self.add_video_to_listbox(index, video_name, director_name, rating)

    def display_videos_library(self):
        # Clear the Listbox widget
        self.listbox.delete(0, tk.END)

        # Load and display videos from CSV
        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for index, row in enumerate(reader, start=1):
                    if len(row) == 3:  # Ensure row has the expected number of columns
                        video_name, director_name, rating = row
                        self.add_video_to_listbox(index, video_name, director_name, rating)

    def add_video_to_listbox(self, index, video_name, director_name, rating):
        display_text = f"{index}: {video_name} (Director: {director_name}, Rating: {rating})"
        self.listbox.insert(tk.END, display_text)

    def selected_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_video = self.listbox.get(selected_index[0])
            self.status_lbl.configure(text=f"Selected Video: {selected_video}", fg="Green")
        else:
            self.status_lbl.configure(text="No video selected.", fg="red")

    def play_selected(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_video = self.listbox.get(selected_index[0])
            video_name = selected_video.split(":")[1].split("(")[0].strip()
            self.status_lbl.configure(text=f"Playing: {video_name}", fg="green")
            # Open a YouTube search for the video name
            webbrowser.open(f"https://www.youtube.com/results?search_query={video_name}")
        else:
            self.status_lbl.configure(text="No video selected to play.", fg="red")

    def delete_selected(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            # Get the selected video details
            selected_video = self.listbox.get(selected_index[0])
            video_number = int(selected_video.split(":")[0].strip())

            # Remove the video from the CSV file
            if os.path.exists(self.csv_file):
                with open(self.csv_file, mode='r', newline='') as file:
                    reader = list(csv.reader(file))

                # Check if the video number is valid
                if 0 < video_number <= len(reader):
                    del reader[video_number - 1]  # Delete the selected row
                    with open(self.csv_file, mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(reader)
                    self.status_lbl.configure(text="Video deleted successfully!", fg="green")
                    self.display_videos_library()  # Refresh the listbox display
                else:
                    self.status_lbl.configure(text="Video number out of range.", fg="red")
        else:
            self.status_lbl.configure(text="No video selected to delete.", fg="red")

    def init_create_tab(self):
        # Create tab elements
        name_lbl = tk.Label(self.create_tab, text="Video Name:", font=("Arial", 12), bg="#f0f0f0")
        name_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.name_txt = tk.Entry(self.create_tab, width=50, font=("Arial", 12))
        self.name_txt.grid(row=0, column=1, padx=10, pady=10)

        director_lbl = tk.Label(self.create_tab, text="Director Name:", font=("Arial", 12), bg="#f0f0f0")
        director_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.director_txt = tk.Entry(self.create_tab, width=50, font=("Arial", 12))
        self.director_txt.grid(row=1, column=1, padx=10, pady=10)

        rating_lbl = tk.Label(self.create_tab, text="Rating:", font=("Arial", 12), bg="#f0f0f0")
        rating_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        self.rating_txt = tk.Entry(self.create_tab, width=50, font=("Arial", 12))
        self.rating_txt.grid(row=2, column=1, padx=10, pady=10)

        save_btn = tk.Button(self.create_tab, text="Save Video", font=("Arial", 12, "bold"), bg="#FFC1C1", fg="black", command=self.save_video_clicked)
        save_btn.grid(row=3, column=0, columnspan=2, pady=20)

        self.saved_videos_txt = tkst.ScrolledText(self.create_tab, width=70, height=10, wrap="none", font=("Arial", 12), bg="#e0e0e0", fg="#000")
        self.saved_videos_txt.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.status_lbl_create = tk.Label(self.create_tab, text="", font=("Arial", 10), bg="#f0f0f0", fg="red")
        self.status_lbl_create.grid(row=5, column=0, columnspan=2, sticky="W", padx=10, pady=10)

        self.display_videos_create()

    def display_videos_create(self):
        self.saved_videos_txt.delete("1.0", tk.END)

        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 3:  # Ensure row has the expected number of columns
                        video_name, director_name, rating = row
            self.saved_videos_txt.insert(tk.END, f"Video Name: {video_name}\n")
            self.saved_videos_txt.insert(tk.END, f"Director Name: {director_name}\n")
            self.saved_videos_txt.insert(tk.END, f"Rating: {rating}\n")
            self.saved_videos_txt.insert(tk.END, "-"*50 + "\n")

    def save_video_clicked(self):
        video_name = self.name_txt.get().strip()
        director_name = self.director_txt.get().strip()
        rating = self.rating_txt.get().strip()

        if video_name and director_name and rating:
            with open(self.csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([video_name, director_name, rating])
            self.status_lbl_create.configure(text="Video saved successfully!", fg="green")
            self.display_videos_create()
        else:
            self.status_lbl_create.configure(text="Please fill in all fields.", fg="red")

    def init_update_tab(self):
        # Update tab elements
        update_lbl = tk.Label(self.update_tab, text="Update Video Rating", font=("Arial", 14, "bold"), bg="#f0f0f0")
        update_lbl.grid(row=0, column=0, columnspan=2, pady=10)

        number_lbl = tk.Label(self.update_tab, text="Video Number:", font=("Arial", 12), bg="#f0f0f0")
        number_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.number_txt = tk.Entry(self.update_tab, width=50, font=("Arial", 12))
        self.number_txt.grid(row=1, column=1, padx=10, pady=10)

        rating_lbl = tk.Label(self.update_tab, text="New Rating:", font=("Arial", 12), bg="#f0f0f0")
        rating_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        self.new_rating_txt = tk.Entry(self.update_tab, width=50, font=("Arial", 12))
        self.new_rating_txt.grid(row=2, column=1, padx=10, pady=10)

        update_btn = tk.Button(self.update_tab, text="Update", font=("Arial", 12, "bold"), bg="#FFC1C1", fg="black", command=self.update_rating_clicked)
        update_btn.grid(row=3, column=0, columnspan=2, pady=20)

        self.update_status_lbl = tk.Label(self.update_tab, text="", font=("Arial", 10), bg="#f0f0f0", fg="red")
        self.update_status_lbl.grid(row=4, column=0, columnspan=2, sticky="W", padx=10, pady=10)

    def update_rating_clicked(self):
        try:
            video_number = int(self.number_txt.get().strip())
            new_rating = self.new_rating_txt.get().strip()

            if new_rating:
                if os.path.exists(self.csv_file):
                    updated = False
                    with open(self.csv_file, mode='r', newline='') as file:
                        reader = list(csv.reader(file))

                    if 0 < video_number <= len(reader):
                        reader[video_number - 1][2] = new_rating  # Update the rating column
                        updated = True

                    if updated:
                        with open(self.csv_file, mode='w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(reader)
                        self.update_status_lbl.configure(text="Rating updated successfully!", fg="green")
                    else:
                        self.update_status_lbl.configure(text="Video number out of range.", fg="red")
            else:
                self.update_status_lbl.configure(text="Please enter a new rating.", fg="red")
        except ValueError:
            self.update_status_lbl.configure(text="Invalid video number.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    video_manager = VideoManager(root)
    root.mainloop()
