# 基本
```CSS
セレクタ {
  プロパティ: 値;
}
```
- セレクタ：どこの部分にスタイルを適用したいかを、要素型セレクタ・classセレクタ・idセレクタなどで指定します。
  - 要素型セレクタ：象となるタグ名をそのまま記述　例：h1
  - classセレクタ：HTMLタグにclass名をつけることで、その要素に個別のスタイルを適用します。記述方法として、CSSではドット（.）の後にclass名を書き、その後に中括弧 {} の中にスタイルを記述
    - ※classには任意の名前を付与できますが、先頭に数字をつけることはできません。
  - idセレクタ：HTMLタグにid名をつけることで、その要素に個別のスタイル適用やページ内リンクの指定ができます。記述方法として、CSSではシャープ（#）の後にid名を書き、その後に中括弧 {} の中にスタイルを記述
    - ※idには任意の名前を付与できますが、先頭に数字をつけることはできません。
    - ※HTML文書内で、同じid名は1度しか使用できません。
    - idは1度しか使用できない特性から、ページ内リンクやJavaScriptのために使うのが主な目的です。 スタイルを指定するには、classセレクタを使うのが推奨されます。
- プロパティ：どのようなスタイルを適用するかを指定します（例：文字の色を指定する場合はcolor）。
- 値：プロパティに対して、値を設定します（例：文字の色を赤色に変更する場合はred)。
# 入れ子のセレクタ
「.header-list」の後にスペースを空けてliで、「header-list」の中の<li>要素にのみCSSを適用
```CSS
.header-list li {
  プロパティ: 値;
}
```
# 色
- 16進数：例：#FF0000　赤色
- RGB値：例：rgb(255, 0, 0)は赤色
- キーワード：例：red
## 例：カラーコードを使って、文字色を赤色にします
```CSS
<style>
.red {
    color: #f00;
}
</style>
<p class="red">文字の色が赤色になります。</p>
```
# フォントサイズ：font-size
- px：他の要素の影響を受けず、指定したピクセル数で文字の大きさを決定します。
- %：親要素の文字の大きさに対して、指定したパーセンテージで文字の大きさを決定します。
- em：親要素の文字の大きさに対して、指定した倍率で文字の大きさを決定します。
- rem：ルート要素（<html>タグ）の文字の大きさに対して、指定した倍率で文字の大きさを決定します。
# 文字の太さ:font-weight
- 数字（100~900の100刻み）
- キーワード（normal, bold, bolder, lighter）
- ```<h1>~<h6>```の要素は初期状態でfont-weight: bold;⇒font-weight: normal;と指定すれば文字が細くなる
# テキストや画像の横方向の配置を指定：text-align
- left：初期値。テキストや画像を左揃えにします。
- center：中央揃えにします。
- right：右揃えにします。
- justify：両端を揃えて配置（均等割付）します。
  - ※text-alignが効かない場合は、以下の2点を確認しましょう。
    - 適用させたいテキストや画像がブロック要素で囲まれているか(<div>、<p>など)
    - ブロック要素に対して指定しているか
# 文字間隔
主に、数値+pxまたは数値+emで指定します。
相対値であるemで記述すれば、文字のサイズを変更してもそれに応じたスペースが設定されます。
- 推奨の値は0.05〜0.1em(5%〜10%)。
```CSS
letter-spacing: 0.08em;
```
0.08emは相対値のため、文字サイズに対して8%の字間が空きます。
letter-spacingでは、相対的な比率で指定したほうが文字のバランスが良くなる傾向にあるため、em指定を推奨します。
# 行間
単位を使わず、数値のみで指定することが推奨されています。値が大きいほど行間が大きくなる。
- 1.5～2が一般的に見やすい数値とされています。
```CSS
line-height: 1.5;
```
- line-heightプロパティは本来行間を調整するためのプロパティですが、要素の縦方向の中央に文字を配置するのにも使えます。
- line-heightプロパティの「高さの中心」に文字が配置されるため、要素の高さとline-heightプロパティを同じ値にすると、文字がちょうど中央に配置されるようになります。
# フォントを指定する
複数のフォントを指定する
```CSS
font-family:Arial, Helvetica, sans-serif;
```
左から順番に、Webブラウザが最初に表示可能だと判断されたフォントが使用されます。
全てのフォントが表示できない場合には、代替フォントが使用されます。
# テキストの半角スペース、タブ、改行をどのように表示させるかを指定：white-space
```CSS
element {
  white-space: nowrap;
}
```
- normal: 初期値。テキスト内の連続するスペースやタブは1つの空白として扱われ、行は自動的に折り返されます。
- nowrap: 行の折り返しを防ぎ、一行で表示します。連続する空白文字はnormalと同様に1つにまとめられます。
  - ※<p>要素内のテキストがどんなに長くても改行されずに一行で表示されます。スクロールが必要になることがあります。
    - overflow-x: scroll;
