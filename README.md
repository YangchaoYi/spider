Learning how to crawl data from websites 
Learning how to use regex to deal with text(unicode)

data source: 
http://www.in263.com/xiangsheng/duikou/ 
This is a Chinese crosstalk website. I find this website suitable for building a dialog dataset.

Firstly, I use dmoz_spider.py file to scrawl data from this website. 
Then I use formalize.py to formalize the raw data.

If you want to get the same result: download the project enter the dir containing the `spider` folder and run:
```
scrapy crawl dmoz
```
You will the the `dialog` file then run the `formalize.py` you get a `amend` file which is formalized data
