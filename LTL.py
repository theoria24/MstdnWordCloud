#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mastodon import Mastodon
import configparser
import re
import time
import MeCab
from tqdm import tqdm
from wordcloud import WordCloud
from datetime import datetime

def login():
    # config.sample.iniを元にconfig.iniを作成してください
    config = configparser.ConfigParser()
    config.read('config.ini')
    mstdn = Mastodon(
        client_id = config['client']['id'],
        client_secret = config['client']['secret'],
        api_base_url = config['mastodon']['server'])
    return(mstdn)

def format(text):
    # HTMLタグとURLの削除
    text = re.sub("</?p>", "", text)
    text = re.sub("<a href=\"(.*?)\".*?>(.*?)</a>", "", text)
    text = re.sub("<span class=\"(.*?)\".*?>(.*?)</span>", "", text)
    text = re.sub("<br />", '\n', text)
    return(text)

def getLTL(lim,max):
    text = ""
    mstdn = login()
    ltl = mstdn.timeline_local(limit=lim,max_id=max)
    for row in ltl:
        if row["account"]["username"] not in []: #除外するアカウントを配列で指定
            text += format(row["content"]) + "\n"
        toot_id = row["id"]
    return(text,toot_id)

def wakati(text):
    kekka = ""
    m = MeCab.Tagger()
    node = m.parseToNode(text)
    # 拾う品詞を指定 「する」「ある」などが大きくなりすぎるので動詞を削った。名詞だけでいいかも？
    target_hinshi = ['名詞', '形容詞', '形容動詞']
    exclude = ['非自立', '接尾'] # 除外する品詞細分類1パラメーター
    exclude_word = ['ない'] # 除外する単語（終止形で指定）。「ない」があまりにも大きいので。
    while node:
        if node.feature.split(',')[0] in target_hinshi:
            if node.feature.split(',')[1] not in exclude:
                if node.feature.split(',')[6] not in exclude_word:
                    kekka += node.feature.split(',')[6] + "\n" # 活用のあるものに対して終止形のものを選ぶ
        node = node.next
    return(kekka)

def wordcloud(text):
    filename = datetime.now().strftime("%Y%m%d-%H%M%S")
    # 背景色や画像の大きさ、出力場所の指定
    wordcloud = WordCloud(background_color="white", font_path="./Kazesawa-Regular.ttf",width=1024,height=768).generate(text)
    wordcloud.to_file("./out/LTL-"+filename+".png")
    print("Saved as out/LTL-"+filename+".png")

def main():
    t = 0
    rep = 25 # この数字*40 のトゥートを取得しようとする
    toots = ""
    max = None
    print("Getting Toots...")
    pbar = tqdm(total=(rep*40))
    while t < rep:
        data = getLTL(40,max)
        toots += data[0]
        max = data[1]
        t += 1
        pbar.update(40)
        if t < rep - 1:
            time.sleep(3) #サーバー負荷にちょっと配慮
    pbar.close()
    print("Generating Image...")
    wordcloud(wakati(toots))

if __name__ == '__main__':
    main()
