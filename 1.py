from matplotlib import pyplot
import numpy

Daedeok = [81, 70, 94, 91, 74, 78, 80, 81, 75, 89, 102, 110]
Donggu = [84, 82, 86, 89, 75, 91, 100, 88, 108, 111, 88, 77]

label = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']

pyplot.rcParams["font.family"] = 'Malgun Gothic'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (12, 8)

pyplot.figure()

x = numpy.arange(len(label))

pyplot.bar(x-0.0, Daedeok, label='대덕구', width=0.2, color='#dd0000')
pyplot.bar(x+0.2, Donggu, label='동구', width=0.2, color='#ddff00')
pyplot.xticks(x, label)

pyplot.legend()
pyplot.xlabel('월')
pyplot.ylabel('교통사고 수')
pyplot.ylim(0, 150)
pyplot.title('2016년 대덕구/동구 월별 교통사고')

pyplot.savefig('ti.png')

pyplot.close()