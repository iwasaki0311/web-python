import pyxel

from .fire import Fire


# フラワークラス
class FireFlower:
    # フラワーを初期化する
    def __init__(self, game, x, y):
        self.game = game  # ゲームクラス
        self.x = x  # X座標
        self.y = y  # Y座標
        self.fire_timer = 0  # 火の玉の発射タイマー

    # フラワーを更新する
    def update(self):
        # 火の玉の発射タイマーが0になったら花粉を発射する
        if self.fire_timer > 0:
            self.fire_timer -= 1
        else:  # 火の玉を発射する
            dx = self.game.player.x - self.x
            dy = self.game.player.y - self.y
            sq_dist = dx * dx + dy * dy
            if sq_dist < 60**2:  # プレイヤーとの距離が60未満の時
                # プレイヤーの方向に向けて速度1で火の玉を発射する
                dist = pyxel.sqrt(sq_dist)
                self.game.enemies.append(
                    Fire(self.game, self.x, self.y, dx / dist, dy / dist)
                )  # 火の玉を敵リストに追加



                # 火の玉の発射タイマーをリセットする
                self.fire_timer = 90

    # フラワーを描画する
    def draw(self):
        # 画像の参照X座標を決める
        u = pyxel.frame_count // 8 % 2 * 8 + 8
        # 8フレーム周期で0と8を繰り返す

        # 画像を描画する
        pyxel.blt(self.x, self.y, 0, u, 96, 8, 8, 15)
