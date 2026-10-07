# TagStripper

A lightweight Python-based utility for cleaning and normalizing file and folder names.

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square)](https://www.microsoft.com/en-us/windows)

## Overview

TagStripper is a desktop utility for cleaning filenames by removing common download tags, encoding strings, formatting clutter, and unwanted separators.

It works with file and folder names only and does not modify file contents.

## Features

- Safe cleanup mode for replacing common filename separators
- Smart cleanup mode for removing tags, brackets, duplicate words, and web clutter
- File extension preservation
- Filename collision handling
- Support for renaming files and top-level folders

## Demo

Not applicable. TagStripper is distributed as a Windows desktop application.

## Tech Stack

- Python
- Tkinter
- PyInstaller

## Getting Started

Download the latest `TagStripper_Setup.exe` from the [Releases](https://github.com/mdhzarif03/TagStripper/releases) section.

Run the installer and launch TagStripper.

Select the directory you want to process, choose a cleanup mode, and execute the operation.

No additional dependencies are required when using the packaged application.

## Project Structure

```bash
TagStripper/
├── assets/
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

<img src="assets\software_interface.png">

| Mode | Description |
|------|------------|
| Safe Cleanup | Only replaces separators (`_`, `-`) |
| Smart Cleanup | Removes tags, brackets, and clutter strings |
 
Output Examples
| Input | Output (Smart Mode) |
|------|---------------------|
| Movie_1080p_Bluray.mkv | Movie.mkv |
| funny-cat-hd.gif | funny cat.gif |
| Wallpaper_[site].png | Wallpaper.png |

Notes
- Only the selected directory level is processed.
- Subdirectories are not scanned recursively.
- There is no preview before renaming.
- There is no undo feature.
- File contents are never modified.

**Status:** Released as version 1.0.0.
**Author:** Muhammad Hasan Zarif
**GitHub:** @mdhzarif03
