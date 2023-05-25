import random
import math
from matplotlib import pyplot as plt
import scipy.integrate as si
import numpy as np
import scipy.stats

sigma = 1
density = 1000


def getData(density, sigma):
    list_r = []
    list_g = []
    list_f = []

    for i in range(density):
        list_r.append(random.random())
    list_r.sort()

    for i in range(density):
        # list_g.append(1/(1-math.exp(-((list_r[i]**2)/(2*0.5**2)))))
        list_g.append(math.sqrt(-2 * sigma ** 2 * math.log(1 - list_r[i], math.e)))

    list_x2 = np.linspace(0, 6, density)
    for i in range(density):
        list_f.append(list_x2[i] / sigma ** 2 * math.exp(-((list_x2[i] ** 2) / (2 * sigma ** 2))))

    return list_r, list_g, list_x2, list_f


list_r, list_g, list_x2, list_f = getData(density, sigma)


# for i in range(density):
#    print('X = ', list_r[i], '  Y = ', list_g[i])


def getHistList(delta_list, list_g, sigma, N, density):
    vList = []
    flist = []
    z_list = []
    for j in range(1, N + 1):
        count = 0
        for i in range(len(list_g)):
            if list_g[i] <= delta_list[j] and list_g[i] >= delta_list[j - 1]:
                count += 1
        vList.append(count / (density * (abs(delta_list[j] - delta_list[j - 1]))))

    for j in range(1, N + 1):
        h = abs(delta_list[j] - delta_list[j - 1]) / 2
        flist.append(
            (delta_list[j - 1] + h) / sigma ** 2 * math.exp(-(((delta_list[j - 1] + h) ** 2) / (2 * sigma ** 2))))
        z_list.append(delta_list[j - 1] + h)

    return vList, flist, z_list


deltaList = np.linspace(0, 3, 15)


def getCharacteristics(list_g, sigma):
    f1 = lambda x: x * x / sigma ** 2 * math.exp(-x ** 2 / (2 * sigma ** 2))
    Mat_Oj = si.quad(f1, 0, math.inf)

    f2 = lambda x: (x - Mat_Oj[0]) ** 2 * x / sigma ** 2 * math.exp(-x ** 2 / (2 * sigma ** 2))
    Dispersion = si.quad(f2, 0, math.inf)

    Sredn = 0
    for i in range(len(list_g)):
        Sredn += list_g[i]
    Sredn = Sredn / len(list_g)

    Razmax = list_g[-1] - list_g[0]

    Vib_Dispersion = 0
    for i in range(len(list_g)):
        Vib_Dispersion += (list_g[i] - Sredn) ** 2
    Vib_Dispersion = Vib_Dispersion / len(list_g)

    dif1 = abs(Mat_Oj[0] - Sredn)
    dif2 = abs(Dispersion[0] - Vib_Dispersion)

    Mediana = sigma * math.sqrt(math.log(4, math.e))
    return Mat_Oj[0], Sredn, dif1, Dispersion[0], Vib_Dispersion, dif2, Mediana, Razmax


def getCount(delta_list, list_g, N):
    countList = []
    countList.append(0)
    for j in range(1, N):
        count = 0
        for i in range(len(list_g)):
            if list_g[i] <= delta_list[j] and list_g[i] >= delta_list[j - 1]:
                count += 1
        countList.append(count)
    countList.append(0)

    return countList


Mat_Oj, Sredn, dif1, Dispersion, Vib_Dispersion, dif2, Mediana, Razmax = getCharacteristics(list_g, sigma)

print('Математическое ожидание: ', Mat_Oj)
print('Выборочное среднее: ', Sredn)
print("Разность1: ", dif1)
print("Дисперсия: ", Dispersion)
print("Выборочная дисперсия: ", Vib_Dispersion)
print("Разность2: ", dif2)
print("Медиана: ", Mediana)
print('Размах выборки: ', Razmax)

N = 10
min = list_g[0]
max = list_g[-1]

delta = (max - min) / N + 2
delta_list = np.linspace(min, max, N + 2)
z_list = []

vList, flist, z_list = getHistList(delta_list, list_g, sigma, N, density)

for i in range(N):
    print(f'z{i}=', z_list[i], vList[i], flist[i], vList[i] - flist[i])
print(np.max(any(flist) - any(vList)))

xlist = np.linspace(list_g[0], list_g[-1], N)


def getqList(xlist, sigma, N):
    q_list = []
    f1 = lambda x: x / sigma ** 2 * math.exp(-x ** 2 / (2 * sigma ** 2))
    q_list.append(si.quad(f1, -math.inf, xlist[0])[0])
    for i in range(N - 1):
        q_list.append(si.quad(f1, xlist[i], xlist[i + 1])[0])
    q_list.append(si.quad(f1, xlist[-1], math.inf)[0])
    print(xlist)
    print(q_list, len(q_list))
    return q_list


q_list = getqList(xlist, 1, N)
countList = getCount(xlist, list_g, N)
print(countList)


def Gipoteza(countList, q_list, density, N, alpha):
    sum = 0
    critical = scipy.stats.chi2.ppf(1 - alpha, N - 1)
    for j in range(1, N + 1):
        sum += (countList[j] - density * q_list[j]) ** 2 / (density * q_list[j])
    return sum, critical


print(q_list)
print(countList)
for i in range(5):
    print(Gipoteza(countList, q_list, density, N, 0.05))

'''''
plt.subplot(1, 2, 1)
plt.title('Функция распределения')
plt.plot(list_g, list_r, '-g')

plt.subplot(1, 2, 2)
plt.title('Плотность распределения')
plt.plot(list_x2, list_f, '-r')
for i in range(N):
    plt.plot([delta_list[i], delta_list[i + 1], delta_list[i + 1], delta_list[i], delta_list[i]],
             [vList[i], vList[i], 0, 0, vList[i]], 'b')
    plt.plot([delta_list[i], delta_list[i + 1]], [vList[i], vList[i]], 'b')


#plt.show()
'''''
