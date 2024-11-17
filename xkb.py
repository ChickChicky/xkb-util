from typing import Any, Optional, Type, TypeVar, Union
from os.path import join, exists
from collections import ChainMap

XKB_PATH = '/usr/share/X11/xkb/'
SYMBOLS_BASE = 'us'

WARN_BAD_CHARCODE = False
WARN_BAD_KEYCODE = True
WARN_TRUNC_KEYMAP = False
WARN_BAD_BLOCK = True

# Generated with `naming.py` 
charmap = {'nul': 0, 'Control_a': 1, 'Control_b': 2, 'Control_c': 3, 'Control_d': 4, 'Control_e': 5, 'Control_f': 6, 'Control_g': 7, 'BackSpace': 8, 'Tab': 9, 'Linefeed': 10, 'Control_k': 11, 'Control_l': 12, 'Control_m': 13, 'Control_n': 14, 'Control_o': 15, 'Control_p': 16, 'Control_q': 17, 'Control_r': 18, 'Control_s': 19, 'Control_t': 20, 'Control_u': 21, 'Control_v': 22, 'Control_w': 23, 'Control_x': 24, 'Control_y': 25, 'Control_z': 26, 'Escape': 27, 'Control_backslash': 28, 'Control_bracketright': 29, 'Control_asciicircum': 30, 'Control_underscore': 31, 'space': 32, 'exclam': 33, 'quotedbl': 34, 'numbersign': 35, 'dollar': 36, 'percent': 37, 'ampersand': 38, 'apostrophe': 39, 'parenleft': 40, 'parenright': 41, 'asterisk': 42, 'plus': 43, 'comma': 44, 'minus': 45, 'period': 46, 'slash': 47, 'zero': 48, 'one': 49, 'two': 50, 'three': 51, 'four': 52, 'five': 53, 'six': 54, 'seven': 55, 'eight': 56, 'nine': 57, 'colon': 58, 'semicolon': 59, 'less': 60, 'equal': 61, 'greater': 62, 'question': 63, 'at': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, 'bracketleft': 91, 'backslash': 92, 'bracketright': 93, 'asciicircum': 94, 'underscore': 95, 'grave': 96, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122, 'braceleft': 123, 'bar': 124, 'braceright': 125, 'asciitilde': 126, 'Delete': 127, 'nobreakspace': 160, 'exclamdown': 161, 'cent': 162, 'sterling': 163, 'currency': 164, 'yen': 165, 'brokenbar': 166, 'section': 167, 'diaeresis': 168, 'copyright': 169, 'ordfeminine': 170, 'guillemotleft': 171, 'notsign': 172, 'hyphen': 173, 'registered': 174, 'macron': 175, 'degree': 176, 'plusminus': 177, 'twosuperior': 178, 'threesuperior': 179, 'acute': 180, 'mu': 181, 'paragraph': 182, 'periodcentered': 183, 'cedilla': 184, 'onesuperior': 185, 'masculine': 186, 'guillemotright': 187, 'onequarter': 188, 'onehalf': 189, 'threequarters': 190, 'questiondown': 191, 'Agrave': 192, 'Aacute': 193, 'Acircumflex': 194, 'Atilde': 195, 'Adiaeresis': 196, 'Aring': 197, 'AE': 198, 'Ccedilla': 199, 'Egrave': 200, 'Eacute': 201, 'Ecircumflex': 202, 'Ediaeresis': 203, 'Igrave': 204, 'Iacute': 205, 'Icircumflex': 206, 'Idiaeresis': 207, 'ETH': 208, 'Ntilde': 209, 'Ograve': 210, 'Oacute': 211, 'Ocircumflex': 212, 'Otilde': 213, 'Odiaeresis': 214, 'multiply': 215, 'Ooblique': 216, 'Ugrave': 217, 'Uacute': 218, 'Ucircumflex': 219, 'Udiaeresis': 220, 'Yacute': 221, 'THORN': 222, 'ssharp': 223, 'agrave': 224, 'aacute': 225, 'acircumflex': 226, 'atilde': 227, 'adiaeresis': 228, 'aring': 229, 'ae': 230, 'ccedilla': 231, 'egrave': 232, 'eacute': 233, 'ecircumflex': 234, 'ediaeresis': 235, 'igrave': 236, 'iacute': 237, 'icircumflex': 238, 'idiaeresis': 239, 'eth': 240, 'ntilde': 241, 'ograve': 242, 'oacute': 243, 'ocircumflex': 244, 'otilde': 245, 'odiaeresis': 246, 'division': 247, 'oslash': 248, 'ugrave': 249, 'uacute': 250, 'ucircumflex': 251, 'udiaeresis': 252, 'yacute': 253, 'thorn': 254, 'ydiaeresis': 255, 'F1': 256, 'F2': 257, 'F3': 258, 'F4': 259, 'F5': 260, 'F6': 261, 'F7': 262, 'F8': 263, 'F9': 264, 'F10': 265, 'F11': 266, 'F12': 267, 'F13': 268, 'F14': 269, 'F15': 270, 'F16': 271, 'F17': 272, 'F18': 273, 'F19': 274, 'F20': 275, 'Find': 276, 'Insert': 277, 'Remove': 278, 'Select': 279, 'Prior': 280, 'Next': 281, 'Macro': 282, 'Help': 283, 'Do': 284, 'Pause': 285, 'F21': 286, 'F22': 287, 'F23': 288, 'F24': 289, 'F25': 290, 'F26': 291, 'F27': 292, 'F28': 293, 'F29': 294, 'F30': 295, 'F31': 296, 'F32': 297, 'F33': 298, 'F34': 299, 'F35': 300, 'F36': 301, 'F37': 302, 'F38': 303, 'F39': 304, 'F40': 305, 'F41': 306, 'F42': 307, 'F43': 308, 'F44': 309, 'F45': 310, 'F46': 311, 'F47': 312, 'F48': 313, 'F49': 314, 'F50': 315, 'F51': 316, 'F52': 317, 'F53': 318, 'F54': 319, 'F55': 320, 'F56': 321, 'F57': 322, 'F58': 323, 'F59': 324, 'F60': 325, 'F61': 326, 'F62': 327, 'F63': 328, 'F64': 329, 'F65': 330, 'F66': 331, 'F67': 332, 'F68': 333, 'F69': 334, 'F70': 335, 'F71': 336, 'F72': 337, 'F73': 338, 'F74': 339, 'F75': 340, 'F76': 341, 'F77': 342, 'F78': 343, 'F79': 344, 'F80': 345, 'F81': 346, 'F82': 347, 'F83': 348, 'F84': 349, 'F85': 350, 'F86': 351, 'F87': 352, 'F88': 353, 'F89': 354, 'F90': 355, 'F91': 356, 'F92': 357, 'F93': 358, 'F94': 359, 'F95': 360, 'F96': 361, 'F97': 362, 'F98': 363, 'F99': 364, 'F100': 365, 'F101': 366, 'F102': 367, 'F103': 368, 'F104': 369, 'F105': 370, 'F106': 371, 'F107': 372, 'F108': 373, 'F109': 374, 'F110': 375, 'F111': 376, 'F112': 377, 'F113': 378, 'F114': 379, 'F115': 380, 'F116': 381, 'F117': 382, 'F118': 383, 'F119': 384, 'F120': 385, 'F121': 386, 'F122': 387, 'F123': 388, 'F124': 389, 'F125': 390, 'F126': 391, 'F127': 392, 'F128': 393, 'F129': 394, 'F130': 395, 'F131': 396, 'F132': 397, 'F133': 398, 'F134': 399, 'F135': 400, 'F136': 401, 'F137': 402, 'F138': 403, 'F139': 404, 'F140': 405, 'F141': 406, 'F142': 407, 'F143': 408, 'F144': 409, 'F145': 410, 'F146': 411, 'F147': 412, 'F148': 413, 'F149': 414, 'F150': 415, 'F151': 416, 'F152': 417, 'F153': 418, 'F154': 419, 'F155': 420, 'F156': 421, 'F157': 422, 'F158': 423, 'F159': 424, 'F160': 425, 'F161': 426, 'F162': 427, 'F163': 428, 'F164': 429, 'F165': 430, 'F166': 431, 'F167': 432, 'F168': 433, 'F169': 434, 'F170': 435, 'F171': 436, 'F172': 437, 'F173': 438, 'F174': 439, 'F175': 440, 'F176': 441, 'F177': 442, 'F178': 443, 'F179': 444, 'F180': 445, 'F181': 446, 'F182': 447, 'F183': 448, 'F184': 449, 'F185': 450, 'F186': 451, 'F187': 452, 'F188': 453, 'F189': 454, 'F190': 455, 'F191': 456, 'F192': 457, 'F193': 458, 'F194': 459, 'F195': 460, 'F196': 461, 'F197': 462, 'F198': 463, 'F199': 464, 'F200': 465, 'F201': 466, 'F202': 467, 'F203': 468, 'F204': 469, 'F205': 470, 'F206': 471, 'F207': 472, 'F208': 473, 'F209': 474, 'F210': 475, 'F211': 476, 'F212': 477, 'F213': 478, 'F214': 479, 'F215': 480, 'F216': 481, 'F217': 482, 'F218': 483, 'F219': 484, 'F220': 485, 'F221': 486, 'F222': 487, 'F223': 488, 'F224': 489, 'F225': 490, 'F226': 491, 'F227': 492, 'F228': 493, 'F229': 494, 'F230': 495, 'F231': 496, 'F232': 497, 'F233': 498, 'F234': 499, 'F235': 500, 'F236': 501, 'F237': 502, 'F238': 503, 'F239': 504, 'F240': 505, 'F241': 506, 'F242': 507, 'F243': 508, 'F244': 509, 'F245': 510, 'F246': 511, 'VoidSymbol': 512, 'Return': 513, 'Show_Registers': 514, 'Show_Memory': 515, 'Show_State': 516, 'Break': 517, 'Last_Console': 518, 'Caps_Lock': 519, 'Num_Lock': 520, 'Scroll_Lock': 521, 'Scroll_Forward': 522, 'Scroll_Backward': 523, 'Boot': 524, 'Caps_On': 525, 'Compose': 526, 'SAK': 527, 'Decr_Console': 528, 'Incr_Console': 529, 'KeyboardSignal': 530, 'Bare_Num_Lock': 531, 'KP_0': 768, 'KP_1': 769, 'KP_2': 770, 'KP_3': 771, 'KP_4': 772, 'KP_5': 773, 'KP_6': 774, 'KP_7': 775, 'KP_8': 776, 'KP_9': 777, 'KP_Add': 778, 'KP_Subtract': 779, 'KP_Multiply': 780, 'KP_Divide': 781, 'KP_Enter': 782, 'KP_Comma': 783, 'KP_Period': 784, 'KP_MinPlus': 785, 'dead_grave': 1024, 'dead_acute': 1025, 'dead_circumflex': 1026, 'dead_tilde': 1027, 'dead_diaeresis': 1028, 'dead_cedilla': 1029, 'dead_macron': 1030, 'dead_kbreve': 1031, 'dead_abovedot': 1032, 'dead_abovering': 1033, 'dead_kdoubleacute': 1034, 'dead_kcaron': 1035, 'dead_kogonek': 1036, 'dead_iota': 1037, 'dead_voiced_sound': 1038, 'dead_semivoiced_sound': 1039, 'dead_belowdot': 1040, 'dead_hook': 1041, 'dead_horn': 1042, 'dead_stroke': 1043, 'dead_abovecomma': 1044, 'dead_abovereversedcomma': 1045, 'dead_doublegrave': 1046, 'dead_invertedbreve': 1047, 'dead_belowcomma': 1048, 'dead_currency': 1049, 'dead_greek': 1050, 'Console_1': 1280, 'Console_2': 1281, 'Console_3': 1282, 'Console_4': 1283, 'Console_5': 1284, 'Console_6': 1285, 'Console_7': 1286, 'Console_8': 1287, 'Console_9': 1288, 'Console_10': 1289, 'Console_11': 1290, 'Console_12': 1291, 'Console_13': 1292, 'Console_14': 1293, 'Console_15': 1294, 'Console_16': 1295, 'Console_17': 1296, 'Console_18': 1297, 'Console_19': 1298, 'Console_20': 1299, 'Console_21': 1300, 'Console_22': 1301, 'Console_23': 1302, 'Console_24': 1303, 'Console_25': 1304, 'Console_26': 1305, 'Console_27': 1306, 'Console_28': 1307, 'Console_29': 1308, 'Console_30': 1309, 'Console_31': 1310, 'Console_32': 1311, 'Console_33': 1312, 'Console_34': 1313, 'Console_35': 1314, 'Console_36': 1315, 'Console_37': 1316, 'Console_38': 1317, 'Console_39': 1318, 'Console_40': 1319, 'Console_41': 1320, 'Console_42': 1321, 'Console_43': 1322, 'Console_44': 1323, 'Console_45': 1324, 'Console_46': 1325, 'Console_47': 1326, 'Console_48': 1327, 'Console_49': 1328, 'Console_50': 1329, 'Console_51': 1330, 'Console_52': 1331, 'Console_53': 1332, 'Console_54': 1333, 'Console_55': 1334, 'Console_56': 1335, 'Console_57': 1336, 'Console_58': 1337, 'Console_59': 1338, 'Console_60': 1339, 'Console_61': 1340, 'Console_62': 1341, 'Console_63': 1342, 'Down': 1536, 'Left': 1537, 'Right': 1538, 'Up': 1539, 'Shift': 1792, 'AltGr': 1793, 'Control': 1794, 'Alt': 1795, 'ShiftL': 1796, 'ShiftR': 1797, 'CtrlL': 1798, 'CtrlR': 1799, 'CapsShift': 1800, 'Meta_nul': 2048, 'Meta_Control_a': 2049, 'Meta_Control_b': 2050, 'Meta_Control_c': 2051, 'Meta_Control_d': 2052, 'Meta_Control_e': 2053, 'Meta_Control_f': 2054, 'Meta_Control_g': 2055, 'Meta_BackSpace': 2056, 'Meta_Tab': 2057, 'Meta_Linefeed': 2058, 'Meta_Control_k': 2059, 'Meta_Control_l': 2060, 'Meta_Control_m': 2061, 'Meta_Control_n': 2062, 'Meta_Control_o': 2063, 'Meta_Control_p': 2064, 'Meta_Control_q': 2065, 'Meta_Control_r': 2066, 'Meta_Control_s': 2067, 'Meta_Control_t': 2068, 'Meta_Control_u': 2069, 'Meta_Control_v': 2070, 'Meta_Control_w': 2071, 'Meta_Control_x': 2072, 'Meta_Control_y': 2073, 'Meta_Control_z': 2074, 'Meta_Escape': 2075, 'Meta_Control_backslash': 2076, 'Meta_Control_bracketright': 2077, 'Meta_Control_asciicircum': 2078, 'Meta_Control_underscore': 2079, 'Meta_space': 2080, 'Meta_exclam': 2081, 'Meta_quotedbl': 2082, 'Meta_numbersign': 2083, 'Meta_dollar': 2084, 'Meta_percent': 2085, 'Meta_ampersand': 2086, 'Meta_apostrophe': 2087, 'Meta_parenleft': 2088, 'Meta_parenright': 2089, 'Meta_asterisk': 2090, 'Meta_plus': 2091, 'Meta_comma': 2092, 'Meta_minus': 2093, 'Meta_period': 2094, 'Meta_slash': 2095, 'Meta_zero': 2096, 'Meta_one': 2097, 'Meta_two': 2098, 'Meta_three': 2099, 'Meta_four': 2100, 'Meta_five': 2101, 'Meta_six': 2102, 'Meta_seven': 2103, 'Meta_eight': 2104, 'Meta_nine': 2105, 'Meta_colon': 2106, 'Meta_semicolon': 2107, 'Meta_less': 2108, 'Meta_equal': 2109, 'Meta_greater': 2110, 'Meta_question': 2111, 'Meta_at': 2112, 'Meta_A': 2113, 'Meta_B': 2114, 'Meta_C': 2115, 'Meta_D': 2116, 'Meta_E': 2117, 'Meta_F': 2118, 'Meta_G': 2119, 'Meta_H': 2120, 'Meta_I': 2121, 'Meta_J': 2122, 'Meta_K': 2123, 'Meta_L': 2124, 'Meta_M': 2125, 'Meta_N': 2126, 'Meta_O': 2127, 'Meta_P': 2128, 'Meta_Q': 2129, 'Meta_R': 2130, 'Meta_S': 2131, 'Meta_T': 2132, 'Meta_U': 2133, 'Meta_V': 2134, 'Meta_W': 2135, 'Meta_X': 2136, 'Meta_Y': 2137, 'Meta_Z': 2138, 'Meta_bracketleft': 2139, 'Meta_backslash': 2140, 'Meta_bracketright': 2141, 'Meta_asciicircum': 2142, 'Meta_underscore': 2143, 'Meta_grave': 2144, 'Meta_a': 2145, 'Meta_b': 2146, 'Meta_c': 2147, 'Meta_d': 2148, 'Meta_e': 2149, 'Meta_f': 2150, 'Meta_g': 2151, 'Meta_h': 2152, 'Meta_i': 2153, 'Meta_j': 2154, 'Meta_k': 2155, 'Meta_l': 2156, 'Meta_m': 2157, 'Meta_n': 2158, 'Meta_o': 2159, 'Meta_p': 2160, 'Meta_q': 2161, 'Meta_r': 2162, 'Meta_s': 2163, 'Meta_t': 2164, 'Meta_u': 2165, 'Meta_v': 2166, 'Meta_w': 2167, 'Meta_x': 2168, 'Meta_y': 2169, 'Meta_z': 2170, 'Meta_braceleft': 2171, 'Meta_bar': 2172, 'Meta_braceright': 2173, 'Meta_asciitilde': 2174, 'Meta_Delete': 2175, 'Ascii_0': 2304, 'Ascii_1': 2305, 'Ascii_2': 2306, 'Ascii_3': 2307, 'Ascii_4': 2308, 'Ascii_5': 2309, 'Ascii_6': 2310, 'Ascii_7': 2311, 'Ascii_8': 2312, 'Ascii_9': 2313, 'Hex_0': 2314, 'Hex_1': 2315, 'Hex_2': 2316, 'Hex_3': 2317, 'Hex_4': 2318, 'Hex_5': 2319, 'Hex_6': 2320, 'Hex_7': 2321, 'Hex_8': 2322, 'Hex_9': 2323, 'Hex_A': 2324, 'Hex_B': 2325, 'Hex_C': 2326, 'Hex_D': 2327, 'Hex_E': 2328, 'Hex_F': 2329, 'Shift_Lock': 2560, 'AltGr_Lock': 2561, 'Control_Lock': 2562, 'Alt_Lock': 2563, 'ShiftL_Lock': 2564, 'ShiftR_Lock': 2565, 'CtrlL_Lock': 2566, 'CtrlR_Lock': 2567, 'CapsShift_Lock': 2568, 'SShift': 3072, 'SAltGr': 3073, 'SControl': 3074, 'SAlt': 3075, 'SShiftL': 3076, 'SShiftR': 3077, 'SCtrlL': 3078, 'SCtrlR': 3079, 'SCapsShift': 3080, 'Brl_blank': 3584, 'Brl_dot1': 3585, 'Brl_dot2': 3586, 'Brl_dot3': 3587, 'Brl_dot4': 3588, 'Brl_dot5': 3589, 'Brl_dot6': 3590, 'Brl_dot7': 3591, 'Brl_dot8': 3592, 'Brl_dot9': 3593, 'Brl_dot10': 3594, 'Control_h': 8, 'Control_i': 9, 'Control_j': 10, 'Home': 276, 'End': 279, 'PageUp': 280, 'PageDown': 281, 'multiplication': 215, 'pound': 163, 'pilcrow': 182, 'Oslash': 216, 'Shift_L': 1796, 'Shift_R': 1797, 'Control_L': 1798, 'Control_R': 1799, 'AltL': 1795, 'AltR': 1793, 'Alt_L': 1795, 'Alt_R': 1793, 'AltGr_L': 1795, 'AltGr_R': 1793, 'AltLLock': 2563, 'AltRLock': 2561, 'SCtrl': 3074, 'Spawn_Console': 530, 'Uncaps_Shift': 1800, 'tilde': 126, 'circumflex': 94, 'dead_ogonek': 1029, 'dead_caron': 1026, 'dead_breve': 1027, 'dead_doubleacute': 1027, 'no-break_space': 160, 'paragraph_sign': 167, 'soft_hyphen': 173, 'rightanglequote': 187}
charmap |= {
    'Greek_alpha': ord('α'),
    'Greek_ALPHA': ord('Α'),
    'Greek_lamda': ord('λ'),
    'Greek_LAMDA': ord('Λ'),
    'Greek_lambda': ord('λ'),
    'Greek_LAMBDA': ord('Λ'),
    'Greek_chi': ord('χ'),
    'Greek_CHI': ord('Χ'),
    'Greek_omega': ord('ω'),
    'Greek_OMEGA': ord('Ω'),
    'Greek_pi': ord('π'),
    'Greek_PI': ord('Π'),
    'Greek_epsilon': ord('ε'),
    'Greek_EPSILON': ord('Ε'),
    'Greek_rho': ord('ρ'),
    'Greek_RHO': ord('Ρ'),
    'Greek_upsilon': ord('υ'),
    'Greek_UPSILON': ord('Υ'),
    'Greek_tau': ord('τ'),
    'Greek_TAU': ord('Τ'),
    'Greek_theta': ord('θ'),
    'Greek_THETA': ord('Θ'),
    'Greek_iota': ord('ι'),
    'Greek_IOTA': ord('Ι'),
    'Greek_omicton': ord('ο'),
    'Greek_OMICTON': ord('Ο'),
    'Greek_beta': ord('β'),
    'Greek_BETA': ord('Β'),
    'Greek_mu': ord('μ'),
    'Greek_MU': ord('Μ'),
    'Greek_nu': ord('ν'),
    'Greek_NU': ord('Ν'),
    'Greek_zeta': ord('ζ'),
    'Greek_ZETA': ord('Ζ'),
    'Greek_psi': ord('ψ'),
    'Greek_PSI': ord('Ψ'),
    'Greek_kappa': ord('κ'),
    'Greek_KAPPA': ord('Κ'),
    'Greek_xi': ord('ξ'),
    'Greek_XI': ord('Ξ'),
    'Greek_sigma': ord('σ'),
    'Greek_finalsmallsigma': ord('ς'),
    'Greek_SIGMA': ord('Σ'),
    'Greek_eta': ord('η'),
    'Greek_ETA': ord('Η'),
    'Greek_delta': ord('δ'),
    'Greek_DELTA': ord('Δ'),
    'Greek_phi': ord('φ'),
    'Greek_PHI': ord('Φ'),
    'Greek_gamma': ord('γ'),
    'Greek_GAMMA': ord('Γ'),
    'Greek_omicron': ord('ο'),
    'Greek_OMICRON': ord('Ο'),
    'union': ord('∪'),
    'intersection': ord('∩'),
    'elementof': ord('∈'),
    'notelementof': ord('∉'),
    'includedin': ord('⊂'),
    'includes': ord('⊃'),
    'zerosuperior': ord('⁰'),
    'onesuperior': ord('¹'),
    'twosuperior': ord('²'),
    'threesuperior': ord('³'),
    'foursuperior': ord('⁴'),
    'fivesuperior': ord('⁵'),
    'sixsuperior': ord('⁶'),
    'sevensuperior': ord('⁷'),
    'eightsuperior': ord('⁸'),
    'ninesuperior': ord('⁹'),
}

