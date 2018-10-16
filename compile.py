import re


class GetData():
    def get(self, data):
        """
        利用正则表达式从文件中获取用户名，发帖内容和发帖时间
        :param data:
        :return:
        """

        user_name = re.findall('username=".*?"', data, re.S)
        content = re.findall('class="d_post_content j_d_post_content ">(.*?)<', data, re.S)
        time = re.findall('"tail-info">(2018.*?)<', data, re.S)

        return user_name, content, time


