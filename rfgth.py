p1 = plt.bar(index, tips_sum_by_day_male,
             bar_width,
             color='b',
             alpha=alpha,
             label='Male')
p2 = plt.bar(index + bar_width, tips_sum_by_day_female,
                                       bar_width,
                                       color='r',
                                       alpha=alpha,
                                       label='Female')