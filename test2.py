import random;

def play_game():
    # パソコンが 1 〜 10 の中からランダムで答えを決める
    answer = random.randint(1, 10);
    print("【数字当てゲーム】1から10までの数字を当ててみてね！");

    # 3回 チャンスを与えるループ
    for chance in range(1, 4):
        # プレイヤーの予想（今回は毎回 7 と予想したと仮定します）
        # ※明日はここをキーボード入力に変えます！
        guess = int(input(str(chance) + "回目の予想を入力してね: "));

        # 判定
        if guess == answer:
            print("🎉 大正解！おめでとう！");
            return; # 正解したらその時点で関数を終了（関数を閉じる）
        else:
            print("❌ ハズレ！");

    print("💀 ゲーーームオーバー！正解は " + str(answer) + " でした。");

# ゲームを実行！
play_game();
