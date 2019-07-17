# atcoder-tools

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

## src

srcはこのリポジトリでは管理しないで別のリポジトリとして管理.

# atcoder-tools (English)

## set up 

Create `config.py` as the following.

Fill in AtCoder credentials at config.py.

```python:config.py
USERNAME = "*********"
PASSWORD = "*********"
```
`config.py` is included in `.gitignore` so as not to track credentials.

## code generation

i.e.) How to create template directories/files for ABC063. (Language: python)

```
python main.py --mkdir --level abc --rnd 63 --lang python
```
python template files will be created for each problem.
src directory will be created as necessary.

## test

i.e.) How to code test ABC063 problem A in python.

```
python main.py  --level abc --rnd 63 --prob a --lang python
```

## submit

Test for all samples and submit if all pass.

```
python main.py --submit  --level abc --rnd 63 --prob a --lang python
```
## parameters

* -v,--verbose (verbose mode)
* --lang (python(default), cpp)
* --level (abc(default), arc, agc) 
* --rnd (rounds i.e.: ABC063 -> 63) 
* --prob (problem A would be denoted as a. In lower case)
* --src-dir (Directory for submission. default: src)
* --submit (flag for submission after passing all test cases)
* --mkdir (flag for creating template)

## caution
Sponsored contests are not implemented.

## src
src directory will be managed in another repo.
