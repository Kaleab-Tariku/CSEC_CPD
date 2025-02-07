first = list(map(int, input().split()))
second = list(map(int, input().split()))


student_length, fence_height = first[0], first[1]
def check_min_width():
    sum_width = []
    minmum_width = 0
    for i in second:
        count = 1
        if i > fence_height:
            count += 1
            sum_width.append(count)
        else:
            count = 1 
            sum_width.append(count)   
    minmum_width = sum(sum_width)
    print(minmum_width)
check_min_width()
