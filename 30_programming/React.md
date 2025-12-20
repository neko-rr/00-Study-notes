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
