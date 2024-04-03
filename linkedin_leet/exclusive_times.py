#leet code URL https://leetcode.com/problems/exclusive-time-of-functions/description/


def exclusiveTime(n, logs):
    result = [0] * n
    stack = []
    prev_time = 0

    for log in logs:
        fn_id, event, time = log.split(':')
        fn_id, time = int(fn_id), int(time)

        if event == 'start':
            if stack:
                result[stack[-1]] += time - prev_time
            stack.append(fn_id)
            prev_time = time
        elif event == 'end':
            result[stack.pop()] += time - prev_time + 1
            prev_time = time + 1
    return result    

def main():
    n = 2
    logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    print(exclusiveTime(n, logs))

    n = 1
    logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
    print(exclusiveTime(n, logs))

    n = 2
    logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
    print(exclusiveTime(n, logs))

    n = 2
    logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
    print(exclusiveTime(n, logs))

    n = 1
    logs = ["0:start:0","0:end:0"]
    print(exclusiveTime(n, logs))

main()