import customtkinter as ctk

# 1. 画面全体のテーマとカラー設定
# 'System'はOSの設定に合わせる（ライト/ダーク）
# 'blue'はアクセントカラー（ボタンの色など）
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class CustomLayoutApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- サイズとタイトルの設定 ---
        # 画像の縦長デザインに合わせて縦長に設定
        self.geometry("380x600")
        self.title("計算ドリル")

        # ウィンドウの余白（内側）
        self.grid_columnconfigure(0, weight=1)  # 全体を中心に配置
        self.root_pady = 20
        self.root_padx = 20

        # --- 各部品の共通フォント設定 ---
        # これで毎回指定する手間を省く
        self.font_m = ("Meiryo", 14)          # 標準
        self.font_l = ("Meiryo UI", 16, "bold") # 大・太字

        # --- 1. ラベル 1 (上部) ---
        self.label1 = ctk.CTkLabel(self,text="次の問題を解け",font=self.font_l,anchor="w") # 左寄せ
        self.label1.pack(fill="x", padx=self.root_padx, pady=(self.root_pady, 10))

        # --- 2. ラベル 2 (中央の大きな表示エリア) ---
        # 画像のデザインに合わせてフレーム（枠）で囲んで大きく表示
        self.display_frame = ctk.CTkFrame(self,corner_radius=10,border_width=1,border_color="gray50") # 枠線の色
        self.display_frame.pack(fill="both", expand=True, padx=self.root_padx, pady=10)

        self.label2 = ctk.CTkLabel(self.display_frame,text="ラベル 2\n(ここを大きく表示エリアにします)",font=self.font_m,text_color="gray80") # 少し薄い色に
        self.label2.pack(fill="both", expand=True, padx=20, pady=20)

        # --- 3. 入力欄 ---
        self.entry = ctk.CTkEntry(self, placeholder_text="入力欄 (テキストを入力してください)",font=self.font_m,height=40,corner_radius=8)
        self.entry.pack(fill="x", padx=self.root_padx, pady=(20, 10))

        # --- 4. ボタンエリア (横並び) ---
        # 3つのボタンを横に並べるためのフレーム
        self.button_frame = ctk.CTkFrame(self,fg_color="transparent") # フレーム自体の色をなくす
        self.button_frame.pack(fill="x", padx=self.root_padx, pady=(10, self.root_pady))

        # ボタンを均等に配置するための設定
        self.button_frame.grid_columnconfigure(0, weight=1, pad=10) # 余白
        self.button_frame.grid_columnconfigure(1, weight=1, pad=10)
        self.button_frame.grid_columnconfigure(2, weight=1, pad=10)

        # ボタン 1
        self.button1 = ctk.CTkButton(self.button_frame,text="ボタン 1",font=self.font_m,height=40,command=self.button1_click) # 機能
        self.button1.grid(row=0, column=0, padx=(0, 5))

        # ボタン 2
        self.button2 = ctk.CTkButton(self.button_frame,text="ボタン 2",font=self.font_m,height=40,command=self.button2_click) # 機能
        self.button2.grid(row=0, column=1, padx=5)

        # ボタン 3
        self.button3 = ctk.CTkButton(self.button_frame,text="ボタン 3",font=self.font_m,height=40,command=self.button3_click) # 機能
        self.button3.grid(row=0, column=2, padx=(5, 0))

    # --- ボタンの機能 (関数) ---
    def button1_click(self):
        print("ボタン 1 が押されました")
        self.label2.configure(text="ボタン 1 が押されました！")

    def button2_click(self):
        input_text = self.entry.get() # 入力欄の文字を取得
        self.label2.configure(text=f"入力欄の文字: {input_text}")

    def button3_click(self):
        self.label2.configure(text="表示をリセットしました")
        self.entry.delete(0, 'end') # 入力欄を消去

# アプリの起動
if __name__ == "__main__":
    app = CustomLayoutApp()
    app.mainloop()