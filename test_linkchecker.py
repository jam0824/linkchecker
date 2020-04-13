import unittest
import classlinkchecker

class Test_LinkChecker(unittest.TestCase):
    def test_get_page_source_ページ存在時の確認(self):
        page_info = classlinkchecker.LinkChecker().get_page_info('http://testerchan.hatenadiary.com/')
        self.assertEqual(
            True, 
            "ソフトウェアテストの用語、やり方などを4コマ漫画でわかりやすく説明する（予定の）ブログです。脱線も多いです。" in page_info.text
        )

    def test_get_list_url_URLがとってこれた時の確認(self):
        lc = classlinkchecker.LinkChecker()
        page_info = lc.get_page_info('http://testerchan.hatenadiary.com/')
        list_url = lc.get_list_url(page_info.url, page_info.text)
        #print(list_url)
        self.assertIn('https://manga.line.me/indies/product/detail?id=2358',list_url)

    def test_check_url_status(self):
        lc = classlinkchecker.LinkChecker()
        page_info = lc.get_page_info('https://www.testerchan.work/')
        list_url = lc.get_list_url(page_info.url, page_info.text)
        list_error = lc.check_url_status(list_url)
        self.assertEqual(3, len(list_error))
        self.assertEqual('https://www.amazon.co.jp/gp/product/B07CJTF8FP/ref=series_rw_dp_sw', list_error[0]['url'])

if __name__ == '__main__':
    unittest.main()