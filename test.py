print("hello world");
print("sain baina uu?");
ner = "たかし";print(ner);
mnd="sain uu?"; print(mnd);
x = 10;
if x > 5:
    print("5より大きいです");print("これもifの中身です");
print("これはifの外です");
for i in range(5):
    print("sain baina uu?");
for i in range(5):
    print(i);
for i in range(10):
    if i % 2 == 0:
        print(i);
for i in range(1,11):
    if i % 2 == 0:
        print(i);
# 🐍 Pythonのリスト（C言語の配列の進化系）
# 数字、文字、さらには別の変数（ner）まで1つの箱にまとめられます
my_list = [10, 20, "たかし", "sain uu?"];

# データの追加も1行で全自動（メモリの再確保とか不要！）
my_list.append("新しいデータ");
print(my_list);
names=["たかし", "ボルド", "ドルジ"];
for name in names:
    print(name);
for name in my_list:
    print(name);
