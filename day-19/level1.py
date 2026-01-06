f = open('./day-19/obama_speech.txt')

def count_lines(para1):
    lines = f.readlines()
    lines_count = len(lines)
    return lines_count

def count_words(para2):
    f.seek(0)
    lines = f.readlines()
    word_sum = 0
    for i in lines:
        word_sum = word_sum + len(i.split())
    return word_sum



print(count_lines(f), ' riviä puheessa', count_words(f), ' sanaa tekstissä')