- pre: テキスト内のすべての空白文字（スペース、タブ、改行）がそのまま表示されます。行の折り返しは行われません。
- pre-wrap: preと同様に空白文字をそのまま表示しますが、行は要素の幅に応じて自動的に折り返されます。
- pre-line: 改行はそのまま表示されますが、連続する空白文字は1つにまとめられます。行は自動的に折り返されます。
# 横並び：float
```CSS
float: left;
```
要素が左から順に横に並ぶ
## 左右に横並び
float: leftとfloat:rightを組み合わせることで、ロゴとリスト全体を左右に配置することができます。
左端に配置したい「footer-logo」にはfloat: left;を、右端に配置したい「footer-list」にはfloat: right;を指定しましょう。
# 背景
## 背景色：background-color
- rgba関数で透明度を指定する
- 背景色のみを透明にする⇔「opacity」には要素の中身全てを透明にする
```CSS
<p>背景色の透明度を指定する</p>

<style>
p {
  background-color: rgba(255 ,0, 0, 0.5);
}
</style>
```
## 背景画像：background-imageとbackground-size: cover;
- background-imageで指定された背景画像は図のように表示範囲を埋め尽くすまで、繰り返し表示される性質がある
- background-size: cover;を指定すると、1枚の画像で表示範囲を埋め尽くすように画像の大きさが拡大縮小します
```CSS
background-image: url(画像のURL);
background-size: cover;
```
# 枠線：border
borderで指定した太さの数値は、初期状態だとブロック要素のwidth、heightに加算されるため、意図せずレイアウトが崩れる可能性があります。 
box-sizingの値であるborder-boxを合わせて指定することで、ブロックの横幅と高さにborderのサイズを含めることができます。
# ボックスに影：box-shadow
値は半角スペースで区切り、下記の順番で指定します。
- ① 横の位置
- ② 縦の位置
- ③ ぼかし
- ④ 広がり
- ⑤ 色
- ⑥ inset（指定すると影が内側に追加されます）
- ①〜②の設定は必須で、③〜⑥の設定は任意です。正の値を指定すると、右と下に影がつきます。反対に、マイナス値の場合、左と上に影がつきます。
```CSS
box-shadow: 5px 5px 20px -5px #cdcdcd;
```
右下に影を追加する
# 要素に透明度をつける：opacity
透明度は0.0(完全に透明) ~ 1.0(完全に不透明)の数値で指定
- 表示させた要素を透明にします
```CSS
<div class='opacity-ex'>
  <p> 透明になります</p>
</div>

<style>
  .opacity-ex {
    background: rgba (132, 127, 127, 1);
    opacity: 0;
  }
/* 要素全体が透明になるので、p要素「透明になります」や背景色が見えなくなる。rgba()との違いに注意 */
</style>
```
- opacityは要素全体の透明度を指定します。そのため、要素内の背景や文字だけを薄くしたい場合は、個別にrgba()で記述する必要があります。
- opacity: 0;とdisplay:none;も似ていますが、opacityは非表示でなく透明になるだけなので、 要素の領域は残ります。 そのため、クリックなどのアクションができるといった違いがあります。
# 要素の角を丸くする：border-radius
数字が大きいほど角が丸くなる
```CSS
border-radius: 10px;
```
# 要素の横幅を指定：width
- ブロック要素への指定
  - display: blockが指定されている要素（divタグ、pタグなど）の場合、widthを指定しないと初期値のautoが適用され、自動的に横幅いっぱいになります。
