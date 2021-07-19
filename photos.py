import os

path = 'data'
ep = set()

for f in os.listdir(path):
    m = os.path.splitext(f)
    if m[0] in ep:
        os.remove(os.path.join(path, m[0] + '.MOV'))
    ep.add(m[0])