keymap = {
    # TODO: Not sure if LSGT should really map to this
    'TLDE': 0x29,
    'I219': 0x56, 'LSGT': 0x56,
    'SPCE': 0x39,
    'ESC': None, # 0x01,
    'TAB': 0x0F,
    'BKSP': None, # 0x0E,
    'RTRN': None, # 0x1C,
    'INS': None, # 0x52,
    'SUPR': None, # 0x53,
    'DELE': None, # 0x53,
    'HOME': None, # 0x47,
    'END': None, # 0x4F,
    'PGUP': None, # 0x49,
    'PGDN': None, # 0x51,
    'UP': None, # 0x48,
    'DOWN': None, # 0x50,
    'LEFT': None, # 0x4B,
    'RGHT': None, # 0x4D,
    
    'NMLK': None,
    'KPDL': None,
    'KPPT': None,
    'KPEN': None,
    'KPEQ': None,
    'KPDV': None,
    'KPMU': None,
    'KPSU': None,
    'KPAD': None,
    'KP7': None,
    'KP8': None,
    'KP9': None,
    'KP4': None,
    'KP5': None,
    'KP6': None,
    'KP1': None,
    'KP2': None,
    'KP3': None,
    'KP0': None,
    'KODL': None,
    'KOPT': None,
    'KOEN': None,
    'KOEQ': None,
    'KODV': None,
    'KOMU': None,
    'KOSU': None,
    'KOAD': None,
    'KO7': None,
    'KO8': None,
    'KO9': None,
    'KO4': None,
    'KO5': None,
    'KO6': None,
    'KO1': None,
    'KO2': None,
    'KO3': None,
    'KO0': None,
    'LFSH': None,
    'RTSH': None,
    'ALT': None,
    'LALT': None,
    'RALT': None,
    'LCTL': None,
    'RCTL': None,
    'MENU': None, # What is this?
    'META': None,
    'LWIN': None,
    'RWIN': None,
    'CAPS': None,
    'HYPR': None,
    'PRSC': None,
    'SCLK': None,
    'PAUS': None,
    'LVL1': None,
    'LVL2': None,
    'LVL3': None,
    'LVL4': None,
    'LVL5': None,
    'FK01': None,
    'FK02': None,
    'FK03': None,
    'FK04': None,
    'FK05': None,
    'FK06': None,
    'FK07': None,
    'FK08': None,
    'FK09': None,
    'FK10': None,
    'FK11': None,
    'FK12': None,
    'FK13': None,
    'FK14': None,
    'FK15': None,
    'FK16': None,
    'FK17': None,
    'FK18': None,
    'FK19': None,
    'FK20': None,
    'FK21': None,
    'FK22': None,
    'FK23': None,
    'FK24': None,
    'MUHE': None,
    'HENK': None,
    'HKTG': None,
    'HIRA': None,
    'KATA': None,
    'HNGL': None,
    'HJCV': None,
    'OUTP': None,
    'KITG': None,
    'KATA': None,
    'KIDN': None,
    'KIUP': None,
    'LatQ': None,
    'LatW': None,
    'LatY': None,
    'LatA': None,
    'LatZ': None,
    'COMP': None,
    'SYRQ': None,
    
    'AE01': 0x02,
    'AE02': 0x03,
    'AE03': 0x04,
    'AE04': 0x05,
    'AE05': 0x06,
    'AE06': 0x07,
    'AE07': 0x08,
    'AE08': 0x09,
    'AE09': 0x0A,
    'AE10': 0x0B,
    'AE11': 0x0C,
    'AE12': 0x0D,
    'AE13': None, # Backspace
    
    'AD01': 0x10,
    'AD02': 0x11,
    'AD03': 0x12,
    'AD04': 0x13,
    'AD05': 0x14,
    'AD06': 0x15,
    'AD07': 0x16,
    'AD08': 0x17,
    'AD09': 0x18,
    'AD10': 0x19,
    'AD11': 0x1A,
    'AD12': 0x1B,
    
    'AC01': 0x1E,
    'AC02': 0x1F,
    'AC03': 0x20,
    'AC04': 0x21,
    'AC05': 0x22,
    'AC06': 0x23,
    'AC07': 0x24,
    'AC08': 0x25,
    'AC09': 0x26,
    'AC10': 0x27,
    'AC11': 0x28,
    'AC12': 0x2B, 'BKSL': 0x2B,
    
    'AB01': 0x2C,
    'AB02': 0x2D,
    'AB03': 0x2E,
    'AB04': 0x2F,
    'AB05': 0x30,
    'AB06': 0x31,
    'AB07': 0x32,
    'AB08': 0x33,
    'AB09': 0x34,
    'AB10': 0x35,
    'AB11': None,
    'AB12': None,
    
    'AA01': None,
    'AA02': None,
    'AA03': None,
    'AA04': None,
    'AA05': None,
    'AA06': None,
    'AA07': None,
}

