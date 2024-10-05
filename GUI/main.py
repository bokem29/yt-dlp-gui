import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp

# Function to download videos
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL")
        return

    download_path = filedialog.askdirectory()
    if not download_path:
        messagebox.showerror("Error", "Please select a download directory")
        return

    try:
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Function to display download progress
def progress_hook(d):
    if d['status'] == 'downloading':
        progress_label.config(text=f"Downloading: {d['_percent_str']} complete")
    elif d['status'] == 'finished':
        progress_label.config(text="Download complete!")
        messagebox.showinfo("Success", "Video downloaded successfully!")

# Creating the main view
app = tk.Tk()
app.title("YouTube Video Downloader")

# Window size
app.geometry("500x300")
app.config(bg="#f0f0f0")

# Header label
header_label = tk.Label(app, text="YouTube Video Downloader", font=("Arial", 18, "bold"), bg="#f0f0f0")
header_label.pack(pady=20)

# Frame for input URL
frame = tk.Frame(app, bg="#f0f0f0")
frame.pack(pady=10)

# Label Entry
url_label = tk.Label(frame, text="YouTube URL:", font=("Arial", 12), bg="#f0f0f0")
url_label.pack(side=tk.LEFT, padx=10)
url_entry = tk.Entry(frame, width=40, font=("Arial", 12))
url_entry.pack(side=tk.LEFT)

# Download Button
download_button = tk.Button(app, text="Download", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=download_video)
download_button.pack(pady=20)

# Download progress
progress_label = tk.Label(app, text="", font=("Arial", 12), bg="#f0f0f0")
progress_label.pack(pady=10)

# Running the app
app.mainloop()