- インラインブロック要素への指定
  - display: inline-blockが指定されている要素の場合、中身の長さに対して幅が決まります。
  - 横幅を変更したい場合はwidthを指定する必要があります。
- インライン要素への指定
  - 通常、display: inlineが指定されている要素（aタグ、spanタグなど）には、widthを指定することができません。（例外として、imgタグはインライン要素ですが、widthを指定できます）
  - 横幅を変更したい場合、あらかじめdisplay: blockまたはdisplay: inline-blockを指定しておきましょう。
# 要素の最大幅：max-width
主にレスポンシブ対応で使用し、閲覧環境によって要素が大きくなりすぎたり、収縮しすぎてしまうことを防ぎます。
要素の高さは幅に合わせて調節されるため、縦横比を維持するためにheight: auto;をセットで指定します。
- 例1：画面幅が変わっても500px以上にならないようにする場合
  - 画面幅に合わせて親要素の80%で伸縮しますが、500px以上は大きくなりません。
```CSS
.box {
    親要素の80%の幅width: 80%;
    最大幅を500pxに制限max-width: 500px;
    height: 100px;
    background-color: #74992e;
  }
```
```HTML
<div class="box"></div>
```
- 例2：画像をブラウザ画面の幅に収める場合
```CSS
img {
    max-width: 100%; 
    height: auto;
  }
```
# 要素の内側の余白：padding
- padding-top: 上側
- padding-right: 右側
- padding-bottom: 下側
- padding-left: 左側
```CSS
padding: 10px; /* 要素内の上下左右10px */
padding: 10px 20px; /* 要素内の上下に10px・左右に20px */
padding: 10px 20px 30px; /* 要素内の上10px・左右20px・下30px */
padding: 10px 20px 30px 40px; /* 要素内の上・右・下・左(時計回り)で指定 */
```
# 要素の外側の余白を指定：margin
```CSS
margin: 10px; /* 上下左右に10px */
margin: 10px 20px; /* 上下に10px・左右に20px */
margin: 10px 20px 30px; /* 上10px・左右20px・下30px */
margin: 10px 20px 30px 40px; /* 上・右・下・左(時計回り)で指定 */
```
- ボックスを画面の水平方向で中央に配置する
  - 文章や画像を水平方向で中央に配置したいときには、margin: autoを使います。ただし、ボックスの幅を設定する必要があります。なぜなら、ボックスの幅が設定されていないと、ボックスは全幅を占め、margin: autoは効果がないからです。containerクラスを作ると便利です。
```CSS
width: 200px;
margin: 0 auto;
```
# 箇条書きの設定
- ```<ul>,<ol>,<li>```の箇条書きリストのスタイルを一括指定できます。
- 値は半角スペースで区切って記述するか、個々に記述したい場合は次のプロパティを使用します。

- list-style-type：リストの先頭についているマーカーの見た目を変更する際に使用します。
  - disc：黒丸（ulとliの初期値）
  - decimal：数字（olの初期値）
  - circle：中空円
  - none：表示しない