class Source:
    """
    Used to store data from the source of a program
    """
    
    name : str
    body : str
    
    def __init__( self, name:str, body:str ):
        self.name = name
        self.body = body
        
    def lines( self ) -> list[str]:
        return list(map(lambda l:l.removesuffix('\r'),self.body.split('\n')))
        
    @staticmethod
    def fromFile( path:str ) -> 'Source':
        """
        Creates a new source from a file
        """
        body = ''
        with open(path,'rt') as file:
            body = file.read().replace('\r\n','\n')
        return Source(path,body)
    
class TokenEOF(str):
    """
    Used as the text of the token appended at the end of `tokenize`
    """
    
    def __init__(self):pass
    def __str__(self):return'<EOF>'
    def __repr__(self):return'<EOF>'
    pass
    
class Token:
    """
    Represents a single token
    """
    
    t : str
    c : int
    l : int
    i : int
    s : Source
    
    def __init__( self, t:str, c:int, l:int, i:int, s:Source ):
        self.t = t
        self.c = c
        self.l = l
        self.i = i
        self.s = s
    
    def isidentifier( self ) -> bool:
        return len(self.t) > 0 and self.t[0].lower() in 'abcdefghijklmnopqrstuvwxyz_$'
    
    def isnumeric( self ) -> bool:
        return self.t.isnumeric()
    
    def isstring( self ) -> bool:
        return self.t.startswith('"') and self.t.endswith('"')
    
    def __str__( self ) -> str:
        return 'Token<\x1b[33m%s\x1b[39m \x1b[35m%d\x1b[39m:\x1b[35m%d\x1b[39m>'%(self.t,self.l+1,self.c+1)

