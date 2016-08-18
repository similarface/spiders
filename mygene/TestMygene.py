#coding:utf-8
__author__ = 'similarface'

import urllib
import urllib2
import cookielib
import json,sys
'''
登录wegene获取验证码
200 优惠卷
'''
class Wegene:
    def __init__(self):
        self.baseurl='https://www.mygene.com/'
        self.login_url=''
        self.login_post='https://www.mygene.com/Home/Public/login.html'

    def login(self):
        '''
        登录wegene 代码
        :return:
        '''
        #存放cookie
        opener=self.saveCookieInFIle('/tmp/mygene.txt')
        request_header,form_data = self.structure_headers()
        try :
            #登录返回jdon字符
            result=opener.open(self.login_post,form_data)
            jsonStr=json.loads(result.read().decode('utf-8'))
            errno=jsonStr.get('errno')
            err=jsonStr.get('err')
        except Exception,e :
            print(e)
            if hasattr(e, "code"):
                print "The server couldn't fulfill the request.Please check your url and read the Reason"
                print "Error code: %s" % e.code
            elif hasattr(e, "reason"):
                print "We failed to reach a server. Please check your url and read the Reason"
                print "Reason: %s" % e.reason
                sys.exit(2)
        if errno == 1 :
            print "登陆成功!"
            return opener
        else:
            print("登陆失败!"+err)
            return False

    def structure_headers(self):
        postData={
            "return_url":"https://www.mygene.com/",
             'family': '',
             'username': 'Ywj',
             'password': '198998',
             'remember': 1
        }
        headers={
            # "Accept":"application/json, text/javascript, */*; q=0.01",
            # "Accept-Language":"zh-CN,zh;q=0.8",
            # "Connection":"keep-alive",
            # "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            # "Host":"www.wegene.com",
            # "Origin":"https://www.mygene.com",
            # "Referer":"https://www.mygene.com/account/login/",
            # "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
            # "X-Requested-With":"XMLHttpRequest"
            #
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36",
            "Host": "www.mygene.com",
            "Content-Length": 36,
            "Origin": "https://www.mygene.com",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.mygene.com/Home/Public/login.html"
        }
        return headers,urllib.urlencode(postData)

    def getLink(self,url):
        opener=self.login()
        if opener:
            print(opener.open(url).read().decode('utf-8'))


    def getCookieOpener(self):
        #声明一个cookieJar对象实现来保存cookie
        cookie=cookielib.CookieJar()
        #利用urllib2库的HTTPCookieProcessor对象来创建处理器
        handler=urllib2.HTTPCookieProcessor(cookie)
        #通过handler来构建opener
        opener=urllib2.build_opener(handler)
        response=opener.open(self.baseurl)
        return opener

    def saveCookieInFIle(self,filename='/tmp/filecookiefile.txt'):
        '''
        保存cookie 到 文件中
        :param filename:
        :return:
        '''
        #设置保存cookie的文件 如果没给出默认在/tmp/filecookiefile.txt
        cookie=cookielib.MozillaCookieJar(filename)
        #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        handler=urllib2.HTTPCookieProcessor(cookie)
        #通过handler来构建opener
        opener = urllib2.build_opener(handler)
        #访问的url 进行cookie生成
        opener.open(self.baseurl)
        #保存cookie到文件
        cookie.save(ignore_discard=True, ignore_expires=True)
        return opener

    def getCookieFromFile(self,filename='/tmp/filecookiefile.txt'):
        #创建MozillaCookieJar实例对象
        cookie = cookielib.MozillaCookieJar()
        #从文件中读取cookie内容到变量
        cookie.load('/tmp/filecookiefile.txt', ignore_discard=True, ignore_expires=True)
        #利用urllib2的build_opener方法创建一个opener
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        return opener


    def strunctPromoHeader(self,promocode):
        postData={
            "promo_code":promocode
        }
        headers={
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36",
            "Host": "www.mygene.com",
            "Content-Length": 36,
            "Origin": "https://www.mygene.com",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.mygene.com/Home/Public/login.html"
        }
        return headers,urllib.urlencode(postData)

    def strunctPromoHeader1(self):
        postData={
            "promo_code":"BGI99999"
        }
        headers={
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Content-Length":"19",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Host":"www.wegene.com",
            "Origin":"https://www.wegene.com",
            "Referer":"https://www.wegene.com/shop/cart/",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
        }
        return headers,urllib.urlencode(postData)

    def addCar(self):
        '''
        模拟加入购物车
        :return:返回session 对象
        '''
        #首先登录
        opener=self.login()
        #
        addCar="https://www.wegene.com/shop/ajax/add_cart/"
        postData={
            "item_id":"3",
            "_post_type":"ajax"
        }
        form_data=urllib.urlencode(postData)
        if opener:
            print(opener.open(addCar,form_data).read().decode("utf-8"))
            return opener
    def getPromoCode(self):
        '''
        获取优惠码
        :return:
        '''
        #加入商品到购物车
        opener=self.addCar()
        #优惠码地址
        promocodeUrl='https://www.wegene.com/promo/ajax/apply_code/'
        #获取优惠码
        if opener:
            for i in range(1,100000):
                resultPromo=opener.open(promocodeUrl,self.strunctPromoHeader('BGI'+str(i))[1])
                jsonPromoStr=json.loads(resultPromo.read().decode('utf-8'))
                print(i,jsonPromoStr)

if __name__=="__main__":
    we=Wegene()
    #we.getLink('https://www.wegene.com/inbox/')
    we.getPromoCode()
    #we.saveCookieInFIle()