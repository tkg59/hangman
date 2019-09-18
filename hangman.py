import random

def hangman(word):
    # 回答失敗のカウンター
    wrong = 0
    # 失敗数に応じたステージ(7段階)
    stages = ["",
              "_________         ",
              "|                 ",
              "|        |        ",
              "|        0        ",
              "|       /|\       ",
              "|       / \       "
              ]

    # 正解の文字列リスト
    rletters = list(word)
    # ヒント文字列
    board = ["_"] * len(word)
    # 勝敗のフラグ
    win = False

    #ゲーム開始
    print("ハングドマンへようこそ！")

    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1

        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))

ans_list = ["cat", "dog", "lion", "panda", "monky"]
hangman(ans_list[random.randint(0,4)])