U = TypeVar('U')
Tup = Union[U, tuple[U,...], list[U]]

class Tokens:
    """
    Represents a group of tokens issued from the same source
    """
    
    source : Source
    tokens : list[Token]
    
    def __init__( self, source:Source ):
        self.source = source
        self.tokens = []
        self.idx = 0
            
    def more( self, n: int = 0 ) -> bool:
        return len(self.tokens) > self.idx+n
    
    def next( self ) -> Token:
        tk = self.tokens[self.idx]
        self.idx += 1
        return tk
    
    def peek( self, n: int = 0 ):
        return self.tokens[self.idx+n]
    
    def expect( self, t: Tup[str] ) -> bool:
        return self.more() and self.next().t in tup(t)
    
    def require( self, t: Tup[str] ) -> bool:
        return self.more() and self.peek().t in tup(t)
    
    def trim( self, t: Tup[str] ):
        if self.more() and self.peek().t in tup(t):
            self.idx += 1
            
    def rewind( self, token: Token ):
        while self.tokens[self.idx] != token and self.idx > 1:
            self.idx -= 1
        
    def __str__(self) -> str:
        return 'Tokens['+', '.join(map(str,self.tokens))+']'

compoundTokens = [
    '//',
    '/*',
    '*/',
]

def tokenize(source: Source) -> Tokens:
    """
    Retrieves tokens from the provided source
    """
    
    tokens = Tokens(source)
    
    in_line_comment = False
    in_block_comment = False
    
    l,c = 0,0
    
    flags: dict[str,dict[str,Any]] = {}
    
    tmp = ''
    
    def sep(i,dooff=True):
        nonlocal tmp
        if in_line_comment or in_block_comment:
            return
        if len(tmp):
            tokens.tokens.append(Token(tmp,c-(dooff*len(tmp)),l,i,source))
            tmp = ''
    
    skip = 0
    for i,ch in enumerate(source.body):
        if skip > 0: 
            c += 1
            skip -= 1
            continue
        if 'str' in flags:
            s = flags.get('str')
            esc: dict = s.get('esc')
            if esc:
                def end(c:str):
                    nonlocal tmp
                    del s['esc']
                    tmp += c
                if not esc.get('n',False):
                    esc['n'] = True
                    if ch.lower() in 'xou':
                        esc['radix'] = ch.lower()
                    elif ch == 'n': end('\n')
                    elif ch == 'r': end('\r')
                    elif ch == 't': end('\t')
                    elif ch == '@': end('\0')
                    elif ch == '0': end('\0')
                    elif ch == 'e': end('\x1b')
                    elif ch == '^': end('\x1b')
                    else          : end(ch)
                    esc['v'] = ''
                else:
                    esc['v'] += ch
                    radix = esc.get('radix',None)
                    if radix:
                        if radix == 'x' and len(esc['v']) == 2:
                            end(chr(int(esc['v'],base=16)))
                        elif radix == 'o' and len(esc['v']) == 3:
                            end(chr(int(esc['v'],base=8)))
                        elif radix == 'u' and len(esc['v']) == 4:
                            end(chr(int(esc['v'],base=16)))
                    else:
                        raise RuntimeError('That should not happen, right ?')
            else:
                if ch == s.get('opens'):
                    tokens.tokens.append(Token('"'+tmp+'"',s.get('c'),s.get('l'),s.get('i'),source))
                    tmp = ''
                    del flags['str']
                elif ch == '\\':
                    s['esc'] = {'n':0,'v':''}
                else:
                    tmp += ch
        else:
            compound = False
            for t in compoundTokens:
                if source.body[i:i+len(t)] == t:
                    if t == '*/':
                        in_block_comment = False
                        tmp = ''
                        compound = True
                        skip = 1
                    elif in_block_comment or in_line_comment:
                        pass
                    elif t == '/*':
                        in_block_comment = True
                    elif t == '//':
                        in_line_comment = True
                    else:
                        sep(i)
                        tmp = t
                        sep(i,False)
                        skip = len(t)-1
                        compound = True
                    break
            if not compound and not (in_block_comment or in_line_comment):
                if ch in ' \t\n':
                    sep(i)
                elif ch in '.,:;/+-*=!?()[]{}<>@#~^&\\|':
                    sep(i)
                    tmp = ch
                    sep(i,False)
                elif ch in '`\'"':
                    flags['str'] = {'opens':ch,'c':c,'l':l,'i':i}
                else:
                    tmp += ch
        c += 1
        if ch == '\n':
            if in_line_comment:
                in_line_comment = False
                tmp = ''
            l += 1
            c = 0
    
    sep(len(source.body))
    
    tokens.tokens.append(Token(TokenEOF(),c,l,i,source))
    
    return tokens

