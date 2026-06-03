# 定数モジュール

SCROLL_BORDER_X = 80  # スクロール境界X座標
# プレイヤーがこの座標を超えたらスクロールさせる

# タイル種別
TILE_NONE = 0  
TILE_GEM = 1  
TILE_EXIT = 2  
TILE_MUSHROOM = 3  
TILE_SPIKE = 4  
TILE_LAVA = 5  
TILE_WALL = 6  
TILE_GOOMBA_POINT = 7  # クリボー出現位置
TILE_IRONBALL_POINT = 8  # 鉄球出現位置
TILE_CHICKEN_POINT = 9  # 鶏出現位置
TILE_FIREFLOWER_POINT = 10  # フラワー出現位置

# タイル→タイル種別変換テーブル
TILE_TO_TILETYPE = {
    (1, 0): TILE_GEM,
    (2, 0): TILE_EXIT,
    (3, 0): TILE_MUSHROOM,
    (4, 0): TILE_SPIKE,
    (5, 0): TILE_LAVA,
    (1, 2): TILE_WALL,
    (2, 2): TILE_WALL,
    (3, 2): TILE_WALL,
    (4, 2): TILE_WALL,
    (5, 2): TILE_WALL,
    (6, 2): TILE_WALL,
    (7, 2): TILE_WALL,
    (1, 3): TILE_WALL,
    (2, 3): TILE_WALL,
    (1, 4): TILE_WALL,
    (1, 5): TILE_WALL,
    (0, 9): TILE_GOOMBA_POINT,     # Y=9 : クリボー
    (0, 10): TILE_IRONBALL_POINT,  # Y=10: 鉄球
    (0, 11): TILE_CHICKEN_POINT,   # Y=11: 鶏
    (0, 12): TILE_FIREFLOWER_POINT,# Y=12: ファイアーフラワー
}
# このテーブルにないタイルはTILE_NONEとして判定する
