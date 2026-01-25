# Reactとは
- App.jsに書かれているJSXは最終的にHTMLに変換されて、ブラウザに表示される。Reactのコードを実際にブラウザに表示するには、App.js以外にもindex.jsとindex.htmlというファイルが必要
- index.js内で「ReactDOM.render(<App />, ...」と書くことで、App.jsのJSXが、HTMLに変換される（定型文）
  - さらに「..., document.getElementById('id名'));」と書くことで、変換されたHTMLがindex.htmlの指定したid名の要素の中に挿入される。今回は、id名rootを指定しています。最終的に、index.htmlの内容がブラウザに表示される。
  - index.html内でstylesheet.cssを読み込むことで、CSSを適用することが可能
- 表示の流れ：コンポーネント.js⇒app.js（挿入）⇒index.js（変換）⇒index.html（挿入）
```
.
└── React
    ├── src
    │   ├── components
    │   │   ├── app.js
    │   │   └── コンポーネント毎の.js
    │   └── index.js
    └── index.html
```
## index.jsx定型文
- React 18 で導入された新しいルート API（createRoot）を使っている
- createRootは画面の特定の部分を管理するための準備をし、root.renderはその部分に実際に表示したい内容を描き出します。
```jsx
import React from 'react';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```
【アプリケーションの更新】
- ウェブアプリケーションの内容を更新したいときに、どの部分を新しくするかを指定して、効率よく画面を変えるために使います。
- ウェブページの中のidがappという部分にMyComponentという新しい内容を表示します。これにより、ページ全体を再読み込みすることなく、特定の部分だけを更新できます。
```jsx
import React from 'react';
const root = ReactDOM.createRoot(document.getElementById('app'));
root.render(<MyComponent />);
```
React 17 以前の古いレンダリング方式（ReactDOM.render）（非推奨）
```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';

ReactDOM.render(<App />, document.getElementById('root'));
```
# JXS記法
- returnの中は、1つのタグで囲う必要がある（return内に複数の要素があるとエラーになる）
  - ```<div></div>```や```<h1></h1>```
    - 複数の要素がある場合は、```<div>```タグで囲んで、1つの要素にまとめ
  - 回避のためにReact限定の空タグがある<></>
- BABELが、本来JavaScriptで無いコードをJavaScriptに変換してくれている(**HTMLのように書ける**)
- ```<br />```のような自己終了タグは明示的に閉じる必要がある
- コンポーネントは、単一のトップレベル要素しか返せない  

関数コンポーネントと組み合わせると関数ベースでコンポーネントを定義可能
```jsx
const ComponentName = () => {
  return (
    <div>
      <h1>Hello, World!</h1>
    </div>
  );
};
```
- React.Fragmentや<>は、複数の要素を一つにまとめる機能をしますが、実際のHTMLには何も出力されません。
  - 複数の要素を一つの親要素で包む必要があるとき、不要なHTMLタグを追加したくない場合です。
  - <React.Fragment>の短縮形である<>
```jsx
<React.Fragment>
  <ChildComponent1 />
  <ChildComponent2 />
</React.Fragment>

<>
  <ChildComponent1 />
  <ChildComponent2 />
</>
```
## JXSのコメント
- JSXを{/* */}で囲むと、その部分はコメントになる
- 正しくコメントにできている場合は、囲んだ部分が灰色になる
## imgタグの注意点
- imgタグは、HTMLでは、```<img src='画像のURL'>```のように閉じタグが必要ありませんでした。
一方、JSXでは閉じタグが必要になります。```<img src='画像のURL' />```のように、タグの終わりにスラッシュ「/」を記述します。
## JSXとクラス名
- JSXにクラス名をつける場合、HTMLと書き方が異なる
- クラス名は、「className='クラス名'」とします。
- CSSの指定方法は変わりません。
```js
<タグ className='クラス名'></タグ>
```
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
# イベント
- 「何かが起きたときに、処理を実行するように指定」する
- アロー関数を使って、タグ内に「イベント名={() => { 処理 }}」
  - アロー関数はJavaScriptなので、{}で囲む
