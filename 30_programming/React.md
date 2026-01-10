# Reactとは
- コンポーネント:小さな部品(HTML・CSS・JavaScript一纏め)を階層構造で組み立てる
- コンポーネント1つに付き1ファイルにする
- インポートとエクスポート必須
- コンポーネントとファイル名を揃えるのが基本
# コンポーネント
exportを前に付ける事で他のファイルから参照可能
# JXS記法
- returnの中は、1つのタグで囲う必要がある（return内に複数の要素があるとエラーになる）
  - ```<div></div>```や```<h1></h1>```
    - 複数の要素がある場合は、```<div>```タグで囲んで、1つの要素にまとめ
  - 回避のためにReact限定の空タグがある<></>
- BABELが、本来JavaScriptで無いコードをJavaScriptに変換してくれている(**HTMLのように書ける**)
- ```<br />```のような自己終了タグは明示的に閉じる必要がある
- コンポーネントは、単一のトップレベル要素しか返せない
## JXSのコメント
- JSXを{/* */}で囲むと、その部分はコメントになる
- 正しくコメントにできている場合は、囲んだ部分が灰色になる
## imgタグの注意点
- imgタグは、HTMLでは、```<img src='画像のURL'>```のように閉じタグが必要ありませんでした。
一方、JSXでは閉じタグが必要になります。```<img src='画像のURL' />```のように、タグの終わりにスラッシュ「/」を記述します。
# App.jsの構成
- App.jsファイル
- JSXとJS ( JavaScript ) の記述部分は分かれている。renderメソッドのreturn内のみ、JSXで記述する必要がある。JSXで記述された要素はブラウザに表示される
  - renderメソッドの、returnの外にはJavaScriptを記述可能
  - returnの中でも、JSXにJavaScriptを埋め込むことが可能
    - JavaScriptの部分を中括弧{ }で囲む
    - タグの属性の値も、同様に中括弧{ }を使ってJavaScriptを記述することが可能
```js
// Reactをインポート
import React from "react";

// Appクラスを定義
class App extends React.Component{
  render(){
    return (
      <h1>Hello React</h1>
    );
  }
}

// Appクラスをエクスポート
export default App;
```
JavaScriptの使用例
```js
import React from 'react';

class App extends React.Component {
  render() {
    const name = "ねこ";
    const imgUrl = "画像URL.png";
    
    return (
      <div>
        <h1>{name}</h1>
        <img src={imgUrl}/>
        
      </div>
    );
  }
}

export default App;
```
# state

# props
動的情報



# 実装
# Node.js
React + Viteの開発にはバージョン18以上のNode.jsが必要
# Vite（ヴィート）
Viteとは、モダンなフロントエンド開発ツール
- 高速な開発サーバー起動
- 効率的なHMR（Hot Module Replacement）
- 最適化された本番ビルド
- 豊富なプラグインエコシステム
## Viteプロジェクトの作成

# Next.js + Tailwind CSS プロジェクトのセットアップ
```sh
npx create-next-app@latest nextjs-tailwind-tutorial --typescript --tailwind --eslint
```
- 基本的にはEnterキーを押してデフォルトの選択肢で進めて問題ありません
- コマンドが完了すると、nextjs-tailwind-tutorialという名前のフォルダが作成されます。VS Codeでこのフォルダを開きましょう。
- 作成されたプロジェクトでは、すでにTailwind CSSを使うための設定が完了しています。
- tailwind.config.ts: Tailwind CSSのカスタマイズを行う設定ファイルです。
- app/globals.css: Tailwind CSSの基本的なディレクティブ（@tailwind base;など）が記述されています。
- app/layout.tsx: app/globals.cssがインポートされ、アプリケーション全体に適用されています。
```PowerShell
npx create-next-app@latest 作成予定のフォルダ `
    --ts `
    --eslint `
    --app `
    --src-dir `
    --tailwind `
    --import-alias "@/*" `
    --no-turbopack
```
既存フォルダに作成
```PowerShell
cd 既存フォルダパス
npx create-next-app@latest . --ts --tailwind --eslint --app --src-dir --import-alias "@/*"
```
# ローカルサーバ起動
```PowerShell
npm run dev
```
変更確認時等にすでに動いている Next.js を止める
```PowerShell
taskkill /F /IM node.exe
```



