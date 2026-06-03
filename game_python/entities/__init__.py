# エンティティ(キャラクター)モジュール

# entitiesフォルダのクラスを__init__.pyでインポートすることで
#   from entities.player import Player
# のようにクラスを個別にインポートする代わりに
#   from entities import Player, Enemy1, Enemy2, Enemy3
# のようにまとめてインポートできるようにする

from .fireflower import FireFlower  # フラワークラス
from .chicken import Chicken  # マミークラス
from .player import Player  # プレイヤークラス
from .fire import Fire  # 花粉クラス
from .mob import Mob  # スライムクラス
