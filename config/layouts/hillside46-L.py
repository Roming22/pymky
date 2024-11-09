# fmt: off
layout = {
    "alpha": {
        "color": (255, 0 , 0),
        "default": True,
        "keys": [
"ESC",              "F",    "TH(P, LALT)",  "TH(C, LCTL)",  "TH(N, LSFT)",  "B",
"TH(TAB, LSFT)",    "D",    "S",            "A",            "E",            "U",
"LCTL",             "LALT", "X",            "Z",            "V",            "COMMA",
                                            "NO",           "LM(nums)",     "SPACE",    "LGUI", "U",
        ],
        "combos": {
            (2, 3): "X",
            (2, 4): "Z",
            (3, 4): "V",
            (8, 9): "F",
            (8, 10): "B",
            (9, 10): "U",
        },
    },
    "nums": {
        "color": (255, 0 , 255),
        "keys": [
"____",     "NO",   "7",    "8",    "9",            "-",
"____",     "0",    "4",    "5",    "6",            "/",
"____",     "NO",   "1",    "2",    "3",            "=",
                            "NO",   "LC(alpha)",    "____", "____", "LC(nums)",
        ],
        "combos": {
            (2, 3): "5",
            (3, 4): "6",
            (8, 9): "3",
            (9, 10): "4",
        },
    },
}
