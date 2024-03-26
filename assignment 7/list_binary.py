#!/usr/bin/env python3
import pickle

OS = [["Mac OS", "11.0"],
      ["Windows", "11"],
      ["Android", "12"],
      ["Linux", "21.1"]]

# Open a binary file for write (overwrite)
with open("os.txt", "wb") as file:    # wb = write binary
    pickle.dump(OS, file)

# Open a binary file for read
with open("os.txt", "rb") as file:    # wr = read binary
    os = pickle.load(file)
    print(os)