- list-style-image：マーカーを画像で指定します。url(画像パス）で記述します。
- list-style-position:マーカーの位置を指定します。
- outside：リストボックスの外側に配置します。（初期値）
- inside：リストボックスの内側に配置します。
# 擬似クラス
## 特定の順番にある要素を選択する：:nth-child()
- evenは、偶数の要素を表します。
- oddは、奇数の要素を表します。
- nを使って、倍数番目の要素を選択することもできます。
  - 例えば、2の倍数番目の要素を選択する場合は2n、3の倍数番目の要素を選択する場合は3nとなります。
```HTML
<style>
li:nth-child(even) {
  color: red;
}
li:nth-child(odd) {
  color: blue;
}
</style>
<ul>
  <li>List1</li>
  <li>List2</li>
  <li>List3</li>
  <li>List4</li>
</ul>
```
## 要素の最初の子要素と最後の子要素を選択する：:first-childと:last-child
## 特定の条件を満たさない要素を選択する：:not()
```CSS
p:not(.not-blue) {
  color: #0066ff;
}
```
## 特定の要素が他の要素を含んでいるかどうかをチェックする：:has()
:has()と隣接兄弟結合子の+を使うと直後に特定の要素を持つ要素に対してスタイルを適用することができます。
```HTML
<style>
h3:has(+p) {
  color: red;
}
</style>
<h2>ここの文字色は変わりません。</h2>
<p>ここはh2要素の兄弟要素になります。</p>

<h3>ここの文字色は赤くなります。</h3>
<p>ここはh3要素の兄弟要素になります。</p>
```
## 複数のセレクタ（選択子）をまとめて書くための便利な機能：:is()
- :is()の中に複数のセレクタをカンマ,で区切って書くと、そのどれかに当てはまる要素全てに対してスタイルを適用できます。
- 一般的には、可読性を保つために適切な数にまとめることが推奨されます。実用的には、数十個程度までなら問題なく使えるでしょう。
```CSS
section > h1,
section > h2,
section > h3 {
  color: #333333;
}

↓↓ コードを省略

section:is(h1, h2, h3) {
  color: #333333;
}
```
## 複数の選択肢から一つを選ぶ：:where()
ただし、:where() 内のセレクターは詳細度が 0 になります。
これは、他のスタイルの優先順位が:where()の中のルールよりも強くなることを防ぐためです。
:is()
:where()
これらは、どちらも複数のセレクタをグループ化するための便利な関数です。
ただし、これらの関数の大きな違いはスタイルの優先順位です。

:is()は引数内のセレクタの優先度を保持します。
一方、:where()はその優先度を 0 にリセットします
```HTML
<style>
/* :is()では全部ピンクに設定 */
.isContent :is(.text1, .text2) {
  color: pink;
}

/* :where()では全部オレンジに設定 */
.whereContent :where(.text1, .text2) {
  color: orange;
}

/* .text2を緑色に上書き */
.text2 {
  color: green;
}
</style>

<div class="isContent">
  <p class="text1">:is()のText1</p>
  <p class="text2">:is()のText2</p>
</div>
<div class="whereContent">
  <p class="text1">:where()のText1</p>
  <p class="text2">where()のText2</p>
</div>
```
## マウスカーソル（マウスポインター）を要素の上でかざした時に指定したスタイルを反映させる：:hover
- リンクを作成するaタグと一緒に使われることが多い擬似クラスです。
- セレクタ:hoverとすることで、カーソルが乗ったときのCSSを指定する
```CSS
a:hover {
    color: red;
}
```
例1: ボタンにマウスカーソルを合わせると色が変わります
```CSS
<style>
.button {
  border: 1px solid #000;
  color: #fff;
  background-color: blue;
  padding: 10px;
  border-radius: 20px;
  text-decoration: none;
}
.button:hover {
  background-color: red;
}
</style>
<a class="button" href="#">ボタン</a>
```
## 要素が選択された強調：:focus
例えば、テキストボックスをクリックすると、そのボックスの枠が強調されることがあります。
## 要素が選択された強調：:active
要素がクリックされている間だけCSSを適用することができる
## 個別の辺（上、下、左、右）に対してボーダーの幅、スタイル、色を指定するための便利なショートハンド：border-[上下左右]
```HTML
<style>
div  {
  width: 100px;
  height: 100px;
  border-top: 1px solid red;
  border-right: 1px solid #333;
  border-bottom: 1px solid #333;
  border-left: 1px solid #333;
}
</style>
<div></div>
```
# HTML要素の表示方法を指定するプロパティ:display
block,inline,inlineblock,noneの4種類
## display: block;
要素をブロックに指定します。（<div>や <h1> はデフォルトでblock）
## display: inline;
要素をインラインに指定します。（ <a> <img> はデフォルトでinline）
## display: inline-block;
要素をインラインブロックに指定します。
## display: none;
要素をブラウザ上で非表示にします。
レスポンシブで表示切り替えしたい時などに使用します
```CSS
.element{
 display: none;
}
```
- ```<a>```タグはインライン要素なので、中身のテキストの部分しか大きさを持ちません。その結果、<a>タグをクリックできる範囲はテキストの部分だけになってしまいます。
- ```<a>```タグをブロック要素にすると、大きさが親要素いっぱいに広がるので、全体をクリックできるようになり
# 装飾
## <span>タグ
<span>タグで囲まれたテキストに、特定のスタイルを適用
- 文字に下線を引く
```HTML
<span>対象</span>
```
```HTML
<style>
  span{
 text-decoration: underline;
}
</style>
```
# 表の装飾
## テーブルのセルの境界線（ボーダー）をどのように表示するかを指定：border-collapse
<table>タグに対し、border-collapseプロパティを指定します。
テーブルのセルの境界線を表示する方法には、
- border-collapse: collapse;
- border-collapse: separate;

- border-collapse: collapse;を指定することで、テーブルのセルの境界線を重ねて表示することができます。
```CSS
  table {
    border-collapse: collapse;
    width: 100%;
  }
```
- border-collapse: separate;を指定することで、テーブルのセルの境界線を分けて表示することができます。
```CSS
  table {
    border-collapse: separate;
    width: 100%;
  }
```
## 罫線の装飾
- border: テーブルやセルの境界線の太さ、スタイル、色を指定します。
- border-spacing: border-collapse: separate;の場合、セル間のスペースを設定します。
- padding: セル内のコンテンツと境界線の間の余白を調整します。
# アニメーション：transition
「変化の対象」や、「変化にかかる時間」などを指定できます。
「変化の対象」にはcolorなどのプロパティを指定しますが、allを指定すると全てのプロパティに適用出来ます。
transitionは多くの場合hoverと組み合わせて使います。
```CSS
transition:all 0.5s;
```
# 要素同士重ねる：position:
- HTMLの要素同士は通常重なって表示されることはありませんが、position: absolute;を使うと、要素同士を重ねて表示することが出来ます。
- サイト全体の左上部分を基準とし、そこからの位置をtopとleftを用いて指定します。また、rightやbottomを併用することも可能です。
- 基準としたい親要素にposition: relative;と指定すると、その要素の左上部分が基準位置となります。

- 常に要素を画面上の指定した位置に固定させておくことができる。例：ヘッダー等：position: fixed;
  - 位置は、top、left、right、bottomを使って指定
  - positionを使用すると要素の重なりが生じます。その結果、コンテンツ部分とヘッダーが重なった時に、ヘッダーが隠れてしまいます。重なり順を指定して、ヘッダーが上に表示されるようにする：z-index
```CSS
position: fixed;
z-index:10;
```
## 重なり順調整：z-index
- 整数値で指定し、値が大きいほど上に表示される
- z-indexプロパティは必ずpositionプロパティと併用する必要がある
# 使用例・使い分け
## 中央寄せ
containerクラスのように、広い範囲を囲うようなブロック要素の場合はmarginを、テキストやボタンのようなインライン要素・インラインブロック要素の場合はtext-alignを使う

# レイアウトパータン
# カード型レイアウト
ブログ記事や商品紹介などの情報を見やすく整理するためのレイアウト
- 画像: 記事の内容を視覚的に示す役割を果たします。
- タイトル: 各カードのタイトルを表示します。
- 概要: 記事の短い概要や抜粋を表示します。
- 詳細リンク: 「続きを読む」や「詳細を見る」などのリンクを設置し、ユーザーが完全な記事にアクセスできるようにします。
```HTML
<div class="card">
  <img src="https://picsum.photos/200/150" alt="ブログ画像">
  <div class="container">
    <h4><b>ブログタイトル</b></h4>
    <p>ブログの概要説明文</p>
    <a href="article.html">続きを読む</a>
  </div>
</div>

<style>
 .card {
   border: 1px solid #ccc;
   padding: 16px;
   margin: 16px;
   border-radius: 8px;
   box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
   width: 200px;
   text-align: center;
 }
 .card img {
   max-width: 100%;
   height: auto;
 }
</style>
```
# ボタンを押したらへこむように見える
ボタンを押したときに以下の処理をすると、へこんで見えるようになります。
- 影を消す＝box-shadowをnoneにする
- ボタンの位置を影の分だけ下げる＝position: relative;とtopによって影の分だけ位置を下げる


