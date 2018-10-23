import pandas as pd

#VIDEO_INFO_PATH = 'F:\\test-data-ex\\0729(0-12).csv'
VIDEO_INFO_PATH = 'F:\\0729-history-alarm.csv'

# Series & DataFrame是Pandas中最常用的两个对象
# Series

if __name__ == '__main__':
    #video_info = pd.read_csv(VIDEO_INFO_PATH, encoding='ISO-8859-1')
    video_info = pd.read_csv(VIDEO_INFO_PATH, low_memory=False)

    # shape 可以得到行数和列数
    print(video_info.shape)
    print(video_info.head(n=5))
    '''
    # index保存行索引，columns保存列索引
    print(video_info.columns)
    print(video_info.columns.name)

    # 行索引是一个表示多级索引的MultiIndex对象，每级的索引名可以通过names属性存取
    print(video_info.index)
    print(video_info.index.names)

    # DataFrame对象有两个轴，第0轴为纵轴，第一轴为横轴
    # []运算符可以通过索引标签获取指定的列，当下标是单个标签时，所得到的是Series对象
    # 而当下标是列表时，则得到一个DataFrame对象
    video_id = video_info['VideoID']
    video_object = video_info[['VideoID', 'Start', 'End']]

    # 进行去重操作
    video_object = video_object.drop_duplicates()
    print(video_object)
    print(video_object.values)
    # video_test = video_info[video_info['VideoID'].unique()]

    # .loc[]可通过索引标签获取指定的行，或指定行的某个元素
    # 因为这里没有行索引，所以这里报错video_one = video_info.loc['mv89psg6zh4']

    s = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
    print(u" index", s.index)
    print(u" values", s.values)
    print(s[1:3])
    print(s['b':'d'])
    '''