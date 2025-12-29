# ripgrep のインストール方法（Windows）
検索早い
# ripgrepで固定色検索
## 最強：全検索
```bash
rg -n "(#[0-9a-fA-F]{3,8}|rgba?\(|style=\{[^}]*\(color|background|border\))"
```
## 個別指定検索
1. hexカラー（3〜8桁）
```bash
rg -n "#[0-9a-fA-F]{3,8}"
```
2. rgb / rgba
```bash
rg -n "rgba?\("
```
3. JSX の style={} 内の color/background/border
```bash
rg -n "style=\{[^}]*\(color|background|border\)"
```
4. CSS の color/background/border に直書き
```bash
rg -n "(color|background|border)[^;]*#"
```
## 検索後
よくある固定色の例（grep対象）
種類	例
hex	#fff, #000000, #12abcf, #12345678
rgb	rgb(255, 0, 0)
rgba	rgba(255, 0, 0, 0.5)
JSX style	style={{ color: "#fff" }}
CSS	background: #f00;
💡 プロの現場でよくやる流れ
ripgrep で全固定色を抽出

一覧を Notion / GitHub Issue に貼る

Tailwind / CSS変数に置き換える計画を立てる

PR で段階的にリファクタリング
