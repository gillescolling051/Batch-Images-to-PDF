# Batch-Images-to-PDF
Converts all image files from a folder (subfolders) into (a) PDF file(s)

Utility which scans a folder or all subfolder for images files (jpg, png, gif) and outputs a single or multiple PDFs.

I desined this to read manga on my Remarkable, which I have in image form.


----------------------------------------------------------------------------------------------------------------------

The Logic for a single Folder works like this: 

Folder               images           Output
genericname            001     ==>    genericname.pdf
                       002
                       003
                       .
                       .
                       .
                       
 The Logic for a Folder containing subfolder works like this: 
 
Folder                 subfolder        images                Output
genericname            SUB_01           SUB_01_001     ==>    SUB_01.pdf
                       SUB_02           SUB_01_002            SUB_02.pdf
                                        SUB_01_002              .
                                          .                     .
                                          .                     .
                                          .
                                        SUB_02_001
                                        SUB_02_002
                                        SUB_02_003
                                          .
                                          .
                                          .
