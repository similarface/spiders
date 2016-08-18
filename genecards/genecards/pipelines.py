# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



import MySQLdb
import json
import codecs
#放入到
class GenecardsPipeline(object):
    def __init__(self):
        self.file=codecs.open('genecards_similarface_data_999.json',mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        line=json.dumps(dict(item))+'\n'
        self.file.write(line.decode("unicode_escape"))
        return item
#放入到数据库中
class MySQLStoreGenecardsPipeline(object):
    def __init__(self):
        # user, passwd, db
        self.conn = MySQLdb.connect(user='dna', passwd='dna', db='gendb', host='192.168.30.252', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        # self.cursor.execute('create table free_proxy_list (ip varchar(32), port int, code varchar(16), country varchar(64), anoymity varchar(32), google varchar(4), https varchar(4), last_checked varchar(32));''')

    def process_item(self, item, spider):
        try:
            l = ['rsid','genename','gytogeneticband']
            self.cursor.execute("""
                INSERT INTO t_genecards_rsid_gname(rsid,genename,gytogeneticband,version)
                VALUES (%s, %s, %s,'999')""",
               [item[i] for i in l]
            )
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item