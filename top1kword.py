import os
if __name__ == "__main__":
    path = 'C:\\Users\\Administrator\\PycharmProjects\\DataTaggingTool\\civil_keyword'
    xingshi = '刑事'
    xingzheng = '行政'
    minshi = '民事'

    words = dict()

    # with open(xingshi, mode='r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         words[line[:-1]] = line[:-1]
    #
    # with open(xingzheng, mode='r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         words[line[:-1]] = line[:-1]

    with open(minshi, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            words[line[:-1]] = line[:-1]

    cnt = 0
    for top, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(top, file)
            tmp = ''
            with open(file_path, mode='r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    word = line.split(' ')
                    if words.get(word[0]) is not None:
                        cnt += 1
                        continue
                    tmp += word[0] + '\n'
            out_path = 'C:\\Users\\Administrator\\PycharmProjects\\DataTaggingTool\\minshi'
            out_file = os.path.join(out_path, file)
            with open(out_file, mode='w', encoding='utf-8') as f:
                f.write(tmp)
    print(cnt)


