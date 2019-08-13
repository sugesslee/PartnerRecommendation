#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-08-10 10:09
@Author  : red
@Site    : 
@File    : execute_data.py
@Software: PyCharm
"""
import time
import os
import sys
import xml.sax
import re
import utils.sql_util as sql

# author|editor|title|booktitle|pages|year|address|journal|volume|number|month|url|ee|cdrom|cite|publisher|note|crossref|isbn|series|school|chapter|publnr
paper_tags = ('article', 'inproceedings', 'proceedings', 'book', 'incollection', 'phdthesis', 'mastersthesis', 'www',
              'person', 'data')


# sub_tags = ('publisher', 'journal', 'booktitle')


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.id = 1
        self.kv = {}
        self.reset()
        self.params = []
        self.batch_len = 10

    def reset(self):
        self.curtag = None
        self.pid = None
        self.ptag = None
        self.booktitle = None
        self.title = None
        self.address = None
        self.journal = None
        self.volume = None
        self.number = None
        self.month = None
        self.cdrom = None
        self.city = None
        self.pages = None
        self.publisher = None
        self.note = None
        self.crossref = None
        self.isbn = None
        self.series = None
        self.school = None
        self.chapter = None
        self.publnr = None
        self.editor = None
        self.author = None
        self.tag = None
        # self.subtag = None
        # self.subtext = None
        self.year = None
        self.url = None
        self.mdate = None
        self.key = None
        self.publtype = None
        self.ee = None
        self.kv = {}

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        if tag is not None and len(tag.strip()) > 0:
            self.curtag = tag

            if tag in paper_tags:
                self.reset()
                self.pid = self.id
                self.kv['ptag'] = str(tag)
                self.kv['id'] = self.id
                self.id += 1

                if attributes.__contains__('key'):
                    self.key = str(attributes['key'])

                if attributes.__contains__('mdate'):
                    self.mdate = str(attributes['mdate'])

                if attributes.__contains__('publtype'):
                    self.publtype = str(attributes['publtype'])
            # elif tag in sub_tags:
            #     self.kv['sub_tag'] = str(tag)

    # 元素结束事件处理
    def endElement(self, tag):
        if tag == 'title':
            self.kv['title'] = str(self.title)
        elif tag == 'author':
            self.author = re.sub(' ', '_', str(self.author))
            if not self.kv.__contains__('author'):
                self.kv['author'] = []
                self.kv['author'].append(str(self.author))
            else:
                self.kv['author'].append(str(self.author))
        elif tag == 'ee':
            self.ee = re.sub(' ', '_', str(self.ee))
            if not self.kv.__contains__('ee'):
                self.kv['ee'] = []
                self.kv['ee'].append(str(self.ee))
            else:
                self.kv['ee'].append(str(self.ee))
        elif tag == 'url':
            self.kv['url'] = str(self.url)
        elif tag == 'editor':
            self.kv['editor'] = str(self.editor)
        elif tag == 'volume':
            self.kv['volume'] = str(self.volume)
        elif tag == 'year':
            self.kv['year'] = str(self.year)

        elif tag in paper_tags:
            tid = int(self.kv['id']) if self.kv.__contains__('id') else 0
            ptag = self.kv['ptag'] if self.kv.__contains__('ptag') else 'NULL'

            try:
                title = self.kv['title'] if self.kv.__contains__('title') else 'NULL'
            except Exception as e:
                title = ''
            author = self.kv['author'] if self.kv.__contains__('author') else 'NULL'
            author = ','.join(author) if author is not None else 'NULL'
            ee = self.kv['ee'] if self.kv.__contains__('ee') else 'NULL'
            ee = ','.join(ee) if ee is not None else 'NULL'
            # subtag = self.kv['subtag'] if self.kv.__contains__('subtag') else 'NULL'
            # sub_detail = self.kv['sub_detail'] if self.kv.__contains__('sub_detail') else 'NULL'
            year = self.kv['year'] if self.kv.__contains__('year') else 0
            url = self.kv['url'] if self.kv.__contains__('url') else 'NULL'
            editor = self.kv['editor'] if self.kv.__contains__('editor') else 'NULL'
            volume = self.kv['volume'] if self.kv.__contains__('volume') else 'NULL'
            mdate = self.mdate if self.mdate else 'NULL'
            key = self.key if self.key else 'NULL'
            publtype = self.publtype if self.publtype else 'NULL'
            param = (str(tid), ptag, title, author, year, url, mdate, key, publtype, editor, volume, ee)
            print(param)
            # self.params.append(param)
            # if len(self.params) % 100 == 0:
            # sql_str = "INSERT INTO `dblp`.`paper`(`id`, `author`, `editor`, `title`, `book_title`, `year`, `address`," \
            #           " `journal`, `volume`, `number`, `month`, `url`, `ee`, `cdrom`, `city`, `mdate`, `key`," \
            #           " `pages`, `publisher`, `note`, `crossref`, `isbn`, `series`, `school`, `chapter`, `publnr`)" \
            #           " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
            #           " %s, %s, %s, %s)"
            #     sql.insertmany(sql_str, self.params)
            #     self.params[:] = []

    # 内容事件处理
    def characters(self, content):
        if self.curtag == "title":
            self.title = content.strip()
        elif self.curtag == "author":
            self.author = content.strip()
        elif self.curtag == "year":
            self.year = content.strip()
        elif self.curtag == "url":
            self.url = content.strip()
        elif self.curtag == 'editor':
            self.editor = content.strip()
        elif self.curtag == 'volume':
            self.volume = content.strip()
        elif self.curtag == 'ee':
            self.ee = content.strip()


if __name__ == "__main__":
    filename = '/Users/red/Desktop/temp/PartnerRecommendation/dblp/data/dblp.xml'

    # 创建一个 XMLReader
    parser = xml.sax.make_parser()

    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse(filename)
    print('Parser Complete!')
