import customtkinter as ctk
import random

# 1. 画面全体のテーマとカラー設定
# 'System'はOSの設定に合わせる（ライト/ダーク）
# 'blue'はアクセントカラー（ボタンの色など）
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class CustomLayoutApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.is_problem_active = False #まだ何も画面が表示されていない状態
        self.mondaisuu=0
        self.seikaisuu=0

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
        self.label3= ctk.CTkLabel(self,text="正解率??%",font=self.font_m,anchor="e")
        self.label3.pack(fill="x",padx=self.root_padx)

        # --- 2. ラベル 2 (中央の大きな表示エリア) ---
        # 画像のデザインに合わせてフレーム（枠）で囲んで大きく表示
        self.display_frame = ctk.CTkFrame(self,corner_radius=10,border_width=1,border_color="gray50") # 枠線の色
        self.display_frame.pack(fill="both", expand=True, padx=self.root_padx, pady=10)

        self.label2 = ctk.CTkLabel(self.display_frame,text="1.出題ボタンを押す\n2.回答を入力する\n3.答え合わせを押す",font=self.font_m,text_color="black") # 少し薄い色に
        self.label2.configure(anchor="nw", justify= "left")
        self.label2.pack(fill="both", expand=True, padx=20, pady=20)

        # --- 3. 入力欄 ---
        self.entry = ctk.CTkEntry(self, placeholder_text="入力してエンターキー",font=self.font_m,height=40,corner_radius=8)
        self.entry.pack(fill="x", padx=self.root_padx, pady=(20, 10))
        # ★Enterキーと紐付ける
        self.entry.bind("<Return>", lambda event: self.show_answer())

        # --- 4. ボタンエリア (横並び) ---
        # 3つのボタンを横に並べるためのフレーム
        self.button_frame = ctk.CTkFrame(self,fg_color="transparent") # フレーム自体の色をなくす
        self.button_frame.pack(fill="x", padx=self.root_padx, pady=(10, self.root_pady))

        # ボタンを均等に配置するための設定
        self.button_frame.grid_columnconfigure(0, weight=1, pad=10) # 余白
        self.button_frame.grid_columnconfigure(1, weight=1, pad=10)
        self.button_frame.grid_columnconfigure(2, weight=1, pad=10)

        # ボタン 1
        self.button1 = ctk.CTkButton(self.button_frame,text="出題",font=self.font_m,height=40,command=self.button1_click) # 機能
        self.button1.grid(row=0, column=0, padx=(0, 5))

        # ボタン 2
        self.button2 = ctk.CTkButton(self.button_frame,text="答え合わせ",font=self.font_m,height=40,command=self.button2_click) # 機能
        self.button2.grid(row=0, column=1, padx=5)

        # ボタン 3
        self.button3 = ctk.CTkButton(self.button_frame,text="リセット",font=self.font_m,height=40,command=self.button3_click) # 機能
        self.button3.grid(row=0, column=2, padx=(5, 0))
    
      
        

    #数列の添え字に変換        
    def to_subscript(self, n):
        subs = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return str(n).translate(subs) 
        
    # --- ボタンの機能 (関数) ---
    def button1_click(self):
        if self.is_problem_active==True:
            print("まずは今の問題を解いてください！")
            return

        self.a1=random.randint(-9,9)
        self.p=random.randint(-9,9)
        self.q=random.randint(-9,9)
        self.n=random.randint(2,9)

        #特性方程式の計算
        alpha=self.q/(1-self.p)
        if self.p!=1:
            self.answer=(self.a1-alpha)*self.p**(self.n-1)+alpha
        else:
            self.answer=self.a1+self.q*(self.n-1)  
        
        #数式のUI出力
        if self.q == 0:
            q_str = ""
        elif self.q > 0:
            q_str = f"+{self.q}"
        else:
            q_str = str(self.q)

        if self.p == 0:
            formula = f"aₙ₊₁={self.q}"
        elif self.p == 1:
            formula = f"aₙ₊₁=aₙ{q_str}"
        elif self.p == -1:
            formula = f"aₙ₊₁=-aₙ{q_str}"
        else:
            formula = f"aₙ₊₁={self.p}aₙ{q_str}"

        current_text = self.label2.cget("text")
    
        if current_text == "1.出題ボタンを押す\n2.回答を入力する\n3.答え合わせを押す":
            n_sub = self.to_subscript(self.n)
            updated_text = formula +"  " +f"a₁={self.a1}"+"このとき" + f"a{n_sub}"+"は？"
        else:
            n_sub = self.to_subscript(self.n)
            updated_text = current_text + "\n" + formula +"  "+f"a₁={self.a1}" +"このとき" + f"a{n_sub}"+"は？"
        print("ボタン 1 が押されました")
        self.label2.configure(text=updated_text)

        self.is_problem_active = True #回答スイッチオン

    def show_answer(self, event=None):
        self.kaitou=self.entry.get().strip()
        if self.kaitou=="":
            return
        
        if self.is_problem_active == False:
            print("まずは出題を押して問題を出してください!")
            return
                    
        current_text = self.label2.cget("text")
        updated_text = current_text + "\n" + self.kaitou
        print("回答が入力されました")
        self.label2.configure(text=updated_text)
        self.entry.delete(0, 'end')

    def button2_click(self):
        if not self.is_problem_active:
            return
        
        if not hasattr(self, 'kaitou'):
            self.kaitou = self.entry.get().strip()

        self.mondaisuu += 1 # 1回増やす

        
        if self.kaitou!="" and int(self.kaitou)==int(round(self.answer)):
            self.seikaisuu=self.seikaisuu+1
            current_text = self.label2.cget("text")
            updated_text = current_text + "\n" + "正解"
            self.label2.configure(text=updated_text)

        else:
            current_text = self.label2.cget("text")
            updated_text = current_text + "\n" + f"不正解 答えは {int(round(self.answer))}"
            self.label2.configure(text=updated_text) 
            
    
        self.seitouritsu=self.seikaisuu/self.mondaisuu*100
        self.label3.configure(text=f"正答率{round(self.seitouritsu)}%")
        self.is_problem_active = False

    def button3_click(self):
        self.label2.configure(text="1.出題ボタンを押す\n2.回答を入力する\n3.答え合わせを押す")
        self.entry.delete(0, 'end') # 入力欄を消去
        self.mondaisuu=0
        self.seikaisuu=0
        self.label3.configure(text="正解率??%")
        # 3. ★ここが最重要：状態変数を完全にクリアする
        self.is_problem_active = False # 出題中フラグを強制的にオフ
        
        # 4. 過去のデータも完全に消去
        if hasattr(self, 'kaitou'):
            del self.kaitou
        if hasattr(self, 'answer'):
            del self.answer
    

# アプリの起動
if __name__ == "__main__":
    app = CustomLayoutApp()

    app.mainloop()