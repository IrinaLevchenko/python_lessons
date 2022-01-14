from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается на {TrafficLight.__color[i]}!')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(10)
            i += 1
        # TODO: реализовать проверку порядка режимов


t = TrafficLight()
t.running()
