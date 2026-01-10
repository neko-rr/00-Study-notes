# 環境変数エラー確認
ターミナルで実行
```
python -c "from dotenv import load_dotenv; import os; load_dotenv('.env', override=False); print('APP_BASE_URL=', os.getenv('APP_BASE_URL')); print('SUPABASE_URL_set=', bool(os.getenv('SUPABASE_URL'))); print('SUPABASE_ANON_KEY_set=', bool(os.getenv('SUPABASE_ANON_KEY') or os.getenv('SUPABASE_KEY')))"
```
# エラー理由
- ファイル名が .env ではなく .env.txt になっている（Windowsあるある）
- 実行しているカレントディレクトリが異なる
- .env の保存が反映されていない（保存漏れ）

