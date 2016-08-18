#coding:utf-8
__author__ = 'similarface'
import json
import MySQLdb



def getConn():
    connection=MySQLdb.connect(user='dna', db='genedb', passwd='dna', host='192.168.30.252')
    return connection

def insertRsid(RsidInfo):
    #db = MySQLdb.connect(user='dna', db='genedb', passwd='dna', host='192.168.30.252')
    #cursor = db.cursor()
    sql='insert into mygene_rsidinfo(chrom,startpos,endtpos,genename ,genebase ,rsid,rsiddesc,assess,gene,created,modified) VALUES ('+RsidInfo.chrom+','+RsidInfo.startpos+','+RsidInfo.endtpos+','+RsidInfo.genename+','+RsidInfo.genebase+','+RsidInfo.rsid+','+RsidInfo.rsiddesc+','+RsidInfo.assess+','+RsidInfo.gene+',now(),now())'
    print(sql)
    #cursor.execute()
    #names = [row[0] for row in cursor.fetchall()]
    #db.close()
    return ""


def jsonToRsidObj(json):
    rsidobjs=[]
    rsidslist=[]
    for i in json:
        rsidobj=RsidInfo()
        rsidobj.chrom=i['染色体']
        rsidobj.startpos=i['起始坐标']
        rsidobj.endtpos=i['终止坐标']
        rsidobj.genename=i['基因']
        rsidobj.genebase=i['参考碱基']
        rsidobj.gene=i['基因型']
        rsidobj.assess=i['评价']
        rsidobj.rsid=i['RS号']
        rsidobj.rsiddesc=i['位点介绍']
        rsidid=getRsid(rsidobj.rsid)
        if not rsidid:
            insertRsid(rsidobj)
            drugid=getDrugId()
            addRelationShipDrugRsid(rsidid,drugid)
        else:
            print('Rsid已经存在，不进行入库操作!')

def getRsid(rsid):
    cursor = getConn().cursor()
    rsidid = cursor.execute('select id from mygene_rsidinfo where rsid='+rsid)

def getDrugId(cname):
    #cursor = getConn().cursor()
    SQL="SELECT ID from mygene_drug where cname="+"'"+cname+"'"
    print(SQL)

def addRelationShipDrugRsid(rsid,drugid):
    pass

# jsonStr=[{"染色体":"10号","起始坐标":"101563815","终止坐标":"101563815","基因":"ABCC2","参考碱基":"G","基因型":"G/G","RS号":"rs2273697","位点介绍":"正常的卡马西平效果","评价":"triangle-up"},{"染色体":"6号","起始坐标":"31783755","终止坐标":"31783755","基因":"HSPA1A","参考碱基":"T","基因型":"C/C","RS号":"rs1043620","位点介绍":"可能导致过敏反应，轻度红斑性皮疹，史蒂文斯-约翰逊综合征（SJS），中毒性表皮坏死松解症","评价":"triangle-down"},{"染色体":"6号","起始坐标":"31785228","终止坐标":"31785228","基因":"HSPA1A","参考碱基":"G","基因型":"G/G","RS号":"rs506770","位点介绍":"样品未覆盖","评价":"triangle-grey"},{"染色体":"6号","起始坐标":"33774394","终止坐标":"33774394","基因":"MLN","参考碱基":"C","基因型":"C/C","RS号":"rs2894342","位点介绍":"正常的代谢反应","评价":"triangle-up"},{"染色体":"6号","起始坐标":"30946148","终止坐标":"30946148","基因":"MUC21","参考碱基":"G","基因型":"G/A","RS号":"rs2844682","位点介绍":"在亚洲患者中，导致约翰逊-史提芬综合征的风险更高","评价":"triangle-down"},{"染色体":"6号","起始坐标":"31778272","终止坐标":"31778272","基因":"HSPA1L","参考碱基":"G","基因型":"A/A","RS号":"rs2227956","位点介绍":"可能导致过敏反应，轻度红斑性皮疹，史蒂文斯-约翰逊综合征（SJS），中毒性表皮坏死松解症","评价":"triangle-down"},{"染色体":"2号","起始坐标":"166909544","终止坐标":"166909544","基因":"SCN1A","参考碱基":"C","基因型":"C/C","RS号":"rs3812718","位点介绍":"正常的代谢反应","评价":"triangle-up"},{"染色体":"6号","起始坐标":"30699384","终止坐标":"30699384","基因":"FLOT1","参考碱基":"G","基因型":"G/G","RS号":"rs3909184","位点介绍":"在亚洲患者中，导致约翰逊-史提芬综合征的风险更高","评价":"triangle-down"},{"染色体":"6号","起始坐标":"31285935","终止坐标":"31285935","基因":"HLA-B","参考碱基":"G","基因型":"G/G","RS号":"rs3130690","位点介绍":"正常的代谢反应","评价":"triangle-up"},{"染色体":"6号","起始坐标":"29913298","终止坐标":"29913298","基因":"HLA-A","参考碱基":"A","基因型":"A/A","RS号":"rs1061235","位点介绍":"正常的卡马西平效果","评价":"triangle-up"}]
#
#
# rsidlist=[]
# for i in jsonStr:
#     eachrsid=i
#     print(i['染色体'])
#     rsidlist.append(i['RS号'])


dictQ={"染色体":"chrom","起始坐标":"startpos","终止坐标":"endtpos","基因":"genename","参考碱基":"genebase","基因型":"gene","RS号":"rsid","位点介绍":"rsiddesc","评价":"assess"}

if __name__=='__main__':
    getDrugId('xsd')