# ハッカソン対策用
[Prompt Engineering with Llama 2 & 3]
(https://www.deeplearning.ai/short-courses/prompt-engineering-with-llama-2/)  
[Introducing Multimodal Llama 3.2]
(https://www.deeplearning.ai/short-courses/introducing-multimodal-llama-3-2/)  
[Building with Llama 4]
(https://www.deeplearning.ai/short-courses/building-with-llama-4/)

```Python
# import llama helper function
from utils import llama
```
```Python
# define the prompt
prompt = "Help me write a birthday card for my dear friend Andrew."
```
```Python
# pass prompt to the llama function, store output as 'response' then print
response = llama(prompt)
print(response)
```
# メモ
## 最大トークン>入力トークン+出力トークン
- 入出力のどちらかが長い場合は、もう一方の量が減るので、注意
- max_tokens=で制限すると安全
```Python
# set max_tokens to stay within limit on input + output tokens
prompt = f"""
Give me a summary of the following text in 50 words:\n\n
{text}
"""
response = llama(prompt,
                max_tokens=123)
```

## マルチターン
- 応答の記憶を残して、次の会話に繋げる
- 次の会話の際に、「前回のプロンプト+前回の回答+今回の質問」を合わせて依頼する
```Python
prompt_1 = """
    What are fun activities I can do this weekend?
"""
response_1 = llama(prompt_1)
```
```Python
prompt_2 = """
Which of these would be good for my health?
"""
```
```Python
chat_prompt = f"""
<s>[INST] {prompt_1} [/INST]
{response_1}
</s>
<s>[INST] {prompt_2} [/INST]
"""
print(chat_prompt)
```
```Python
response_2 = llama(chat_prompt,
                 add_inst=False,
                 verbose=True)
```
```Python
print(response_2)
```
```Python
