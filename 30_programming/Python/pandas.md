# 公式[https://pandas.pydata.org/](https://pandas.pydata.org/)
# 参考URL
- [pandasで行数、列数、全要素数（サイズ）を取得](https://note.nkmk.me/python-pandas-len-shape-size/)
- [Pandas DataFrameで条件に基づく行と列の選択方法](https://qiita.com/zum-m/items/35e39696382545d05c68)
- 重複は、ここより、これを見る
  - [pandas.DataFrame, Seriesの重複した行を抽出・削除](https://note.nkmk.me/python-pandas-duplicated-drop-duplicates/)
- [pandasのデータ型dtype一覧とastypeによる変換（キャスト）](https://note.nkmk.me/python-pandas-dtype-astype/#pandasdataframedtype_1)
- [pandas.DataFrameを結合するmerge, join（列・インデックス基準）](https://note.nkmk.me/python-pandas-merge-join/)
- データ連結
  - [Pythonデータ分析 | pandasテーブル結合メソッド早見表](https://qiita.com/kakiuchis/items/9624437fc57aff149774)
  - [pandas.DataFrameを結合するmerge, join（列・インデックス基準）](https://note.nkmk.me/python-pandas-merge-join/)
- [【pandas】melt, pivot：縦横変換【データフレーム処理】](https://datasciencemore.com/python-pandas-melt-pivot/)
- [pandas.DataFrame, Seriesをソートするsort_values, sort_index](https://note.nkmk.me/python-pandas-sort-values-sort-index/)
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
# 列の型変更
```Python
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({'grade': 'int64', 'average': 'float64'})
    return students
```
```Python
データ型dtype	型コード	説明
int8	i1	符号あり8ビット整数型
int16	i2	符号あり16ビット整数型
int32	i4	符号あり32ビット整数型
int64	i8	符号あり64ビット整数型
uint8	u1	符号なし8ビット整数型
uint16	u2	符号なし16ビット整数型
uint32	u4	符号なし32ビット整数型
uint64	u8	符号なし64ビット整数型
float16	f2	半精度浮動小数点型（符号部1ビット、指数部5ビット、仮数部10ビット）
float32	f4	単精度浮動小数点型（符号部1ビット、指数部8ビット、仮数部23ビット）
float64	f8	倍精度浮動小数点型（符号部1ビット、指数部11ビット、仮数部52ビット）
float128	f16	四倍精度浮動小数点型（符号部1ビット、指数部15ビット、仮数部112ビット）
complex64	c8	複素数（実部・虚部がそれぞれfloat32）
complex128	c16	複素数（実部・虚部がそれぞれfloat64）
complex256	c32	複素数（実部・虚部がそれぞれfloat128）
bool	?	ブール型（True or False）
object	O	Pythonオブジェクト型
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
# 欠損値の補完例
列指定の欠損値を「０」にする
```Python
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.fillna({'quantity': 0 }, inplace=True)
    return products
```
速度が速いのは、これ
```Python
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    return products
```
# 表を縦に連結
```Python
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], ignore_index=True)
```
# ピポット
```Python
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    ans = weather.pivot(index='month', columns='city', values='temperature')
    month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    ans = ans.reindex(month_order)
    return ans
```
# .melt（縦変換・ピポットの反対）
```Python
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    ans = report.melt(
        id_vars="product", 
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
        var_name="quarter",
        value_name="sales" 
    )
    return ans
```
# 並び替えして列降順の別列のみ表示
```Python
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]
```

#
```Python

```