Flags = dict[str, Any]

KeyMap = tuple[Optional[int], Optional[int], Optional[int], Optional[int]]
Key = int

class Decl:
    flags : Flags
    name  : str
    
    def __init__(self, flags: Flags, name: str):
        self.flags = flags
        self.name = name

class Symbols( Decl ):
    # TODO: maybe use collections.ChainMap to support recursive inclusions?
    mapping : ChainMap[Key, KeyMap]
    
    def __init__(self, flags: Flags, name: str):
        super().__init__(flags, name)
        self.mapping = ChainMap()

class KeyData:
    map : KeyMap
    
    def __init__(self):
        self.map = None

def warn(*args, **kwargs):
    print('\x1b[93;1mWarning\x1b[39;22m:', *args, **kwargs)
    
def error(*args, **kwargs):
    print('\x1b[91;1mError\x1b[39;22m:', *args, **kwargs)
    exit(1)
    
def parse_warn(token: Token, message: str):
    rline = token.s.lines()[token.l].replace('\t', ' ')
    line = rline.lstrip()     # removes all indent
    dl = len(rline)-len(line) # computes the shift caused by the indent
    msg = '\x1b[93;1mWarning\x1b[22;39m (\x1b[36m%s:%d:%d\x1b[39m):\n' % ( token.s.name, token.l+1, token.c+1 )
    msg += '  %s\n\n'  % ( message.replace('\n','\n  '), )
    msg += '  %s\n' %( line[:token.c-dl]+'\x1b[33m'+line[token.c-dl:token.c-dl+len(token.t)]+'\x1b[39m'+line[token.c-dl+len(token.t):], )
    msg += '  %s' % ( ' '*(token.c-dl)+'^'+'~'*(len(token.t)-1), )
    print(msg)
    
