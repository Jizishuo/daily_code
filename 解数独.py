import numpy as np
from queue import Queue, LifoQueue


class Sudo():
    def __init__(self, data):
        # 数据初始化(二维的object数组，值可填数字和list)
        self.value = np.array([[0] * 9] * 9, dtype=object)
        self.new_points = Queue()  # 先进先出的新解坐标

        # 后半部分算法需要的属性
        self.recoder = LifoQueue()  # 先进后出的回溯器
        self.guess_times = 0  # 猜测次数

        # 九宫格的基准列表
        self.base_points = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

        # 整理数据
        # 将81个元素的list转化为9*9的二维数组
        data = np.array(data).reshape(9, -1)
        for r in range(0, 9):
            for c in range(0, 9):
                if data[r, c]:
                    self.value[r, c] = data[r, c]
                    # 新点添加到列表中，以便遍历
                    self.new_points.put((r, c))
                else:
                    self.value[r, c] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            # 剔除数字
            def _cut_num(self, point):
                r, c = point
                val = self.value[r, c]

                # 行
                for i, item in enumerate(self.value[r]):
                    if isinstance(item, list):
                        if item.count(val):
                            item.remove(val)

                            # 判断移除后，是否剩下一个元素
                            if len(item) == 1:
                                self.new_points.put((r, i))
                                self.value[r, i] = item[0]

                # 列
                for i, item in enumerate(self.value[:, c]):
                    if isinstance(item, list):
                        if item.count(val):
                            item.remove(val)

                            # 判断移除后，是否剩下一个元素
                            if len(item) == 1:
                                self.new_points.put((i, c))
                                self.value[i, c] = item[0]

                # 所在九宫格(3x3的数组)
                b_r, b_c = map(lambda x: x / 3 * 3, point)  # 九宫格基准点
                for m_r, row in enumerate(self.value[b_r:b_r + 3, b_c:b_c + 3]):
                    for m_c, item in enumerate(row):
                        if isinstance(item, list):
                            if item.count(val):
                                item.remove(val)

                                # 判断移除后，是否剩下一个元素
                                if len(item) == 1:
                                    r = b_r + m_r
                                    c = b_c + m_c
                                    self.new_points.put((r, c))
                                    self.value[r, c] = item[0]



data = [0,0,2, 8,0,1, 0,7,0,
            4,0,0, 0,0,0, 0,0,1,
            5,0,8, 7,0,0, 9,0,4,
            0,0,0, 6,5,0, 1,4,0,
            6,2,0, 0,0,0, 3,9,0,
            1,7,0, 0,3,8, 2,6,0,
            2,5,3, 4,8,7, 6,1,9,
            0,0,6, 3,0,9, 7,5,2,
            0,9,1, 5,0,0, 4,8,3]

a = Sudo(data)
print(a.cut_num)