# Verify-the-integrity-of-the-files
Project steps:
    1. Create a python script (Find_hash_of_every_file.py) in which:
    • creating the directory function (scrolling in the directory, sub-directory, etc., calculating / generating the hash for each of them)
    • after # main - we read on blocks datein.txt (in this file there is on each separate line the name of a directory / subdirectory / file with full path)
    • change the name of the received string so as to obtain the "correct" name of the path (without \ n etc.)
    • check if the path is the directory, if so, display the directory path and the hash and apply the directory function
    • if it is not a directory, it means that it is a file -----> we display the file path and the hash
    Output: database (as: full path, hash) dateout.txt

    2. Create a python script (Verify_if_the_file_is_corrupted.py) in which:
    • we have as input ----> database
    • we read the database on blocks
    • look for the character “,” in the respective line; save, in the same string variable, the path name and store in the known_hash the old hash in the database
    • we generate the new hash for that path
    • check if known_hash is equal to the newly generated hash (digest)

Output: verifyout.txt
