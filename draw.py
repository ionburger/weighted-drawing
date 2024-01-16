import random
import os
def choice(file):
    try:
        with open (file) as f:
            data = f.read()
    except:
        os.remove(file)
        return "Invalid file"
    os.remove(file)

    pool = []
    passes = data.split("\n")
    for p in passes:
        p = p.split(",")
        if not p[0].isnumeric():
            continue
        for i in range(int(p[1])):
            pool.append(p[0])

    answer = random.choice(pool)
    print(answer)
    return answer