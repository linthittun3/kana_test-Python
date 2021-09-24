import random

print("Which one do you want to test? (H)iragana or (K)atakana: \nType (Q) for exit.")
command = ""

while command.upper() != "Q":
    command = input("> ")
    if command.upper() == "H":
        hiragana = ["あ","い","う","え","お",
                "か","き","く","け","こ",
                "さ","し","す","せ","そ",
                "た","ち","つ","て","と",
                "な","に","ぬ","ね","の",
                "は","ひ","ふ","へ","ほ",
                "ま","み","む","め","も",
                "や","ゆ","よ",
                "ら","り","る","れ","ろ",
                "わ","を","ん"
                ]
        nums_hira = len(hiragana)

        random_choice = random.randint(0, nums_hira - 1)
        random_hiragana = hiragana[random_choice]
        # random_hiragana = random.choice(hiragana)
        print(random_hiragana)

    elif command.upper() == "K":
        katakana = ["ア","イ","ウ","エ","オ",
                "カ","キ","ク","ケ","コ",
                "サ","シ","ス","セ","ソ",
                "タ","チ","ツ","テ","ト",
                "ナ","ニ","ヌ","ネ","ノ",
                "ハ","ヒ","フ","ヘ","ホ",
                "マ","ミ","ム","メ","モ",
                "ヤ","ユ","ヨ",
                "ラ","リ","ル","レ","ロ",
                "ワ","ヲ","ン"
                ]
        nums_kata = len(katakana)
        random_choice = random.randint(0, nums_kata - 1)
        random_katakana= katakana[random_choice]
        # random_katakana = random.choice(katakana)
        print(random_katakana)
    
    elif command.upper() == "Q":
        break
    else:
        print("Sorry, Please input valid characters!")
