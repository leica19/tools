# tools
thanks god. it's Friday.

## searchOnGoogleRoughly.py

引数に指定した検索語をGoogleで調べ、上位5位(デフォルト値)までをそれぞれ別タブで表示する。
検索語は"かつ"に対応

### 使い方

$ python searchOnGoogle.py {検索語} {タブ数}

※タブ数を指定しない場合は、5がデフォルトとなります。

### 例：江坂で美味しいラーメンを調べたい場合

$ python searchOnGoogle.py 江坂+美味しい+ラーメン 3

上位3つまでの検索結果がそれぞれ別タブで開く。

## getPicturesOnGoogle.py

カレントディレクトリにGoogle画像検索の結果をダウンロードする。

### 使い方

$ python getPicturesOnGoogle.py {検索語} {ダウンロード先dir(path)}

※ダウンロード先dirを指定しない場合は検索語がディレクトリ名となります。

### 例:カレントディレクトリに松本人志というディレクトリをつくり、そこに松本人志という検索語でGoogle画像検索した結果をダウンロードする。

$ python getPicturesOnGoogle.py 松本人志

### 例：沖縄かつラーメンで画像検索し、その画像をラーメンという名前のディレクトリに格納する場合

$ python getPicturesOnGoogle.py 沖縄+ラーメン ラーメン
