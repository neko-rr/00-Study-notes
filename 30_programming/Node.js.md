# Node.js
- JavaScriptを使ってサーバーサイド開発を行えるように設計された実行環境。
- 高速な処理性能と優れた拡張性を備え、リアルタイム通信をはじめとしたWebアプリケーションやAPI開発で広く利用されている
# フレームワーク：Express
Node.jsでWebアプリの開発をするためのフレームワーク
- ターミナルでダウンロードしてから
```
npm install express
```
```js
const express = require('express');
const app = express();
```
## ファイルを起動
app.js
```js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.render('hello.ejs');
});

// サーバーを起動するコードを貼り付けてください
app.listen(3000);
```
ターミナル（node ファイル名）
```
node app.js
```
## ルーティング
URLに対応する処理を実行することをルーティングと呼ぶ
```js
app.get('/TOP', () => {
  // TOP画面を表示
});
```
### req(リクエストの略)・res(レスポンスの略)
ルーティングの処理では、req(リクエストの略)・res(レスポンスの略)の２つの引数を受け取ります。reqやresには、リクエスト・レスポンスに関する情報が入っています。
### res.render
ルーティングの処理でres.renderと書くことで、指定したビューファイルをブラウザに表示できます。
### ビューファイル
ブラウザに表示する見た目部分にはEJSという形式のファイルを使い、viewsフォルダに配置します。以後、見た目を作るファイルをビューファイルと呼びます。
```
.
└── app
    ├── app.js
    └── views
        └── top.ejs
```
app.js
```js
app.get('/TOP', (req, res) => {
  res.render('top.ejs');
});
```
## CSSを適用
CSSや画像などを適用するには、まずこれらのファイルを置くフォルダを作ります。フォルダ名は自由ですが、一般的に使われるのは、public
```
.
└── app
    ├── app.js
    ├── views        // ブラウザの見た目ファイルを置く場所
    │   └── top.ejs
    └── public       // CSSや画像などを置く場所
        ├── CSS
        │   └── style.css
        └── images
```
app.js
```
// CSSや画像ファイルを置くフォルダを指定するコード
app.use(express.static('public'));
```
## EJSとは？
HTMLとJavaScriptのコード両方を記述できるNode.jsのパッケージ
- ターミナルに
```
npm install ejs
```
### JavaScriptのコードを記述する：<% %>または<%= %>で囲む
<% %>で囲んだ場合はブラウザに何も表示されないので、変数の定義などに用います。変数の値などをブラウザに表示したい場合は<%= %>を用います。
# 基本
