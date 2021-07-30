# _____Building HEATMAP_______

import pandas
import seaborn

data = pandas.read_csv('support_data.csv')

# списки со старыми и новыми названиями сегментов, а также периодами
segments_old = ['Segment 0', 'Segment 1', 'Segment 2']
segments_new = ['Потенциальные клиенты', 'Обычные клиенты', 'VIP-клиенты']
intervals = ['До внедрения роботов', 'После внедрения роботов']

# вымышленные значения
mean_scores = [[1, 2],
               [3, 4],
               [5, 6]]

# настраиваем и строим хитмэп
seaborn.heatmap(mean_scores, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')

# ______Defining mean quality of support for different segments_______

intervals_column = list(data['interval'])
segments_column = list(data['segment'])
score_column = list(data['score'])

mean_scores = []

for segment in segments_old:
    score_sum_before=0
    score_quantity_before=0
    score_sum_after=0
    score_quantity_after=0
    # допишите код
    for index in range(len(data)):
        if segments_column[index] == segment:
            if intervals_column[index] == 'До внедрения роботов':
                score_sum_before+=score_column[index]
                score_quantity_before+=1
            else:
                score_sum_after+=score_column[index]
                score_quantity_after+=1
    segment_scores = [ score_sum_before/score_quantity_before , score_sum_after/score_quantity_after ] # допишите код
    mean_scores.append(segment_scores)
seaborn.heatmap(mean_scores, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')

# ________Defining mean continuity of answers for support________

intervals_column = list(data['interval'])
segments_column = list(data['segment'])
duration_column = list(data['duration'])

mean_duration = []

for segment in segments_old:
    duration_interval=[]
    for interval in intervals:
        duration_rate=0
        duration_counter=0
        for index in range(len(data)):
            if (segments_column[index]==segment and intervals_column[index]==interval):
                duration_rate+=duration_column[index]
                duration_counter+=1
        duration_interval.append(duration_rate/duration_counter)
    mean_duration.append(duration_interval)
seaborn.heatmap(mean_duration, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')

#_________Dive into promo for revealing arguments that helps defuse robotics invasion________

intervals_column = list(data['interval'])
segments_column = list(data['segment'])
promo_column = list(data['promo'])

# ваш код здесь
mean_promo=[]
for segment in segments_old:
    promo_interval=[]
    for interval in intervals:
        promo_rate=0
        promo_counter=0
        for index in range(len(data)):
            if (segments_column[index]==segment and intervals_column[index]==interval):
                promo_rate+=promo_column[index]
                promo_counter+=1
        promo_interval.append(promo_rate/promo_counter)
    mean_promo.append(promo_interval)
seaborn.heatmap(mean_promo, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')