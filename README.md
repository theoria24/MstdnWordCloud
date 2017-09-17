# MstdnWordCloud

Mastodonからトゥートを取得してワードクラウドを作成します。

## 必要そうなもの
たぶんこのあたりが入っていれば動きます。
#### [Python3](https://www.python.org/)
#### [Mastodon.py](https://github.com/halcy/Mastodon.py)
MastodonのAPIを叩くやつ  
`pip3 install Mastodon.py`

#### [MeCab](http://taku910.github.io/mecab/)
日本語をいい感じに分ける

#### mecab-python3
MeCabをPythonで扱うのに便利  
`pip3 install mecab-python3`

#### [word_cloud](https://github.com/amueller/word_cloud)
ワードクラウドを作成  
`pip3 install wordcloud`
#### [tqdm](https://github.com/tqdm/tqdm)
進捗バーを表示するのに必要  
`pip3 install tqdm`

## あると便利なもの
#### [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd)
固有名詞がいっぱい入っているので便利

## 含まれているもの
#### [Kazesawaフォント](https://kazesawa.github.io/)
[SIL Open Font License](http://scripts.sil.org/OFL)で提供されるフォント。きれい。

## 使い方
### 設定
1. このRepositoryをクローンするなりZipでダウンロードするなりする。
1. なんとかして目的のMastodonの`client_id`、`client_secret`、`access_token`を入手する。
1. `config.sample.ini`をコピーするなりして`config.ini`を作成。
1. 必要に応じて取得するトゥートの数を変更したり、除外するアカウントを指定したり画像サイズを設定したりする（コメントを見れば分かるはず…）。

### 実行
* ローカルタイムラインから作成  
`python3 LTL.py`
* 自分のトゥートから作成  
`python3 MyToots.py`

## 参考
以下の画像は2017/09/17 5:00頃に[wug.fun](https://wug.fun)のLTLを120件取得して作成したものです。

![Sample](https://user-images.githubusercontent.com/17396689/30515624-c7719226-9b66-11e7-89d7-6dd52deaa8bd.png)

## TODO
* 例外の処理とか

## 何かあったら
issueとか[Twitter](https://twitter.com/_theoria)とかMastodon（[@theoria@wug.fun](https://wug.fun/@theoria)、[@theoria@mstdn.jp](https://mstdn.jp/@theoria)）とかにどうぞ


## ライセンス
MIT License
