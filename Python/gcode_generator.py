from ttgLib.TextToGcode import ttg
ttg("Lollo", 5, 0, "file", 2).toGcode("G0", "G1", "@", "@")