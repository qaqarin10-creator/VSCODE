import tkinter as tk;
import random;

# 1. ボタンが押されたときの「動き（関数）」を決める
def draw_omikuji():
    fortunes = ["大吉 🌟", "中吉 👍", "小吉 🙂", "吉 🎯", "凶 👻"];
    result = random.choice(fortunes); # リストからランダムに1つ選ぶ
    label_result.config(text=result); # 画面の文字を書き換える

# 2. アプリの「画面（ウィンドウ）」を作る
app = tk.Tk();
app.title("おみくじアプリ");
app.geometry("300x200"); # 横300ピクセル × 縦200ピクセルのサイズ

# 3. 画面に「文字（ラベル）」を置く
label_title = tk.Label(app, text="今日の運勢は？", font=("MS Gothic", 16));
label_title.pack(pady=10);

# 4. 結果を表示するための「空の文字（ラベル）」を置く
label_result = tk.Label(app, text="???", font=("MS Gothic", 24, "bold"), fg="red");
label_result.pack(pady=20);

# 5. 画面に「ボタン」を置く（押されたら上の関数を動かす）
button = tk.Button(app, text="おみくじを引く", command=draw_omikuji);
button = tk.Button(app, text="おみくじを引く", command=draw_omikuji);
button.pack();

# 6. アプリを起動して、画面を表示し続ける
app.mainloop();