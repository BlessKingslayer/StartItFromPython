from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)      # 可以自动修正HTML
result = etree.tostring(html) # 是bytes类型
print('-' * 30, 'etree.HTML(text)', '-' * 30)
print(result.decode('utf-8'))


#region 从文件读取html

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print('-' * 30, 'etree.parse()', '-' * 30)
print(result.decode('utf-8'))

#endregion

#region 选取所有节点
result = html.xpath('//*')
print('-' * 30, '选取所有节点', '-' * 30)
print(result)
#endregion

#region 选取所有li节点
result = html.xpath('//li')
print('-' * 30, '选取所有li节点', '-' * 30)
print(result)
print('-' * 30, '选取第2个li节点', '-' * 30)
print(result[1])
#endregion

#region 选取所有li下的子节点中的a节点
result = html.xpath('//li/a') # 无法获取孙节点中的a节点
print('-' * 30, '选取所有li下的子节点中的a节点', '-' * 30)
print(result)
#endregion

#region 选取所有属性为href="link4.html"的a节点 的父节点的class属性
result = html.xpath('//a[@href="link4.html"]/../@class')
# 以下写法相同
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print('-' * 30, '选取所有属性为href="link4.html"的a节点 的父节点的class属性', '-' * 30)
print(result)
#endregion

#region 选取指定节点的文本
result = html.xpath('//li[@class="item-0"]/text()')
print('-' * 30, '选取指定节点的文本', '-' * 30)
print(result) # 自动修正的li尾标签换行 所以得到一个换行符
#endregion

#region 选取指定节点及其所有子孙节点的文本
result = html.xpath('//li[@class="item-0"]//text()')
print('-' * 30, '选取指定节点及其所有子孙节点的文本', '-' * 30)
print(result)
#endregion

#region 选取指定节点属性值
result = html.xpath('//li/a/@href')
print('-' * 30, '选取指定节点属性值', '-' * 30)
print(result)
#endregion

#region 选取属性为多个值的节点 及其 属性
text2 = '''<li class="li li-first ss"><a href="link.html">first team</a></li>
          <li class="li li-first2 ss"><a href="link.html">first2 team</a></li>
        '''
html2 = etree.HTML(text2)
result = html2.xpath('//li[contains(@class, "li li-first2")]/a/text()')
print('-' * 30, '选取属性为多个值的节点', '-' * 30)
print(result)
result = html2.xpath('//li[2]/attribute::*')
print('-' * 30, '获取属性为多个值的节点的属性', '-' * 30)
print(result)
#endregion

#region 选取所有祖先节点
result = html.xpath('//li[1]/ancestor::*')
print('-' * 30, '选取所有祖先节点', '-' * 30)
print(result)
#endregion


