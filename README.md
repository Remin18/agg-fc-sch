# Aggregate FEELCYCLE

フィールサイクルの自動集計プログラム

## Required
* Python 2.7.6

## feel_agg.py
HEADERSのcookieが空になっていますので設定が必要です。<br>
cookieはfeelcycleの予約ページから入手可能です。<br><br>
* Chrome<br>
mypage→右クリック⇒検証*1⇒予約ページ⇒検証のNetwordタブ→<br>
一番上のreserve.phpをクリック⇒Request HeadersのCookieをコピー<br>
*1で検証が開きます。開いたままで予約ページに遷移してください。<br>

コピーしたものをfeel_agg.pyファイルの「Paste here」に設定してください。

## config.txt
* 集計範囲を設定できます。
* tenpo_ids：集計対象店舗ID
* joindate：集計開始日

設定例 1
六本木（RPG）の2019年7月1日～が対象
```
[settings]
tenpo_ids = 10
joindate = 2019/07/01
```

設定例 2
赤坂（AKS）, 六本木（RPG）, 川崎（KWS）の2018年10月22日～が対象
```
[settings]
tenpo_ids = 5,10,13
joindate = 2018/10/22
```

## 店舗ID
2 : 銀座 5th（GNZ 5th）
3 : 池袋（IKB）
4 : 表参道（OMS）
5 : 赤坂（AKS）
6 : 心斎橋（SSB）
7 : 福岡天神（FTJ）
8 : 大宮（OMY）
9 : 東梅田（UMDE）
10 : 六本木（RPG）
11 : 栄（SKE）
12 : 銀座 1st（GNZ 1st）
13 : 川崎（KWS）
15 : 柏（KSW）
16 : 立川（TCK）
17 : 新宿（SJK）
18 : 上野（UEN）
19 : 中目黒（NMG）
20 : 岐阜（GIF）
21 : 町田（MCD）
22 : 横須賀中央（YSC）
23 : 自由が丘（JYO）
24 : 吉祥寺（KCJ）
25 : 三ノ宮（SMY）
26 : 多摩センター（TMC）
27 : 仙台（SND）
28 : 上大岡（KOK）
29 : 名古屋（NGY）
30 : 横浜（YKH）
31 : 銀座（GNZ）
32 : 高松（TKM）
33 : 渋谷（SBY）
34 : 梅田茶屋町（UMDC）
35 : 広島（HSM）
36 : 汐留（SDM）
37 : 西梅田（UMDW）
38 : 越谷（KSG）
39 : 札幌（SPR）
40 : 博多（HKT）
41 : 海浜幕張（KHM）
42 : 京橋（KBS）
43 : 五反田（GTD）
44 : 船橋（FNB）

## Execute
feel_agg.pyとconfig.txtを同じフォルダに配置し、以下のコマンドで実行できます。<br>
'''python ./feel_agg.py'''
