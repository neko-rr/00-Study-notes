# メディアクエリ（Media Queries）
- @media (条件) { .... }
- 指定された条件が当てはまるときにのみ{ }内のCSSが適用
# max-width(最大幅)、min-width(最小幅)
- max-width: ◯◯pxと指定すると、画面幅が◯◯px以下の時にCSSを適用できます。min-widthはその反対となります。
- max-width: ◯◯px（またはmin-width: ◯◯px）のようにメディアクエリの条件を指定するとき、「◯◯px」の部分をブレイクポイントと呼ぶ
  - 例：スマートフォンの画面幅は670px以下、タブレットの画面幅は670px ~ 1000pxと想定して、ブレイクポイントを設定
# レイアウト崩れを直す
- itemクラスのwidthが25%で指定されているため、左右のpaddingを追加すると要素の幅の合計が100%を超えてしまい、レイアウトが崩れてしまっています。このようなレイアウト崩れは、box-sizing: border-box;を用いることで防ぐことができます。
- box-sizingをborder-boxに指定すると、要素の幅(width)の合計にpaddingとborderが含まれるようになります。そのため、paddingやborderを追加した時に生じるレイアウト崩れを未然に防ぐことができます（※ただし、marginはborder-boxでの合計値に含まれません）。
- box-sizing: border-box;を指定するときは、*(アスタリスク)に対して指定することが推奨されています。
*はすべての要素に対してCSSを適用したい場合に用います。
border-boxをすべての要素に対して適用することで、レイアウトを管理しやすくなります。
```CSS
* {
  box-sizing: border-box;
}
```


