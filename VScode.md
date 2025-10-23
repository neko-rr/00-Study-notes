# 仮想環境作成
```Python
python -m venv .venv  # Windowsの場合
```

# 必要なものをインポートまとめ
```Python
pip freeze > requirements.txt
```
```Python
pip install dash pandas
```
```Python
import dash
import pandas as pd

print(dash.__version__)
print(pd.__version__)
```
## pipファイル、不審なファイル扱いエラー
- 管理者権限で PowerShell / VS Code を開く
- VS Code を右クリック → 「管理者として実行」
- その状態で再度コマンドを実行

# Ruff
## [https://qiita.com/nuco_nn/items/fe06c815bb776737e94a](https://qiita.com/nuco_nn/items/fe06c815bb776737e94a)
PythonのLinterとしてはFlake8、コード整形ツールとしてはBlack、importのsortingはisortが主流ではありますが、これら全てを兼ね備えているのがRuffです。
Rustで開発されているRuffは上記既存のツールよりも動作が数十倍早いとされており、設定も一括で行えるため現在はこちらの導入を進めているケースも多いのではないでしょうか。

導入にあたって、VSCodeのsettings.jsonへは以下の項目を追加します。
前半はVSCodeの挙動や設定について、後半はRuff自体の挙動についての設定になります。
Ruff自体の挙動についてはさらに、ここで指定したruff.tomlを同じ階層に作成して設定します。
デフォルトではこちらの設定通りになっていますので、無視させたいディレクトリ名などお好みで設定しましょう。
```Python
{
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true
    },
    "ruff.lint.args": [
        "--config=ruff.toml"
    ],
    "ruff.format.args": [
        "--config=ruff.toml"
    ]
}

```

# VScodeの設定 settings.jsonを編集して開発環境を最適化
Windowsでの表示
Ctrl + P でコマンドパレットを開き、以下のパスを入力すると、settings.jsonを開けます。
```
C:\Users\ユーザー名\AppData\Roaming\Code\User\settings.json
```
## [https://envader.plus/article/526](https://envader.plus/article/526)
## ファイルを自動保存する設定
ファイルを自動保存する設定です。以下の例はファイルの変更から1秒後に自動保存します。
```
{
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
}
```
## お好みのテーマやフォントサイズの設定
VSCodeのテーマやフォントサイズをカスタマイズする設定です。フォントサイズや行の高さなど、見た目のカスタマイズも可能です。
```
{
    "workbench.colorTheme": "テーマ名",
    "editor.fontFamily": "フォント名",
    "editor.fontSize": 文字のサイズ,
    "editor.lineHeight": 行のアキ幅,
}
```
## エディタの表示設定
エディタの使い勝手を向上させるための設定です。以下のような設定ができ、エディタを自分好みにカスタマイズできます。
```
{
    "editor.minimap.enabled": false,
    "editor.renderWhitespace": "boundary",
    "editor.guides.bracketPairs": true,
}
```

