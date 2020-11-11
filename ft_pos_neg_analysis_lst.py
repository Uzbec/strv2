from . import ft_max_min_sum_count as mms
from . import ft_pos_neg_separator_lst as k
from . import ft_len as l


def ft_pos_neg_analysis_lst(lst):
    neg = k.ft_pos_neg_separator_lst(lst)[0]
    zero = k.ft_pos_neg_separator_lst(lst)[1]
    pos = k.ft_pos_neg_separator_lst(lst)[2]
    kp = mms.ft_max_min_sum_count(pos)[0]
    kn = mms.ft_max_min_sum_count(neg)[0]
    kz = mms.ft_max_min_sum_count(zero)[0]
    mp = mms.ft_max_min_sum_count(pos)[1]
    mn = mms.ft_max_min_sum_count(neg)[1]
    mip = mms.ft_max_min_sum_count(pos)[2]
    min = mms.ft_max_min_sum_count(neg)[2]
    sp = mms.ft_max_min_sum_count(pos)[3]
    sn = mms.ft_max_min_sum_count(neg)[3]
    srp = mms.ft_max_min_sum_count(pos)[4]
    srn = mms.ft_max_min_sum_count(neg)[4]
    kt1 = 1
    if l.ft_len(str(kp)) > 2:
        kt1 -= l.ft_len(str(kp)) - 1
    kt2 = 1
    if l.ft_len(str(mp)) > 3:
        kt2 -= l.ft_len(str(mp)) - 1
    kt3 = 1
    if l.ft_len(str(mip)) > 3:
        kt3 -= l.ft_len(str(mip)) - 1
    kt4 = 3
    if l.ft_len(str(sp)) >= 2:
        kt4 -= l.ft_len(str(sp)) - 1
    kt5 = 2
    if l.ft_len(str(srp)) >= 2:
        kt5 -= l.ft_len(str(srp)) - 2
    otv = "Положительные:" + "\t\t\t" + "Отрицательные:\n" + \
          f"Количество чисел: {kp}," + "\t" * \
          kt1 \
          + f"Количество чисел: {kn},\n" + \
          f"Максимальная цифра: {mp}," + "\t" \
          * kt2 + f"Максимальная цифра: {mn},\n" + \
          f"Минимальная цифра: {mip}," + "\t" \
          * kt3 + f"Минимальная цифра: {min},\n" + \
          f"Сумма чисел: {sp}," + "\t" * kt4 + \
          f"Сумма чисел: {sn},\n" + f"Среднее значение: {srp}" + "\t" * kt5 + \
          f"Среднее значение: {srn}\n\n" + f"Количество нулей: {kz}"
    return otv
