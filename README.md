<table>
  <tr>
    <td>

# TagStripper

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Status-Stable-green?style=flat-square)
![Type](https://img.shields.io/badge/Utility-File%20Renamer-orange?style=flat-square)

A lightweight, Python-based batch file renaming tool designed to clean filenames by removing common download tags, encoding strings, and formatting clutter.

It works only on file and folder names — not file contents.

  </td>

  <td width="180" align="right">
    <img src="assets/app_icon.png" width="140">
  </td>
</tr>
</table>

## Features

- **Safe Cleanup Mode**  
  Replaces `_` and `-` with spaces while preserving original text.

- **Smart Cleanup Mode**  
  Removes common media release tags, bracketed text (`[...]`, `(...)`), duplicate words, and web clutter strings.

- **Basic Data Safety**  
  Preserves file extensions and prevents empty filenames.

- **Collision Handling**  
  Adds `_New` suffix when a filename conflict is detected.

- **Folder Support**  
  Can rename files and top-level folders in a selected directory.

---

## How to Use
1. Navigate to the **Releases** panel on the right sidebar of this page.
2. Download the standalone production asset: TagStripper_Setup.exe.
3. Launch the wizard setup installer. Upon completion, the operational documentation guide will automatically deploy inside your desktop browser workspace.

---

## Behavior Summary

<img src="assets\software_interface.png">

| Mode | Description |
|------|------------|
| Safe Cleanup | Only replaces separators (`_`, `-`) |
| Smart Cleanup | Removes tags, brackets, and clutter strings |

---

## Tech Stack

- **Language:** Python
- **GUI:** Tkinter (Windows-style interface)
- **Packaging:** PyInstaller

---

## Output Example

| Input | Output (Smart Mode) |
|------|---------------------|
| Movie_1080p_Bluray.mkv | Movie.mkv |
| funny-cat-hd.gif | funny cat.gif |
| Wallpaper_[site].png | Wallpaper.png |

---

## Notes

- No recursive folder scanning (only selected directory level)
- No preview before renaming
- No undo feature
- File contents are never modified