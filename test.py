#斐波拉切数列
sequence = [0, 1]
count = int(input("请输入要查找的数："))
for i in range(len(sequence), count):
    sequence.append(sequence[i - 2] + sequence[i - 1])
print(sequence[count - 1])