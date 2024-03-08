
with open('1.txt', 'r+', encoding='utf-8') as f_1:
    with open('2.txt', 'r+', encoding='utf-8') as f_2:
        with open('3.txt', 'r+', encoding='utf-8') as f_3:
            line_res = {}
            count_1 = 0
            data_1 = []
            for line in f_1:
                count_1 += 1
                data_1.append(line)
            line_res[count_1] = '1.txt', str(count_1), ''.join(data_1)

            count_2 = 0
            data_2 = []
            for line in f_2:
                count_2 += 1
                data_2.append(line)
            line_res[count_2] = '2.txt', str(count_2), ''.join(data_2)

            count_3 = 0
            data_3 = []
            for line in f_3:
                count_3 += 1
                data_3.append(line)
            line_res[count_3] = '3.txt', str(count_3), ''.join(data_3)

            line_res = sorted(line_res.items())
            line_res = dict(line_res)

            with open('result.txt', 'w', encoding='utf-8') as f_res:
                for key, value in line_res.items():
                    f_res.write(f'{value[0]}\n{value[1]}\n{value[2]}\n')