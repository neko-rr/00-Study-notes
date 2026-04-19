# 公式[https://pandas.pydata.org/](https://pandas.pydata.org/)
# 参考URL
- [pandasで行数、列数、全要素数（サイズ）を取得](https://note.nkmk.me/python-pandas-len-shape-size/)
- [Pandas DataFrameで条件に基づく行と列の選択方法](https://qiita.com/zum-m/items/35e39696382545d05c68)
- 重複は、ここより、これを見る
  - [pandas.DataFrame, Seriesの重複した行を抽出・削除](https://note.nkmk.me/python-pandas-duplicated-drop-duplicates/)
# 列名
パラメータを使用して、カスタム列名を設定できますcolumns。まず、データフレームに表示される順序で列名のリストを作成します。
```Python
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column_names = ["student_id", "age"]
    result_dataframe = pd.DataFrame(student_data, columns=column_names)
    return result_dataframe
```
```Python
# リストを使ってデータフレームを作成
data = [[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 35]]
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])

print("データフレーム:")
print(df)
```
```Python
データフレーム:
   ID     Name  Age
0   1    Alice   25
1   2      Bob   30
2   3  Charlie   35

```
# 行数列数
```Python
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0],players.shape[1]]
```
# 行列選択
```Python
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name','age']]
```
# 新規列追加
給料*2のボーナス列追加
```Python
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees
```
# 重複列削除例
```Python
df.drop_duplicates(subset='state', keep='last', inplace=True)
print(df)
```
# 欠損値の処理
```Python
import numpy as np
import pandas as pd
df = pd.DataFrame({"int": [1, np.nan, np.nan, 32],
                   "str": ["python", "ai", np.nan, np.nan],
                   "flt": [5.5, 4.2, -1.2, np.nan]})
print(df)
# df成分に対してNaNの地位をTrueとしたブールの値のデータフレームを返す
print(df.isnull()) # notnull()を使うと、TrueとFalseが逆の処理になる。
# "int"列にNaNがある行の削除
print(df.dropna(subset=["int"]))
# NaNがある行を全て削除する
print(df.dropna())
# NaNを全て0に置換する
print(df.fillna(0)) # 第一引数にmethod="ffill" 第二引数にlimtit=数字 とすることで指定した数字までは前のデータを使ってNaNを埋めることができます
df2 = pd.DataFrame({"int": [1, np.nan, np.nan, 32],
                   "str": ["python", "ai", np.nan, np.nan],
                   "flt": [5.5, 4.2, -1.2, np.nan]})
# int列だけ0で補完
df2.fillna({"int": 0}) # 特定の列に対しては辞書型を用いる
# 列ごとに異なる値を使いたい時は複数のキーを渡す。
df2.fillna({"int": 0, "str": "ai"}) 
# 特定の列(例えばflt)を削除
df2.drop(labels="flt",axis=1)
"""
  int str
0 1.0 python
1 NaN ai
2 NaN NaN
3 32.0  NaN
"""
# 複数の列を削除
df2.drop(labels=["flt", "str"],axis=1)
"""
  int
0 1.0
1 NaN
2 NaN
3 32.0
"""
# indexを指定すると行を消すこともできます
df2.drop(index=1, axis=0)
"""
int str flt
0 1.0 python  5.5
2 NaN NaN -1.2
3 32.0  NaN NaN
"""
# 元のデータに反映して削除するにはinplaceオプションにTrueを渡します
df2.drop(labels="flt", axis=1, inplace=True)
print(df2)
"""
int str
0 1.0 python
1 NaN ai
2 NaN NaN
3 32.0  NaN
"""
```
# 列の値変更
```Python
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees
```
# 列名行名変更
```Python
df_copy.rename(columns={'A': 'Col_1'}, index={'ONE': 'Row_1'}, inplace=True)
```
## 複数列名変更 
```Python
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
    return students
```





# 
```Python

```
