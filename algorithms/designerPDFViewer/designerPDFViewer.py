#!/usr/bin/env python3
import string


def designerPdfViewer(letter_height: str, word: str):
    width, height = len(word), 0
    word_height_list = [int(i) for i in letter_height if i != ' ']
    map_letter = {letter: index for index, letter in enumerate(string.ascii_lowercase)}
    for item in word:
        t_height = word_height_list[map_letter[item]]
        if t_height > height:
            height = t_height
    return height * width
