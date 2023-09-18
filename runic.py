# -*- coding: utf-8 -*-
"""
Transliterates latin characters (english alphabet and a few punctuation marks)
into unicode anglo-saxon runic characters. These can then be cut and pasted wherever.

Runes from "Runes - Reading the Past" by R. I. Page
University of California Press / British Museum 
ISBN 0-520-06114-4 

and wikipedia (for the unicode codes) https://en.wikipedia.org/wiki/Runic_(Unicode_block)
"""
runic_dict = {
    "ing": "\u16DD",
    "ae": "\u16AB",
    "th": "\u16A6",
    "ea": "\u16E0",
    "ia": "\u16e1",
    "io": "\u16e1",
    "oe": "\u16DF",
    "ee": "\u16DF",
    "gh": "\u16B8",
    "kh": "\u16E4",
    "a": "\u16AA",
    "b": "\u16D2",
    "c": "\u16B3",
    "d": "\u16DE",
    "e": "\u16D6",
    "f": "\u16A0",
    "g": "\u16B7",
    "h": "\u16BB",
    "i": "\u16C1",
    "j": "\u16C4",
    "k": "\u16e3",
    "l": "\u16DA",
    "m": "\u16D7",
    "n": "\u16BE",
    "o": "\u16A9",
    "p": "\u16C8",
    "q": "\u16E2",
    "r": "\u16B1",
    "s": "\u16CB",
    "t": "\u16CF",
    "u": "\u16A2",
    #        "v":"\u16A2",
    "v": "\u16A1",  # medieval version
    "w": "\u16B9",
    "x": "\u16C9",
    "y": "\u16A3",
    "z": "\u16CE",
    " ": "\u16eb",
    ",\u16eb": " \u16ec ",
    ";\u16eb": " \u16ec ",
    ":\u16eb": " \u16ec ",
    ".\u16eb": " \u16ed ",
    "?\u16eb": " \u16ed ",
    "!\u16eb": " \u16ed ",
    "'\u16eb": " \u16eb ",
    "'": " \u16eb ",
    ",": " \u16ec ",
    ";": " \u16ec ",
    ":": " \u16ec ",
    ".": " \u16ed ",
    "?": " \u16ed ",
    "!": " \u16ed ",
    '"': "",
}


def runify(text):
    text = text.lower()
    for k, v in runic_dict.items():
        text = text.replace(k, v)
    return text


if __name__ == "__main__":
    #This is a pangram which includes all of the letters in English as well as
    #runes which represent a short string of letters ("ing" for example)
    text = """sphinx of the black quartz ankh, tread my steep path via the 
station braes to fairly judge each arising poetic vow through aeons"""

    # With apologies to Prof Tolkien.
    text = """Where now the horse and the rider? Where is the horn that was blowing?
Where is the helm and the hauberk, and the bright hair flowing?
Where is the hand on the harpstring, and the red fire glowing?
Where is the spring and the harvest and the tall corn growing?
They have passed like rain on the mountain, like a wind in the meadow;
The days have gone down in the West behind the hills into shadow.
Who shall gather the smoke of the dead wood burning,
Or behold the flowing years from the Sea returning?"""

    print(text, end="\n\n")
    print(runify(text))

#     x =  runic_dict.items()

#     for k,v in x:
#         print(f"{k}\t- {v}")
