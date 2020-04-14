# これは何？
調査対象URLのページ内のaタグに含まれるURLを抽出して、その全てに対してhttpステータスチェックを行います。
  
# 注意！！
ページ内の全URLに短時間でアクセスするため攻撃になります。  
自分の作ったページのチェックや会社でチェックをお願いされた時くらいにだけ使いましょう。  
ご自身の責任で使用してください。  
  
# 使い方
まずはlinkchecker_for_windows.zipまたはlinkchecker_for_mac.zipを解凍してください。  
その後コマンドプロンプトやターミナルなどから、zipを解凍したところまで移動して以下のコマンドを実行します。  

windows  
`./linkchecker.exe 調査したいURL`  
mac  
`./linkchecker 調査したいURL`  
  
# 例
`./linkchecker.exe https://www.testerchan.work/`

# pythonから使う場合
requestsとBeautifulSoup4をインストールする必要があります。 

`pip install requests`  
`pip install beautifulsoup4`  