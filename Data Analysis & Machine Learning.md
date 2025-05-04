# フレームワーク
## TensorFlow
- 開発：Google
- 開発年：2015年
- 規模が大きいもの向き
- コミュニティが大きい
- 習得に時間かかる

## PyTorch
- 開発：Meta
- 開発年：2016年
- 小規模や研究向き
- コミュニティが大きい
- GPU上
- 人気急上昇でTensorFlowを追い抜かすかも
- 習得に時間かかる

## Keras
- 初心者向き
- 構文が分かりやすい
- ディープラーニングモデルを構築するための高レベルAPI
- 通常、TensorFlow等の低レベルライブラリ上で動作する（まず、TensorFlowのインストールが必要）

# 活性化関数
ReLU 関数は
Play video starting at :5: and follow transcript5:00
、 今日のネットワーク設計で最も広く使用されている活性化関数であり、その主な利点は、 すべてのニューロンを同時に活性化しないことです。 softmax 関数は、
Play video starting at :5:11 and follow transcript5:11
各入力のクラスを定義する確率を取得しようとしていた分類器の出力層で使用するのが理想的です。 シグモイド関数と双曲線正接関数は、
Play video starting at :5:18 and follow transcript5:18
勾配が消失する問題につながる可能性があるため、多くの用途で使われていません。 モデルを構築するときは、 まず ReLU 関数を使用し、ReLU
Play video starting at :5:27 and follow transcript5:27
関数のパフォーマンスが良くない場合は、他のアクティベーション関数に切り替えることができます。（courasera IBM)
