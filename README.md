# AtCoder

## set up

`config.py`を直下に作成.

使用したいAtCoderアカウントの情報を記載.

```python:config.py
USERNAME = "*********"
PASSWORD = "*********"
```
デフォルトで`config.py`は`.gitignore`に含まれており、git管理から外れている.


## code generation

ABC063のファイル、ディレクトリを作る場合(言語はpythonを使用)

```
python main.py --mkdir --level abc --rnd 63 --lang python
```

pythonファイルの雛形が各問題ごとに作られる.
srcディレクトリがない場合はまとめて作られる.

## test

ABC063のA問題のコードをテストしたい場合(python)


```
python main.py  --level abc --rnd 63 --prob a --lang python
```

## submit

全てのサンプルをテストし、全て通った場合は提出する場合(python)

```
python main.py --submit  --level abc --rnd 63 --prob a --lang python
```


## parameters

* -v,--verbose (verbose mode)
* --lang (python(default), cpp)
* --level (abc(default), arc, agc) 
* --rnd (コンテストの回数) 
* --prob (A問題とか.小文字で指定)
* --src-dir (提出コードのディレクトリ. default: src)
* --submit (つけるとテストしたあと全部パスしてたら提出する.)
* --mkdir (つけると雛形生成)


## caution
企業コンには未対応.

## branch 

* master : ツールのみが入っている.
* production : 自分の提出コードも含めている.