def parse_error(token: Token, message: str):
    rline = token.s.lines()[token.l]
    line = rline.lstrip()     # removes all indent
    dl = len(rline)-len(line) # computes the shift caused by the indent
    msg = '\x1b[91;1mSyntax error\x1b[22;39m (\x1b[36m%s:%d:%d\x1b[39m):\n' % ( token.s.name, token.l+1, token.c+1 )
    msg += '  %s\n\n'  % ( message.replace('\n','\n  '), )
    msg += '  %s\n' %( line[:token.c-dl]+'\x1b[33m'+line[token.c-dl:token.c-dl+len(token.t)]+'\x1b[39m'+line[token.c-dl+len(token.t):], )
    msg += '  %s' % ( ' '*(token.c-dl)+'^'+'~'*(len(token.t)-1), )
    print(msg)
    exit(1)
    
def tup(val):
    if isinstance(val, (tuple, list)):
        return tuple(val)
    return (val,)

T = TypeVar('T', bound=Decl)
def decls_get(decls: list[Decl], name: str, kind: Optional[Type[T]] = Decl) -> Optional[T]:
    for decl in decls:
        if decl.name == name and (kind == None or isinstance(decl, kind)):
            return decl
    return None

T = TypeVar('T', bound=Decl)
def decls_get_default(decls: list[Decl], kind: Optional[Type[T]] = Decl) -> Optional[T]:
    for decl in decls:
        if 'default' in decl.flags and (kind == None or isinstance(decl, kind)):
            return decl
    return None

