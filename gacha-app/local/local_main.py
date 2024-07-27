import random

class Gacha:
    def __init__(self, items):
        self.items = items
    
    def roll(self):
        return random.choice(self.items)

# ガチャのアイテムリストを定義
items = [
    "SSR キャラクターA",
    "SSR キャラクターB",
    "SR キャラクターC",
    "SR キャラクターD",
    "R キャラクターE",
    "R キャラクターF",
    "N キャラクターG"
]

# ガチャオブジェクトを作成
gacha = Gacha(items)

# ガチャを回して結果を表示
print("ガチャを回します...")
result = gacha.roll()
print(f"結果: {result}")
