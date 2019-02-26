"""出力した結果と正解の比較を行う."""
import sys
args = sys.argv

path1 = args[1]
path2 = args[2]

with open(path1) as f:
    str1 = f.read()

with open(path2) as f:
    str2 = f.read()

if str1 == str2:
    print("Passed.")
else:
    print("Failed.")
    print("---Output------")
    print(str1)
    print("---Expected----")
    print(str2)
