#!/usr/bin/env python
# coding:utf-8

import re
import urlparse
import jieba


def split_url(url):
    return urlparse.urlparse(url)

pattern = re.compile(r'//')


url = "http://www.luxinnerwear.com/javascript_gallery/alibaba/alibaba/login.alibaba.com.php?email=abuse@madecenter.com"
url2 = "http://www.Confirme-paypal.com/"
url3 = "http://www.mmch.co.in/font/index2.html?email=abuse@sfc-ksa.com"
url4 = "http://xxxxx/abc?name=admin&password=admin"
url5 = "http://docs.restala.com/LatestG/file/ServiceLoginAuth.php?cmd=?LOB=RBGLogon&amp;_pageLabel=page_logonform&amp;secured_buyer_page"
url6 = "http://www.legitimate.com//http://www.phishing.com"
url7 = "http://173.236.239.124/wp-content/themes/twentyfourteen/css/alibaba/index.php?email=abuse@houstonlinksmagazine.com"
url8 = "http://www.legitimate.com//http://www.phishing.com"
url9 = "http://www.cclpgms.com/js/?_Acess_Tooken&amp;Acirc;????????????????????????????????792e070ef1e2a9747e63dd241bb32a87792e070ef1e2a9747e63dd241bb32a"
url10 = "http://3designcenter.com/blog/wp-admin/network/other/index.html?.rand&amp;us.battle.net/login/en"
url11 = "http://shop.dominion.dn.ua/templates/redirect/smiles_motivo_para_sorrir_/?https://www.smiles.com.br/promocoes/redireciona/cadastrar/novapromocao/"
string = 'ilikefacebookyouknow'


#print '$'.join(jieba.cut(string))
url_split = urlparse.urlparse(url11)
#print url11
#print pattern.findall(url11)
#print url_split.path


def get_url_query_symbol_2(url):
    url_piece = split_url(url)
    symbols = ['@', '\?', '\.']
    query = url_piece.query
    reg = ''
    for i in symbols:
        reg += '|'+i
    print reg[1:]
    pattern2 = re.compile('@|&|%|\.')
    print len(pattern2.findall(query))

#pattern = re.compile('[@&%\.]')
#print pattern.findall('afa&k@gjl.ajgkla')