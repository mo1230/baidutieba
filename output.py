import csv

class Output():
    def output(self, name, content, time):
        """
        将结果输出并保存为csv文件
        :param name:
        :param content:
        :param time:
        :return:
        """

        result_list = []
        """
        while len(name):
            result = {"username": name[count],
                      "content": content[count],
                      "time": time[count]}
            count += 1

            result_list.append(result)
            if count == len(name):
                break
        """

        for i in range(len(name)):
            result = {"username": name[i],
                      "content": content[i],
                      "time": time[i]}
            result_list.append(result)

        with open("result.csv", "w", encoding="utf-8") as f:
            fwriter = csv.DictWriter(f, fieldnames=["username", "content", "time"])
            fwriter.writeheader()
            fwriter.writerows(result_list)






