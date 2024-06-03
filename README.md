# Magapoke Reverse Shuffle (MRS)
## DISCLAIMER
I do not work for Magapoke nor have any affiliation with them other than being one of their customers. I do not hold any rights to nor have ever seen any official Magapoke shuffle algorithm that may exist. I do not incentivise the use of this repository's code or any code derived from it for illegal purposes. I do not take responsibility for any use of this code by anybody other than myself under any circumstances.
## Description
This repository is able to reverse the shuffling algorithm implemented by Magapoke on their web manga reader.
## Requirements
This repository uses the python librarirs `os`, `numpy` and `opencv`, the latter of which is the only one you may need to install.

To install `opencv`, **open your terminal/powershell/cmd, type `python3 -m pip install opencv-python` and press enter**.
## How to use
Simply run the program with `python3 main.py` and follow the instructions.
## Where can I download the input images?
Simply open a chapter in magapoke with your `chrome developer tools` ***already*** opened on the `network` tab, then look through the pages of the chapter in question. You should see the images appear in the network tab as they are requested by your browser. To download them, simply double click on an image request, then right click on the image and click `Save image as...`.
