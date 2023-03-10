import pymysql


def get_coon():
    coon = pymysql.connect(
        host='192.168.176.128:8888',
        user='root',
        password='a123456.',
        database='test_demo',
        charset='utf8mb4'
    )

    return coon

