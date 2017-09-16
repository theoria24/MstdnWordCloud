# MstdnWordCloud

特定のMastodonインスタンスのローカルタイムラインを取得してワードクラウドを作成します。

## 必要そうなもの
たぶんこのあたりが入っていれば動きます。
- [Python3](https://www.python.org/)
- [Mastodon.py](https://github.com/halcy/Mastodon.py)
 - MastodonのAPIを叩くやつ
 - <code>pip3 install Mastodon.py</code>
- [MeCab](http://taku910.github.io/mecab/)
 - 日本語をいい感じに分ける
- mecab-python3
 - MeCabをPythonで扱うのに便利
 - <code>pip3 install mecab-python3</code>
- [word_cloud](https://github.com/amueller/word_cloud)
 - ワードクラウドを作成
 - <code>pip3 install wordcloud</code>
- [tqdm](https://github.com/tqdm/tqdm)
 - 進捗バーを表示するのに必要
 - <code>pip3 install tqdm</code>

## あると便利なもの
- [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd)
 - 固有名詞がいっぱい入っているので便利

## 含まれているもの
- [Kazesawaフォント](https://kazesawa.github.io/)
 - [SIL Open Font License](http://scripts.sil.org/OFL)で提供されるフォント。きれい。

## 使い方
1. このRepositoryをクローンするなりZipでダウンロードするなりする。
1. なんとかして目的のMastodonの<code>client_id</code>、<code>client_secret</code>、<code>access_token</code>を入手する。
1. <code>config.sample.ini</code>をコピーするなりして<code>config.ini</code>を作成。
1. 必要に応じて取得するトゥートの数を変更したり、除外するアカウントを指定したり画像サイズを設定したりする（コメントを見れば分かるはず…）。
1. <code>python3 wordcloud.py</code>

## 何かあったら
issueとか[Twitter](https://twitter.com/_theoria)とかMastodon（[@theoria@wug.fun](https://wug.fun/@theoria)、[@theoria@mstdn.jp](https://mstdn.jp/@theoria)）とかにどうぞ

## ライセンス
MIT License
