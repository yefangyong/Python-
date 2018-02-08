from urllib import request
import re


class Spider:
    url = "https://www.panda.tv/cate/lol"
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'
    index_pattern = '<a class="game_pic" href="http://cqsj.xy.com/" target="_blank">([\s\S]*?)</a>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls


    def __analysis(self,htmls):
       root_html = re.findall(self.root_pattern, htmls)
       anchors = []
       for html in root_html:
           name = re.findall(self.name_pattern, html)
           number = re.findall(self.number_pattern, html)
           anchor = {'name': name, 'number': number}
           anchors.append(anchor)
       return anchors

    def __refine(self,anchors):
        f = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
        }
        return map(f,anchors)

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = self.__refine(anchors)
        print(list(anchors))



spider = Spider()
spider.go()