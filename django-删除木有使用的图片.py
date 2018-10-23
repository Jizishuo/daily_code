#思路
#在项目根目录新建一个py文件
# 读取django项目-遍历图片的media的文件里的图片取路径
#遍历数据库取文件名
#有保留，没有删除


# 删除没有使用到的图片
import django
from django.conf import settings
import os
import fnmatch
import django



def load_setting():
    # 设置settings文件的位置(xxxxxx换成具体的项目名称)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'xxxxx.settings'
    django.setup()  # 加载xxxx项目


def main():
    # 加载django配置
    load_setting()
    #看具体models在哪
    from blog.models import Blog

    # 获取静态目录的位置（根据自己项目设置路径）
    img_folder = os.path.join(settings.STATICFILES_DIRS[0], 'media', 'article')

    # 查找该目录下的图片文件
    patterns = ['*.jpg', '*.png', '*.gif']
    imgs_del = 0
    imgs_count = 0

    for root, dirs, files in os.walk(img_folder):
        for pattern in patterns:
            for filename in fnmatch.filter(files, pattern):
                # 判断文件是否被使用(content字段是否包含filename)
                if Blog.objects.filter(content__contains=filename).count() == 0:
                    img_path = os.path.join(root, filename)
                    # 若未被使用，则删除
                    os.remove(img_path)
                    imgs_del += 1
                imgs_count += 1

    print('has %s images, delete %s images' % (imgs_count, imgs_del))


if __name__ == '__main__':
    main()