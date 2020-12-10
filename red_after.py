import matplotlib.pyplot as plt


def comma(s):
    for i in range(len(s)):
        if s[i] == ',':
            ans = s[0:i] + '.' + s[i + 1:len(s)]
            return ans


fig = plt.figure()
plt.xlabel('Длина волны, нм')
plt.ylabel('Уровень сигнала')

blk = []
x = []
y = []
max_y = 0
max_z = 0
with open('BLACK1.DAT', 'r') as file:
    s = file.read().split('\n')
    s = s[4:]
    s = [(j.split()) for j in s]
    for j in range(len(s)):
        if s[j]:
            blk.append(int(s[j][1]))
with open('GREEN1.DAT', 'r') as file:
    s = file.read().split('\n')
    s = s[4:]
    s = [(j.split()) for j in s]
    for j in range(len(s)):
        if s[j]:
            x.append(435.83 + (int(s[j][0]) - 1222)*(546.074-435.83)/(1701-1222))
            y.append(int(s[j][1]) - blk[j])

plt.plot(x, y, color='blue')

plt.minorticks_on()

plt.grid(which='major', color='k', linewidth=1)
plt.grid(which='minor', color='k', linestyle=':')
plt.legend()

plt.show()
