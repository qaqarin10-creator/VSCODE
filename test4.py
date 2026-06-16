import tkinter as tk;
import random;

# 1. 共通で使うメッセージ（文字）
hazure = "❌ ブブー！ハズレ！";
seikai = "🎉 正解！お見事！";

# 🌟 ボタン1（printf）が押されたときの動き
def click_button1():
    label_result1.config(text=hazure);
    label_result2.config(text="あと1回"); # 3択なので次はあと1回

# 🌟 ボタン2（print）が押されたときの動き
def click_button2():
    label_result1.config(text=seikai);
    label_result2.config(text="ゲームクリア！");

# 🌟 ボタン3（scanf）が押されたときの動き
def click_button3():
    label_result1.config(text=hazure);
    label_result2.config(text="あと1回");

# 2. アプリの「画面（ウィンドウ）」を作る
app = tk.Tk();
app.title("pythonクイズ");
app.geometry("500x400"); # 画面が大きすぎたので少しコンパクトに調整

# 3. 問題文
label_title = tk.Label(app, text="Pythonで画面に文字を出す命令は？", font=("MS Gothic", 16));
label_title.pack(pady=10);

# 4. 結果を表示するラベル
label_result1 = tk.Label(app, text="", font=("MS Gothic", 24, "bold"), fg="red");
label_result1.pack(pady=20);

label_result2 = tk.Label(app, text="あと2回", font=("MS Gothic", 24, "bold"), fg="red");
label_result2.pack(pady=20);

# 5. ボタンの配置（🌟カッコをつけずに、関数名だけを渡すのがルール！）
button1 = tk.Button(app, text="printf", command=click_button1);
button1.pack(pady=5);

button2 = tk.Button(app, text="print", command=click_button2);
button2.pack(pady=5);

button3 = tk.Button(app, text="scanf", command=click_button3);
button3.pack(pady=5);

# 6. アプリを起動
app.mainloop();