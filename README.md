# ハーメルン小説更新Gettter

## 開発環境

- Windows10
- Mac
- Python
  - feedparser
  - numpy
  - csv

```sh
python -m venv env 

.\env\Scripts\activate    # Windows
source ./env/bin/activate # Mac 

pip install --upgrade pip
pip install -r requirements.txt
```

## 役割

### InitHameln.py

`Heaven'sMemoPad.csv` に新規小説情報を追加

### CheckHameln.py

`Heaven'sMemoPad.csv` に記述している小説の更新情報を調べ、ダウンロードタスクを `Rasiel.csv` に保存

### GetHameln.py

`Rasiel.csv` に記述している小説をtxt形式でダウンロードする

### main.py

`CheckHameln.py` と `GetHameln.py` の機能をまとめた。このコードを実行するだけで、基本は問題ない。 `Rasiel.csv` を介さないので実行時に余計なファイルが生成されない。

## 今後の課題

- デスクトップアプリ化
