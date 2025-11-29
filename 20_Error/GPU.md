# GPUに全ての重みが無い
## 【エラー箇所確認】
- 全サブモジュールのデバイスを確認する 下記のようなコードで、たとえば model.patch_embed.proj.weight.device など、各主要サブモジュールのパラメータのデバイスがGPU（cuda:0）になっているか確認してください
```Python
for name, param in wrapped_embedding_model.named_parameters():
    print(f"{name} is on {param.device}")
```
## 【修正コード】
- 再帰的にすべてのモジュールを GPU に移す： たとえば、以下のような関数を用いて、すべてのサブモジュール、バッファ、パラメータを再帰的に GPU に移す方法があります。
```Python
def move_model_to_device(model, device):
    model.to(device)
    for param in model.parameters():
        param.data = param.data.to(device)
    for buf in model.buffers():
        buf.data = buf.data.to(device)
    return model

wrapped_embedding_model = move_model_to_device(wrapped_embedding_model, device)
```
