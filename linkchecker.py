import classlinkchecker
import sys

args = sys.argv

if len(args) < 2:
    print("調査対象urlが入力されていません")
    sys.exit()
if "http" not in args[1]:
    print("有効なurlではありません")
    sys.exit()

lc = classlinkchecker.LinkChecker()
page_info = lc.get_page_info(args[1])
list_url = lc.get_list_url(page_info.url, page_info.text)
list_error_url = lc.check_url_status(list_url)
print('//////////////////////////////')
print('Error URL List:')
for url in list_error_url:
    print(str(url['status']) + ' : ' + url['url'])


