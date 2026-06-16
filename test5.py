# 現在の「回答するボタン」の処理をこう書き換えます
def check():
    global tensu, mondai_count, current_q
    
    user_ans = int(entry.get())
    correct_ans = eval(current_q) 
    
    if user_ans == correct_ans:
        tensu += 10
        label_result2.config(text="正解！")
        # --- ここがポイント！ ---
        # 10問目までは、正解した瞬間に自動で「次の問題」を表示する
        if mondai_count < 10:
            show_next_question() # 次の問題を出す関数を呼ぶ
    else:
        label_result2.config(text=f"不正解！答えは {correct_ans}")

# 別途、問題を表示するだけの関数を作る
def show_next_question():
    global mondai_count, current_q
    mondai_count += 1
    current_q = random.choice(q_list)
    label_result1.config(text=current_q)
    entry.delete(0, tk.END)
    label_result.config(text=f"残り {10 - mondai_count} 問")