def getnum(v):
    try:
        return int(v, 16)
    except:
        return None
    
class ParseEnv:
    symbols_includes : list[tuple[dict, str, Token]]
    
    def __init__( self ):
        self.symbols_includes = []

bad_charcode = set()

def parse_key_data(tokens: Tokens, env: ParseEnv, key: KeyData):
    acc = []
    
    def process_acc():
        nonlocal acc
        
        if not len(acc):
            acc = []
            return
        
        i = tokens.idx
        
        if acc[0].t == '[':
            tokens.rewind(acc[1])
            
            if key.map != None:
                warn('Overriding key map')
            
            mp = []
            
            while True:
                if not tokens.more():
                    parse_error(token, 'Unexpected EOF')
                
                char_tk = tokens.next()
                raw_char = char_tk.t
                code = charmap.get(raw_char)
                
                if code == None:
                    code = getnum(raw_char)
                    if code != None:
                        code += ord('0')
                if code == None and len(raw_char) and raw_char[0] == 'U':
                    code = getnum(raw_char[1:])
                if WARN_BAD_CHARCODE and code == None and raw_char not in bad_charcode:
                    parse_warn(char_tk, 'Unknown char code')
                    bad_charcode.add(raw_char)
                
                mp.append(code)
                
                if not tokens.require((',', ']')):
                    parse_error(token, 'Expected either `,` or `]`')
                
                tk = tokens.next().t
                
                if tk == ',':
                    continue
                
                break
            
            if WARN_TRUNC_KEYMAP and len(mp) > 4:
                parse_warn(acc[0], 'Truncating key map')
            
            key.map = tuple((mp+[None, None, None, None])[:4])
            
        tokens.idx = i
        acc = []
    
    while True:
        if not tokens.more():
            parse_error(token, 'Unexpected EOF')
        token = tokens.next()
        # print('    kd', token)
        if token.t == '}':
            process_acc()
            tokens.trim(';')
            return
        elif token.t == ',':
            process_acc()
        else:
            acc.append(token)

