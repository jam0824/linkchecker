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
        html = '<html><head></head><body>'
        html += '<a href="foo.html"></a>'
        html += '<a href="bar.html"></a>'
        html += '</body></html>'
        list_url = lc.get_list_url('https://testerchan.hatenadiary.com', html)
        #print(list_url)
        self.assertIn('https://testerchan.hatenadiary.com/foo.html',list_url)

    def test_get_list_url_URLでNoneが含まれていないか確認(self):
        lc = classlinkchecker.LinkChecker()
        html = '<html><head></head><body>'
        html += '<a name="test"></a>'
        html += '</body></html>'
        list_url = lc.get_list_url('https://testerchan.hatenadiary.com', html)
        #print(list_url)
        expected = []
        self.assertEqual(expected,list_url)

    def test_get_list_url_URLで絶対パスが絶対パスのままか確認(self):
        lc = classlinkchecker.LinkChecker()
        html = '<html><head></head><body>'
        html += '<a href="https://testerchan.hatenadiary.com/test.html"></a>'
        html += '</body></html>'
        list_url = lc.get_list_url('https://testerchan.hatenadiary.com', html)
        #print(list_url)
        expected = 'https://testerchan.hatenadiary.com/test.html'
        self.assertIn(expected,list_url)

    def test_integration_check_url_status(self):
        lc = classlinkchecker.LinkChecker()
        page_info = lc.get_page_info('https://www.testerchan.work/')
        list_url = lc.get_list_url(page_info.url, page_info.text)
        list_error = lc.check_url_status(list_url)
        self.assertEqual(3, len(list_error))
        self.assertEqual('https://www.amazon.co.jp/gp/product/B07CJTF8FP/ref=series_rw_dp_sw', list_error[0]['url'])

if __name__ == '__main__':
    unittest.main()