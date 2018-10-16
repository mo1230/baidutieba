## 半自动爬虫开发

- 需求分析
    - 在百度贴吧任意寻找一个帖子，将其源代码复制下来，保存为source.txt。
    - python读入source.txt，通过正则表达式获取用户名、发帖内容和发帖时间，并保存为result.csv
    
- 项目总结

    - 关于正则表达式
        - re.S的作用： 加上re.S后会将整个文件内容当成一个字符串进行匹配，而不会像原来一样一行一行匹配 
    - 关于csv模块
        - 使用python3的字典或者含有字典的列表可以将数据写成csv文件
            > 因为csv文件内容是以表格形式呈现的，所以字典的特性与表格相似，键值对类似鱼表格的表头、数据组合
            
        - 具体的方法可以使用help(csv)查看
      