## onClickイベント
- 「クリックされた時に処理を実行する」
- イベント名にonClickを指定
```js
<button onClick={() => {処理}}>ボタン表示</button>
```
# フック関数
Reactのフック関数は、関数コンポーネントで状態やライフサイクルの機能を使うための仕組みです。これにより、よりシンプルで再利用可能なコードを書くことができます。フック関数は通常、useで始まる名前で定義され、Reactの組み込み関数として提供されています。
- stateは現在の状態を表し、setStateは状態を更新するための関数です。initialStateは初期値
```jsx
import { useState } from 'react';

const [state, setState] = useState(initialState);
```
フック関数は、Reactの関数コンポーネントで状態やライフサイクル機能を使うための特別な関数です。フックを使うことで、クラスコンポーネントを使わずにシンプルで再利用可能なコードが書けます。状態を持つコンポーネントを簡単に作成できるため、開発が効率的になる
- useStateは状態管理
- useEffect: コンポーネントのライフサイクルに応じて副作用（データ取得やDOM操作など）を管理します。
- useContext: コンテキストAPIを使って、コンポーネント間でデータを共有します。
- useReducer: 複雑な状態管理を行うために、Reduxのようなリデューサーを使います。
- useRef: DOM要素や値を保持するための参照を作成します。
# state
- Step1：stateの定義をしてstateを利用できるようにする
  - constructorの中で、オブジェクトとして定義する
  - ここで定義したオブジェクトがstateの初期値となる
  - その他の部分の、「constructor(props)」や「super(props);」といった処理はいつも同じ記述をするため、定型文
- Step2：stateを表示
  - this.stateはオブジェクトなので、this.state.プロパティ名とすることで、指定したstateのプロパティ名に対応する値を取得可能
- Step3：stateの変更
  - this.setState({プロパティ名: 変更する値})とすることで、指定されたプロパティに対応するstateの値が変更されます。その結果、「this.state.name」で表示できる値も変更されます。
  - 今回はボタンがクリックされた時に、名前の表示を変えるために、右の図のようにsetStateをonClick内で行う
  - Reactでは、下図のように「stateの値に直接代入することで値を変更してはいけない」という決まりがある
    - 値を変更したい場合は、setStateを使用
```js
import React from 'react';

class App extends React.Component {
  // Step1：定型文
  constructor(props) {
    super(props);
    // Step1：stateを定義
    this.state = {name:"ねこ"}
    
  }

  render() {
    return (
    	<div>
        // Step2：stateを表示
    	  <h1>こんにちは、{this.state.name}さん！</h1>
        {/* Step3：onClickの処理に、stateを変更する処理 */}
        <button onClick={() => {this.setState({name:"ねこ"})}}>ねこ</button>
        <button onClick={() => {this.setState({name:"人間"})}}>人間</button>
      </div>
    );
  }
}

export default App;
```
状態管理
- ユーザーの入力やアプリケーションの動作に応じて表示を変えるために重要
- useStateを使ってcountという状態を管理しています。ボタンをクリックするたびにsetCountが呼ばれ、countが1ずつ増加します
```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>現在のカウント: {count}</p>
      <button onClick={() => setCount(count + 1)}>カウントアップ</button>
    </div>
  );
}
```
## 三項演算子
- if...elseの省略版のようなもの
- 条件に当てはまるかどうかを判定して、条件式が真（true）の時はコロンの前の値 、偽（false）の時はコロンの後の値を返す
```JavaScript
条件 ? 真の場合の値 : 偽の場合の値
```
```JavaScript
let age = 10;

// IF文
if (age >= 20) {
  console.log('私は20歳以上です');
} else {
  console.log('私は20歳未満です');
}
// 三項演算子
console.log(age >= 20 ? '私は20歳以上です' : '私は20歳未満です');
```
私は20歳未満です

## stateのメソッド化
- メソッドの作成
  - メソッドはイベント内で呼び出すことも可能
  - onClick={() => {this.メソッド名()}}とすることで、クリックされたときに、App.js内の指定したメソッドを実行することができる

