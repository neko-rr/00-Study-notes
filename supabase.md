# 使用方法
パッケージを追加
```
npm install @supabase/ssr
```
APIと接続するため、先にSupabaseプロジェクトを用意します。
Supabaseにログインし、新規プロジェクトを作成する。
プロジェクト名の例：memolite-<yourname>-dev
リージョンは普段利用地域を選択。
データベースのパスワードを設定。
作成完了後、ダッシュボードの「設定」→「API」を開き、次の値を控える。
Project URL（NEXT_PUBLIC_SUPABASE_URLに設定）
anon public key（NEXT_PUBLIC_SUPABASE_ANON_KEYに設定）
service_role key（必要に応じてSUPABASE_SERVICE_ROLE_KEYに設定。サーバー側のみで使用）

.env
NEXT_PUBLIC_BASE_URL=http://localhost:3000
NEXT_PUBLIC_SUPABASE_URL=（SupabaseのProject URL）
NEXT_PUBLIC_SUPABASE_ANON_KEY=（Supabaseのanon public key）
