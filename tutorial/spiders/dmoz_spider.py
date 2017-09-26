#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
import Queue
from scrapy.http import Request
import re as regex

url_queue = Queue.Queue()
count = 0

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    start_urls = [
        "http://www.in263.com/xiangsheng/duikou/"
    ]
    file = open("dialog","a")
    file.write("<dialog>\n")
    file.close()

    def parse(self, response):
        global count
        #This is the list of website containning dialogs
        if response.xpath('//title/text()')[0].extract() == u" 对口相声-相声小品剧本之家" :
            for sel in response.xpath('//ul[@class="left-item"]//h3'):
                url_queue.put(sel.re('href="(.*)" title')[0])
            next_page = response.xpath('//div[@class="page"]/a').re(u'href="(.*)?">下一页')
            if len(next_page) != 0 :
                url_queue.put(next_page[0])
        #in the website containning dialogs
        else :#进入小品对话网页
            content = response.xpath('//*[@id="zoomtext"]/text()|//*[@id="zoomtext"]/p/text()').extract()
            file = open("dialog","a")
            file.write("<s>\n")

            for sentence in content :
                sentence.strip()
                try:
                    file.write(u"%s\n" % sentence)
                except Exception as e:
                    print [sentence]
                    print sentence
                    pass

            file.write("</s>\n\n\n")
            file.close()
            next_page_page = response.xpath('//div[@class="page pages"]/a').re(u'href="(.*)?">下一页')
            if len(next_page_page) != 0:
                yield Request(next_page_page[0])
                return

        if url_queue.empty() == False :
            yield Request(url_queue.get())
            print "dialog:%d\n" %count
            count = count + 1
        else :
            file = open("dialog","a")
            file.write("</dialog>\n")
            file.close()
