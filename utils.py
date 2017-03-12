#encoding:utf-8
import web
import datetime,decimal


def int2Date(val_int):
    """
    :function: 将int值的日期，转化为date日期格式
    :author: 熊家炳 2016-12-02
    :param val_int: int类型日期，如 20161203
    :return: 返回日期格式，如2016-12-03 00:00:00
    """
    string_to_date = '-'.join(split_date(val_int))
    return datetime.datetime.strptime(string_to_date, "%Y-%m-%d")


def str2DateInt(val_str):
    """
    :function:将string类型日期的转成int型日期
    :author:熊家炳 2016-12-11
    :param val_str: 类型string，如 '2016-12-19'
    :return: 类型int,如20161219
    """
    d = datetime.datetime.strptime(val_str, "%Y-%m-%d")
    return date2Int(d)


def date2Int(val_date):
    """
    :function:将日期类型转化为int类型
    :author: 熊家炳 2016-12-02
    :param val_date: 日期类型,如 2016-12-03 00:00:00
    :return: 返回int类型,如 20161203
    """
    m = val_date.strftime('%Y-%m-%d')
    return int(m.replace('-',''))


def formatDate2Week(val_int):
    """
    :function:将日期转化为星期
    :author: 熊家炳 2016-12-02
    :param val_int: int类型，如20161203
    :return: 返回string类型，如'sat'
    """
    d = int2Date(val_int)
    return d.strftime('%a')


def formatFinishDay(now_date,delay_days):
    """
    :function:结算日+延迟日期，如果是周末则跳过
    :author: 熊家炳 2016-12-02
    :param now_date: int类型20161203
    :param delay_days: int类型，延迟天数
    :return: 返回日期的int类型 如20161205
    """
    nw = formatDate2Week(now_date)
    next = int2Date(now_date)  # 初始值
    if delay_days == 0:   # 不延迟
        if nw == 'Sat':
            next = int2Date(now_date) + datetime.timedelta(days=2)
        elif nw == 'Sun':
            next = int2Date(now_date) + datetime.timedelta(days=1)
    elif delay_days > 0:  # 延迟
        for i in range(delay_days):
            if nw == 'Fri':
                next = next + datetime.timedelta(days=3)
            elif nw == 'Sat':
                next = next + datetime.timedelta(days=2)
            else:
                next = next + datetime.timedelta(days=1)
            nw = formatDate2Week(date2Int(next))
    return date2Int(next)


def unicodeMoney2Decimal(ustring):
    """
    :function:将unicode类型的金额转化为Decimal类型的小数，保留2为小数
    :author: 熊家炳 20170222
    :param ustring: 类型unicode,如u'5123.4'
    :return: 保留2位小数，如 5123.40
    """
    return (decimal.Decimal(ustring.encode('utf-8'))).quantize(decimal.Decimal('0.01'))
	
	
def str2date(s):
    """
    :function: 字符串转为日期
    :author: 熊家炳 2016-12-24
    :param s: 类型string，如'2016-12-25'
    :return: 类型datetime
    """
    return datetime.datetime.strptime(v, "%Y-%m-%d")
	
	
def minusOrAddDays(val_str,day):
    """
    :function: 日期加减天数
    :author: 熊家炳 2015-12-15
    :param val_str: 类型string,如 ‘20161206’
    :return: 类型int
    """
    return date2Int(int2Date(int(val_str)) + datetime.timedelta(days=day))
	
	
def unicodeStr2Decimal(ustring):
    """
    :function:将unicode类型的百分比利率转化为小数
    :author: 熊家炳 2015-12-13
    :param ustring: 类型unicode,如u'5.4'
    :return: 类型float,保留8位小数，如 0.05400000
    """
    import decimal
    return (decimal.Decimal(ustring.encode('utf-8'))/100).quantize(decimal.Decimal('0.0001'))
	
	
def format_rate(rate):
    """
    :function:将利率转为百分比的形式,至少保留两位小数
    :author: 熊家炳 2016-12-06
    :param rate: 利率 如0.023，0.06534
    :return: 类型string，如0.23%，6.534%
    """
    if rate:
        inverted_str = str(int(rate*100000000))[::-1] # 转成字符串并逆序
        del_zero_str = str(int(inverted_str)) # 转成int，去除
        length = len(del_zero_str)
        if length <= 2:
            return '{:.2f}'.format(rate*100)+'%'
        else:
            return ('{:.'+str(length-2)+'f}').format(rate*100)+'%'
    else:
        return '0.00%'