【App.js】
```js
import React from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {name:"ねこ"}
    
  }

  // handleClickメソッドを定義
  handleClick(name){
    this.setState({name: name});
  }

  render() {
    return (
    	<div>
    	  <h1>こんにちは、{this.state.name}さん！</h1>
        {/* onClickイベント内の処理を、handleClickメソッドを呼び出す処理に変更：変更前this.setState({name:"ねこ"}) */}
        <button onClick={() => {this.handleClick("ねこ")}}>ねこ</button>
        <button onClick={() => {this.handleClick("人間")}}>人間</button>
      </div>
    );
  }
}

export default App;
```
# コンポーネント
- コンポーネント:小さな部品(HTML・CSS・JavaScript一纏め)を階層構造で組み立てる
- 一度作れば何度でも呼び出すことが可能
- コンポーネント1つに付き1ファイルにする
- インポートとエクスポート必須
- コンポーネントとファイル名を揃えるのが基本
- まず、Reactをインポートします。そして、React.Componentを継承するLanguageクラスを作成します。このクラスがコンポーネントとなる
  - 作成したクラスの中で、renderメソッドを定義し、return内にJSXを記述する。

【個別コンポーネント.jsx】
```jsx
import React from 'react';

class Language extends React.Component{
  render(){
    return(
      <div className='language-item'>
        <div className='language-name'>HTML & CSS</div>
        <img className='language-image' src='画像URL' />
      </div>
      )
  }
}
```
【個別コンポーネント.jsx】
- functionは関数を定義するためのキーワード
- 関数コンポーネントの名前は大文字で始めるのが一般的
- 利用したい箇所で関数コンポーネント<ComponentName />と記述することで関数コンポーネントを利用する
- 同じデザインのボタンを何度も使いたいときに、関数コンポーネントを使ってボタンを一つの部品として作る
```jsx
function ButtonComponent() {
  return (
    <button>Click me!</button>
  );
}

function App() {
  return (
    <div>
      <ButtonComponent />
    </div>
  );
}
```
アロー関数による記法
- アロー関数を使って function の表記を省略
```jsx
const MyComponent = () => {
  return (
    <div>
      <h1>Hello, World!</h1>
    </div>
  );
}

function App() {
  return (
    <div>
      <MyComponent />
    </div>
  );
}
```
## コンポーネントの表示
- 1:App.js内でLanguageコンポーネントを呼び出すには、作成したコンポーネントをコンポーネントファイル内でexportする必要がある
- 2:App.jsで、コンポーネントをインポート
- 3:App.jsで、JSX内に「<コンポーネント名 />」と書く
# 変えたい部分の表示を変更：props
- 動的情報
- App.jsから、各言語の名前と画像のデータを個別コンポーネントに渡すことによって、言語ごとに表示を変えることができます。App.jsから渡すこのデータをprops（プロップス）という
- propsは、「props名=値」という形で、コンポーネントを呼び出す箇所で渡す

【App.js】
```js
  render() {
    return (
    	<div>
        <button
          name="ねこ"
        />
      </div>
    );
  }
}
```
- 渡されたpropsは、this.propsで取得可能
- this.propsは{ props名: 値}というオブジェクトになる
  - 「this.props.props名」とすることでpropsの値を取得可能

【個別コンポーネント.js】
```js
import React from 'react';

class Language extends React.Component{
  render(){
    return(
      <div className='language-item'>
        <div className='language-name'>{this.props.name}</div>
        <img className='language-image' src={this.props.image} />
      </div>
      )
  }
}
```
## 繰り返しコンポーネントを利用：.map
- JSXをmapを用いて効率的に表示している例
- mapメソッドで配列fruitListの各要素に対して順に処理を行い、各要素を<p>タグで囲んで表示しています。mapメソッドの戻り値はJSXなので、引数であるfruitItemは中括弧{}で囲むことに注意

```js
let 新しい配列 = array.map((element, index, array) => {
  // 処理
  return element;
});
```
- element: 現在処理中の要素
- index: 現在処理中の要素のインデックス（省略可能）
- array: 元の配列（省略可能）

【App.js】
```js
const =[マップで使用したい配列定義]
（中略）
    return (
      <div>
        <h1>言語一覧</h1>
        <div className='language'>
          {languageList.map((languageItem) => {
            return (
              <Language
                name = {languageItem.name}
                image = {languageItem.image}
              />
            )
          })}
          
        </div>
      </div>
    );
  }
}
```
### forEachメソッドとの違い
mapメソッドは、forEachメソッドと混同されやすいです。
forEachメソッドは各要素に処理を実行するだけであるのに対して、 mapメソッドは新しい配列を返します。
新しい配列を必要としない場合や値を返す必要がない場合は、forEachメソッドを使用しましょう。



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



