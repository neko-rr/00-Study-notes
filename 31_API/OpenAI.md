# OpenAIのPythonライブラリインストール
```ph
pip install openai
```
# インストール成功確認
```Python
import openai
print(openai.__version__)
```
バージョン番号が表示されれば、インストールは成功
# 使用例
```Python
import os
import openai

# 環境変数からAPIキーを取得
api_key = os.getenv('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("APIキーが設定されていません。環境変数 'OPENAI_API_KEY' を設定してください。")

openai.api_key = api_key

try:
    # APIリクエストの実行
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Tell me a joke."}],
        max_tokens=50,
        temperature=0.5
    )
    # レスポンスの表示
    print(response['choices'][0]['message']['content'].strip())
except openai.error.AuthenticationError:
    print("認証エラー: APIキーを確認してください。")
except openai.error.RateLimitError:
    print("レート制限エラー: リクエストが多すぎます。しばらくしてから再試行してください。")
except Exception as e:
    print(f"予期しないエラーが発生しました: {e}")
```
```Python
import openai
import requests

# APIエンドポイント
url = "https://api.openai.com/v1/chat/completions"

# ヘッダー
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}

# リクエストボディ
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Translate the following English text to French: 'Hello, how are you?'"}
    ],
    "max_tokens": 60
}

# リクエストの送信（json=を使うと簡単）
response = requests.post(url, headers=headers, json=data)

# レスポンスの表示
if response.status_code == 200:
    print(response.json())
else:
    print(f"エラー: {response.status_code}")
    print(response.text)
```
# パラメータ
## temperature
生成されるテキストのランダム性を制御するパラメータです。値の範囲は0から1まで
- 0：最も可能性の高い単語を選びます。結果として、出力は一貫性が高く、予測可能なものになる
- 1：よりランダムになり、異なる単語を選ぶ可能性が高くなります。これにより、創造的で多様な出力が得られますが、一貫性が低くなることがある
## max_tokens
生成されるテキストの最大トークン数を指定する
# レスポンスの解析例
```Python
import os
import openai

# 環境変数からAPIキーを取得
api_key = os.getenv('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("APIキーが設定されていません。環境変数 'OPENAI_API_KEY' を設定してください。")

openai.api_key = api_key

try:
    # APIリクエストの実行
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "What is the capital of France?"}],
        max_tokens=10,
        temperature=0.5
    )
    # レスポンスの解析
    text = response['choices'][0]['message']['content'].strip()
    tokens_used = response['usage']['total_tokens']
    print(f"生成されたテキスト: {text}")
    print(f"使用されたトークン数: {tokens_used}")
except Exception as e:
    print(f"エラーが発生しました: {e}")
```
