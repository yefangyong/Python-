from urllib import request
import re


class Spider:
    url = "https://www.xy.com"
    root_pattern = '<div class="video-info">([\s\S]*)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'
    index_pattern = '<a class="game_pic" href="([\s\S]*?)" target="_blank">([\s\S]*?)</a>'
    img_patten = '<img src=([\s\S]*?)>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls


    def __analysis(self,htmls):
       root_html = re.findall(self.index_pattern, htmls)
       anchors = []
       for html in root_html:
           imageUrl = re.findall(self.img_patten, html[1])
           # number = re.findall(self.number_pattern, html)
           anchor = {'imageUrl': imageUrl}
           anchors.append(anchor)
       return anchors

    def __refine(self, anchors):
        f = lambda anchor: {
            'imageUrl': anchor['imageUrl'][0].strip(),
            #'number': anchor['number'][0]
        }
        return map(f,anchors)

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = self.__refine(anchors)
        print(list(anchors))


spider = Spider()
spider.go()