def parse_symbols(tokens: Tokens, env: ParseEnv, symbols: Symbols):
    acc = []
    d = 0
    
    while True:
        if not tokens.more():
            parse_error(token, 'Unexpected EOF')
        token = tokens.next()
        
        # print('  symb', token)
        
        if token.isidentifier():
            match token.t:
                case 'include':
                    if not tokens.more():
                        parse_error(token, 'Expected name after inclusion statement')
                    name_tk = tokens.next()
                    if not name_tk.isstring():
                        parse_error(token, 'Expected inclusion name as string')
                    name = name_tk.t[1:-1]
                    incl = {}
                    symbols.mapping.maps.append(incl)
                    env.symbols_includes.append((incl, name, name_tk))
                
                case 'key' if tokens.peek().t != '.':
                    if not tokens.expect('<'):
                        parse_error(token, 'Unsupported key type')
                    key_tk = tokens.next()
                    if not tokens.expect('>'):
                        parse_error(token, 'Expected `>` to close key code')
                    if not tokens.expect('{'):
                        parse_error(token, 'Expected `{` to open key data')
                    key_data = KeyData()
                    parse_key_data(tokens, env, key_data)
                    if key_tk.t in keymap:
                        mp = keymap[key_tk.t]
                        if mp != None:
                            symbols.mapping[mp] = key_data
                    elif WARN_BAD_KEYCODE:
                        parse_warn(key_tk, 'Unknown key name')
                
                case _:
                    acc.append(token)
        
        elif token.t == '}' and d <= 0:
            tokens.trim(';')
            return
        
        elif token.t == ';':
            acc = []
        
        else:
            if token.t == '{':
                d += 1
            if token.t == '}':
                d -= 1
            acc.append(token)

symbols_cache = {}
def parse_decls(name: str, bypass_cache: bool = False) -> list[Decl]:
    if name in symbols_cache and not bypass_cache:
        return symbols_cache[name]
    
    path = join(XKB_PATH, 'symbols', name)
    if not exists(path):
        return None
    
    src = Source.fromFile(path)
    tokens = tokenize(src)
    env = ParseEnv()
    flags: Flags = {}
    decls = []
    
    while tokens.more():
        token = tokens.next()
        
        # print('decl', token)
        
        if token.isidentifier():
            match token.t:
                case 'default' | 'hidden' as flag:
                    flags[flag] = True
                
                case 'partial':
                    flags['partial'] = set()
                
                case kind if kind.endswith('_keys') or kind == 'partial':
                    flags.get('mod',set()).add(kind[:-5])
                
                case block if block.startswith('xkb_'):
                    if not tokens.more():
                        parse_error(token,'Expected name after block declaration')
                    name_tk = tokens.next()
                    if not name_tk.isstring():
                        parse_error(token, 'Expected name as string')
                    
                    if not tokens.expect('{'):
                        parse_error(tokens.peek(), 'Expected `{` after block name')
                    
                    block_name = name_tk.t[1:-1]
                    
                    match block[4:]:
                        case 'symbols':
                            symbols = Symbols(flags, block_name)
                            parse_symbols(tokens, env, symbols)
                            decls.append(symbols)
                        case block:
                            if WARN_BAD_BLOCK:
                                parse_warn(token, 'Unknown block kind')
                    
                    flags = {}
                
                case keyword:
                    parse_error(token, 'Unknown keyword')
        
        elif not isinstance(token.t, TokenEOF):
            parse_error(token, 'Unexpected token')
    
    symbols_cache[name] = decls
    
    for target, include, token in env.symbols_includes:
        final = None
        
        if '(' in include:
            if not ')' in include or include.index(')') != len(include)-1:
                parse_error(token, 'Malformed specific inclusion')
            include, final = include[:-1].split('(', 1)
        
        include_decls = parse_decls(include)
        
        symbols = decls_get(include_decls, final, Symbols) if final != None else decls_get_default(include_decls, Symbols)
        
        if not symbols:
            parse_error(token, 'Could not retrieve symbols')
        
        target.update(symbols.mapping)
    
    return decls
    
decls = parse_decls(SYMBOLS_BASE)
# symbols = decls_get(decls, 'nodeadkeys', Symbols)
symbols = decls_get_default(decls, Symbols)
if not symbols:
    error('Could not retrieve symbols')
mapping = dict(symbols.mapping.items()) # dict(it for mp in symbols.mapping.maps for it in mp.items())

def export_c(mapping: dict[int, KeyData]):
    # for code, key in mapping.items():
    #     print(code, key.map)
    # TODO: Trim trailing 0's
    return '{' + ','.join('[' + str(code) + ']={' + ','.join(map(lambda v:str(v or 0), key.map)) + '}' for code, key in mapping.items()) + '}'
        
print(export_c(mapping))
