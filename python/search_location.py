import tkinter as tk
import webbrowser

Height = 700
Width = 600
root = tk.Tk()
root.title("Location Search")
canvas_color = "#1088DD"
frame_color = "#F3EFED"
inner_frame_color = "#E8EFEF"
button_color = "#C04913"
entry_color = "#F2FECE"
font_ = ("Handlee", 16)


def search_function(search_term):
    if search_term:
        search_url = search_term.replace(' ', '+')
        webbrowser.open("https://google.com/maps/place/" + str(search_url))


def distance_function(current_loc, search_term):
    if current_loc and search_term:
        current_url = current_loc.replace(' ', '+')
        search_url = search_term.replace(' ', '+')
        url = f"https://www.google.com/maps/dir/{current_url}/{search_url}"
        webbrowser.open(url)


canvas = tk.Canvas(root, height=Height, width=Width, bg=canvas_color)
canvas.pack()

frame = tk.Frame(root, bg=frame_color, bd=2)
frame.place(relx=0.075, rely=0.1, relwidth=0.85, relheight=0.75)

# Current location label and entry (added above search)
current_label = tk.Label(frame, bg=canvas_color, text="Enter starting location", font=font_)
current_label.place(relx=0.05, rely=0.05, relwidth=0.90)

current_entry = tk.Entry(frame, bg=entry_color, font=font_)
current_entry.place(relx=0.05, rely=0.12, relwidth=0.90, relheight=0.06)

# Adjusted positions for search section (shifted down)
search_entry = tk.Entry(frame, bg=entry_color, font=font_)
search_entry.place(relx=0.16, rely=0.22, relwidth=0.60, relheight=0.05)

search_label = tk.Label(frame, bg=canvas_color, text="Enter location to search", font=font_)
search_label.place(relx=0.20, rely=0.28)

search_button = tk.Button(
    frame,
    font=font_,
    bg=button_color,
    text="Search",
    command=lambda: search_function(search_entry.get()),
)
search_button.place(relx=0.77, rely=0.22, relwidth=0.20, relheight=0.05)

# Distance button (added below search section)
distance_button = tk.Button(
    frame,
    font=font_,
    bg=button_color,
    text="Distance",
    command=lambda: distance_function(current_entry.get(), search_entry.get()),
)
distance_button.place(relx=0.40, rely=0.35, relwidth=0.20, relheight=0.05)

root.mainloop()