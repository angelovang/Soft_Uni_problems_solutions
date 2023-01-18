def words_sorting(*words):
    #word_dict = {}
    total_sum = 0

    word_dict = {word: sum(map(ord, word)) for word in words}
    # for word in words:
    #     sum = 0
    #     for x in word:
    #         sum += ord(x)
    #     word_dict[word] = sum
    total_sum = sum(word_dict.values())

    if total_sum % 2 == 0:
        result = sorted(word_dict.items(), key=lambda x: x[1])
    else:
        result = sorted(word_dict.items(), key=lambda x: -x[1])
    res_str = []
    for y in result:
        res_str.append(f"{y[0]} - {y[1]}")

    return "\n".join(res_str)


    # res = ''
    # for t in result:
    #     res += f'{t[0]} - {t[1]}\n'
    # # return res
    # res = "\n".join([f'{t[0]} - {t[1]}' for t in result])
    # return res


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))