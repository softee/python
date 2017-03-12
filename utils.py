#encoding:utf-8
import web
import datetime,decimal


def int2Date(val_int):
    """
    :function: ��intֵ�����ڣ�ת��Ϊdate���ڸ�ʽ
    :author: �ܼұ� 2016-12-02
    :param val_int: int�������ڣ��� 20161203
    :return: �������ڸ�ʽ����2016-12-03 00:00:00
    """
    string_to_date = '-'.join(split_date(val_int))
    return datetime.datetime.strptime(string_to_date, "%Y-%m-%d")


def str2DateInt(val_str):
    """
    :function:��string�������ڵ�ת��int������
    :author:�ܼұ� 2016-12-11
    :param val_str: ����string���� '2016-12-19'
    :return: ����int,��20161219
    """
    d = datetime.datetime.strptime(val_str, "%Y-%m-%d")
    return date2Int(d)


def date2Int(val_date):
    """
    :function:����������ת��Ϊint����
    :author: �ܼұ� 2016-12-02
    :param val_date: ��������,�� 2016-12-03 00:00:00
    :return: ����int����,�� 20161203
    """
    m = val_date.strftime('%Y-%m-%d')
    return int(m.replace('-',''))


def formatDate2Week(val_int):
    """
    :function:������ת��Ϊ����
    :author: �ܼұ� 2016-12-02
    :param val_int: int���ͣ���20161203
    :return: ����string���ͣ���'sat'
    """
    d = int2Date(val_int)
    return d.strftime('%a')


def formatFinishDay(now_date,delay_days):
    """
    :function:������+�ӳ����ڣ��������ĩ������
    :author: �ܼұ� 2016-12-02
    :param now_date: int����20161203
    :param delay_days: int���ͣ��ӳ�����
    :return: �������ڵ�int���� ��20161205
    """
    nw = formatDate2Week(now_date)
    next = int2Date(now_date)  # ��ʼֵ
    if delay_days == 0:   # ���ӳ�
        if nw == 'Sat':
            next = int2Date(now_date) + datetime.timedelta(days=2)
        elif nw == 'Sun':
            next = int2Date(now_date) + datetime.timedelta(days=1)
    elif delay_days > 0:  # �ӳ�
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
    :function:��unicode���͵Ľ��ת��ΪDecimal���͵�С��������2ΪС��
    :author: �ܼұ� 20170222
    :param ustring: ����unicode,��u'5123.4'
    :return: ����2λС������ 5123.40
    """
    return (decimal.Decimal(ustring.encode('utf-8'))).quantize(decimal.Decimal('0.01'))
	
	
def str2date(s):
    """
    :function: �ַ���תΪ����
    :author: �ܼұ� 2016-12-24
    :param s: ����string����'2016-12-25'
    :return: ����datetime
    """
    return datetime.datetime.strptime(v, "%Y-%m-%d")
	
	
def minusOrAddDays(val_str,day):
    """
    :function: ���ڼӼ�����
    :author: �ܼұ� 2015-12-15
    :param val_str: ����string,�� ��20161206��
    :return: ����int
    """
    return date2Int(int2Date(int(val_str)) + datetime.timedelta(days=day))
	
	
def unicodeStr2Decimal(ustring):
    """
    :function:��unicode���͵İٷֱ�����ת��ΪС��
    :author: �ܼұ� 2015-12-13
    :param ustring: ����unicode,��u'5.4'
    :return: ����float,����8λС������ 0.05400000
    """
    import decimal
    return (decimal.Decimal(ustring.encode('utf-8'))/100).quantize(decimal.Decimal('0.0001'))
	
	
def format_rate(rate):
    """
    :function:������תΪ�ٷֱȵ���ʽ,���ٱ�����λС��
    :author: �ܼұ� 2016-12-06
    :param rate: ���� ��0.023��0.06534
    :return: ����string����0.23%��6.534%
    """
    if rate:
        inverted_str = str(int(rate*100000000))[::-1] # ת���ַ���������
        del_zero_str = str(int(inverted_str)) # ת��int��ȥ��
        length = len(del_zero_str)
        if length <= 2:
            return '{:.2f}'.format(rate*100)+'%'
        else:
            return ('{:.'+str(length-2)+'f}').format(rate*100)+'%'
    else:
        return '0.00%'