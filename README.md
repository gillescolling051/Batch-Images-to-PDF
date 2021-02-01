# Comic2PDF

Convert image files from a folder (subfolders) into (a) PDF file(s)

Scan a folder or all subfolder for images files (jpg, png, gif) and outputs a single or multiple PDFs.

Organize your Chapters into Volumes and convert them into PDF files for easy reading of the tablet of your choice

I desined this to read manga on my Remarkable2

## Installation Guide:
 
 1) Download dist.7z
 2) Unzip it with 7zip
 3) Run Setup
 
## Documentation:

Supported Formats: ".jpg",".jpeg",".png",".gif",".cbr",".rar",".cbz",".zip"

### Define Volumes:

- Define the manga/comic volumes. 
 Example: Volume 1 contains 10 Chapters, Volume 2 contains 5 Chapters
 Input: 1-10-15
 renames your folders containing chapters by adding "Vol. XX" to folder names
 Example: Chapter 1-10 => Vol.1 Chapter 1, Vol.1 Chapter 2,... Vol.1 Chapter 10, Vol.2 Chapter 11, ... Vol.2 Chapter 15
 
### Create Volume SubFolders:

- Move volume folders into seperate folders named XX. 
 Example: "Vol. 1 Chapter 1" "Vol. 1 Chapter 2" => 1, "Vol. 2 Chapter 3" "Vol. 2 Chapter 4" => 2 ... 
 Can only create subfolder when foldername contains "Vol", "vol", "VOL", "Volumes", "volumes", "VOLUMES" followed by volume number

### Combine everything to one PDF:

- Collects all images from the chosen directory and put them in one single PDF.

### Combine everything to one PDF:

- Collects all folders from the chosen directory and puts files in separate PDFs for each folder containing supported fileformats.
