import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import ctypes

# --- Windows Taskbar Icon Grouping Fix (Lightweight & Native) ---
try:
    myappid = 'mdhzarif03.tagstripper.v1.0' 
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass

# --- Comprehensive List of Media, Web, and Archive Noise Tags ---
CLEANUP_PATTERN = re.compile(
    r'\b(1080p|720p|2160p|4k|uhd|bluray|bdrip|brrip|webrip|web\-dl|hdrip|dvdrip|h264|x264|h265|x265|hevc|aac|dts|dd5\.1|ac3|yify|rarbg|psa|galaxyrg|fgt|pahe|tigole|ita|eng|multi|subs?|dual\-audio|full\-hd|hd|www|com|net|org|co|uk|unrated|director\-cut|repack|xvid)\b', 
    re.IGNORECASE
)

# --- Cleanup Functions ---
def safe_cleanup(name):
    return name.replace('_', ' ').replace('-', ' ')

def smart_cleanup_logic(name):
    name = re.sub(r'\[.*?\]', '', name)
    name = re.sub(r'\(.*?\)', '', name)
    name = name.replace('_', ' ').replace('-', ' ').replace('.', ' ')
    name = CLEANUP_PATTERN.sub('', name)
    name = re.sub(r'\b(\w+)\s+\1\b', r'\1', name, flags=re.IGNORECASE)
    name = re.sub(r'\s+', ' ', name).strip()
    name = name.rstrip('. -_')
    return name

# --- Processing Logic ---
def process_directory(mode):
    folder_selected = filedialog.askdirectory(title="Select Directory to Clean")
    if not folder_selected:
        return 

    rename_count = 0
    for filename in os.listdir(folder_selected):
        file_path = os.path.join(folder_selected, filename)
        
        if os.path.isfile(file_path):
            base_name, ext = os.path.splitext(filename)
        else:
            base_name, ext = filename, ''
            
        if mode == 'safe':
            new_base = safe_cleanup(base_name)
        elif mode == 'smart':
            new_base = smart_cleanup_logic(base_name)
            if not new_base: 
                new_base = base_name
        else:
            continue
            
        new_filename = new_base + ext
        
        if filename != new_filename:
            new_file_path = os.path.join(folder_selected, new_filename)
            try:
                if os.path.exists(new_file_path):
                    if ext:
                        new_file_path = os.path.join(folder_selected, f"{new_base}_New{ext}")
                    else:
                        new_file_path = os.path.join(folder_selected, f"{new_base}_New")
                
                os.rename(file_path, new_file_path)
                rename_count += 1
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

    messagebox.showinfo("TagStripper", f"Cleanup complete!\nSuccessfully processed {rename_count} items.")

def open_github(event):
    webbrowser.open_new("https://github.com/mdhzarif03")

def on_enter(event):
    github_link.config(fg="#0066cc", font=("Tahoma", 8, "underline"))

def on_leave(event):
    github_link.config(fg="#555555", font=("Tahoma", 8))

root = tk.Tk()
root.title("TagStripper")  
root.geometry("480x250")  
root.resizable(False, False)

XP_BG = "#ECE9D8"          
XP_BLUE = "#004EAE"        
XP_TEXT = "#000000"
XP_BTN_BG = "#F0F0EA"      

root.configure(bg=XP_BG)

# Window Icon Loading & Auto-Scaling Logic for Banner
try:
    icon_path = os.path.join("assets", "app_icon.png")
    
    icon_img = tk.PhotoImage(file=icon_path)
    root.iconphoto(False, icon_img)
    
    banner_logo = icon_img.subsample(16, 16)
except Exception as e:
    print(f"Note: Runtime window icon could not load. Using system fallback. Details: {e}")

# Top Brand Banner Frame
header_frame = tk.Frame(root, bg=XP_BLUE, height=50)
header_frame.pack(fill="x", side="top")
header_frame.pack_propagate(False)

if 'banner_logo' in locals() or 'banner_logo' in globals():
    header = tk.Label(
        header_frame, 
        text="  TagStripper Clean Utility", 
        image=banner_logo,
        compound="left",
        font=("Tahoma", 11, "bold"), 
        fg="white", 
        bg=XP_BLUE, 
        anchor="w", 
        padx=15
    )
else:
    header = tk.Label(
        header_frame, 
        text="TagStripper v1.0", 
        font=("Tahoma", 12, "bold"), 
        fg="white", 
        bg=XP_BLUE, 
        anchor="w", 
        padx=15
    )
header.pack(fill="both", expand=True)

# Subtitle Instructions Area
sub_header = tk.Label(
    root, 
    text="Select a normalization task to execute on your target folder:", 
    font=("Tahoma", 9), 
    bg=XP_BG, 
    fg=XP_TEXT,
    padx=20,
    pady=15
)
sub_header.pack(anchor="w")

# Centered Button Frame
btn_frame = tk.Frame(root, bg=XP_BG)
btn_frame.pack(expand=True, pady=(0, 20))

# Button Styling
btn_options = {
    "font": ("Tahoma", 9),
    "bg": XP_BTN_BG,
    "fg": XP_TEXT,
    "activebackground": "#E0DEC9",
    "activeforeground": XP_TEXT,
    "bd": 2,
    "relief": "groove",
    "width": 25,       
    "height": 3,
    "cursor": "hand2"
}

btn_safe = tk.Button(
    btn_frame, 
    text="Option A: Safe Cleanup\n(Fix Separators Only)", 
    command=lambda: process_directory('safe'),
    **btn_options
)
btn_safe.grid(row=0, column=0, padx=10)

btn_smart = tk.Button(
    btn_frame, 
    text="Option B: Smart Cleanup\n(Strip Clutter & Tags)", 
    command=lambda: process_directory('smart'),
    **btn_options
)
btn_smart.grid(row=0, column=1, padx=10)

# Status Bar / Footer Separator
separator = tk.Frame(root, bg="#919B9C", height=1) 
separator.pack(fill="x", side="bottom", pady=(0, 24))

# Left Side Status Text
footer = tk.Label(
    root, 
    text="Status: Ready • System Batch Utility", 
    fg="#666666", 
    bg=XP_BG, 
    font=("Tahoma", 8),
    anchor="w",
    padx=15
)
footer.place(relx=0.0, rely=1.0, anchor="sw", y=-4)

# Right Side GitHub Credit Link
github_link = tk.Label(
    root, 
    text="Engineered by mdhzarif03", 
    fg="#555555", 
    bg=XP_BG, 
    font=("Tahoma", 8),
    anchor="e",
    padx=15,
    cursor="hand2"
)
github_link.place(relx=1.0, rely=1.0, anchor="se", y=-4)

# Bind mouse interactions to the hyperlink
github_link.bind("<Button-1>", open_github)
github_link.bind("<Enter>", on_enter)
github_link.bind("<Leave>", on_leave)

root.mainloop()