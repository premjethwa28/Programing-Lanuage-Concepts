# Name - Prem Atul Jethwa
# Student Id - 1001861810
# NetID - paj1810
# Date of submission - 04/20/2023
# OS - Mac
# Language Version - Python 3.6.2

# GOTO functionality is a programming language feature that allows a program to transfer control to a
# different part of the program's code, typically identified by a label or line number.

# In general, the use of GOTO statements is discouraged in modern programming practices because they can
# make code difficult to read, understand, and maintain. Instead, most programming languages provide
# alternative control flow structures, such as loops, conditional statements, and functions, that can be
# used to achieve the same effect in a more structured and maintainable way.

# However, some languages still support GOTO statements as a low-level control mechanism for certain types
# of programming tasks, such as low-level system programming or optimization of performance-critical code.

import random


class Maze:                      # Three class attributes: target, random, and result.
    target = 0
    random = random.seed(0)
    result = []

    def main(args):
        print(" " * 30 + "AMAZING PROGRAM")
        print(" " * 15 + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n\n\n")
        r, c = input(
            "WHAT ARE YOUR WIDTH AND LENGTH (width,length): ").split(',')
        r = int(r)
        c = int(c)
        Maze.spaghetti(r, c)         # Call method spaghetti()
        for i in Maze.result:
            print(i, end="")
        print("OK")

    def clear():
        Maze.result = []

    def println():
        Maze.result.append("\n")

    def print(text):
        Maze.result.append(text)

    def rnd(count):
        return int((count * random.random())) + 1

    def GOTO(line_no):
        Maze.target = line_no  # By setting the Maze.target attribute to a specific line number, the program can "jump" to that line number and continue executing from there

    def spaghetti(horizontal, vertical):
        Maze.clear()
        Maze.println()
        h = horizontal
        v = vertical
        if (h == 1 or v == 1):
            return
        w_Array = [[0] * (v + 1) for _ in range(h + 1)]
        i = 0
        while (i <= h):
            w_Array[i] = [0] * (v + 1)
            i += 1
        v_Array = [[0] * (v + 1) for _ in range(h + 1)]
        i = 0
        while (i <= h):
            v_Array[i] = [0] * (v + 1)
            i += 1
        q = 0
        z = 0
        x = Maze.rnd(h)
        i = 1
        while (i <= h):
            if (i == x):
                Maze.print(".  ")
            else:
                Maze.print(".--")
            i += 1
        Maze.print(".")
        Maze.println()
        c = 1
        w_Array[x][1] = c
        c += 1
        r = x
        s = 1
        Maze.GOTO(270)
        while (Maze.target != -1):
            if (Maze.target == 210):
                if (r != h):
                    Maze.GOTO(250)
                else:
                    Maze.GOTO(220)
                continue
            elif (Maze.target == 220):
                if (s != v):
                    Maze.GOTO(240)
                else:
                    Maze.GOTO(230)
                continue
            elif (Maze.target == 230):
                r = 1
                s = 1
                Maze.GOTO(260)
                continue
            elif (Maze.target == 240):
                r = 1
                s += 1
                Maze.GOTO(260)
                continue
            elif (Maze.target == 250):
                r += 1
                Maze.GOTO(260)
                continue
            elif (Maze.target == 260):
                if (w_Array[r][s] == 0):
                    Maze.GOTO(210)
                else:
                    Maze.GOTO(270)
                continue
            elif (Maze.target == 270):
                if (r - 1 == 0):
                    Maze.GOTO(600)
                else:
                    Maze.GOTO(280)
                continue
            elif (Maze.target == 280):
                if (w_Array[r - 1][s] != 0):
                    Maze.GOTO(600)
                else:
                    Maze.GOTO(290)
                continue
            elif (Maze.target == 290):
                if (s - 1 == 0):
                    Maze.GOTO(430)
                else:
                    Maze.GOTO(300)
                continue
            elif (Maze.target == 300):
                if (w_Array[r][s - 1] != 0):
                    Maze.GOTO(430)
                else:
                    Maze.GOTO(310)
                continue
            elif (Maze.target == 310):
                if (r == h):
                    Maze.GOTO(350)
                else:
                    Maze.GOTO(320)
                continue
            elif (Maze.target == 320):
                if (w_Array[r + 1][s] != 0):
                    Maze.GOTO(350)
                else:
                    Maze.GOTO(330)
                continue
            elif (Maze.target == 330):
                x = Maze.rnd(3)
                Maze.GOTO(340)
                continue
            elif (Maze.target == 340):
                if (x == 1):
                    Maze.GOTO(940)
                elif (x == 2):
                    Maze.GOTO(980)
                elif (x == 3):
                    Maze.GOTO(1020)
                else:
                    Maze.GOTO(350)
                continue
            elif (Maze.target == 350):
                if (s != v):
                    Maze.GOTO(380)
                else:
                    Maze.GOTO(360)
                continue
            elif (Maze.target == 360):
                if (z == 1):
                    Maze.GOTO(410)
                else:
                    Maze.GOTO(370)
                continue
            elif (Maze.target == 370):
                q = 1
                Maze.GOTO(390)
                continue
            elif (Maze.target == 380):
                if (w_Array[r][s + 1] != 0):
                    Maze.GOTO(410)
                else:
                    Maze.GOTO(390)
                continue
            elif (Maze.target == 390):
                x = Maze.rnd(3)
                Maze.GOTO(400)
                continue
            elif (Maze.target == 400):
                if (x == 1):
                    Maze.GOTO(940)
                elif (x == 2):
                    Maze.GOTO(980)
                elif (x == 3):
                    Maze.GOTO(1090)
                else:
                    Maze.GOTO(410)
                continue
            elif (Maze.target == 410):
                x = Maze.rnd(2)
                Maze.GOTO(420)
                continue
            elif (Maze.target == 420):
                if (x == 1):
                    Maze.GOTO(940)
                elif (x == 2):
                    Maze.GOTO(980)
                else:
                    Maze.GOTO(430)
                continue
            elif (Maze.target == 430):
                if (r == h):
                    Maze.GOTO(530)
                else:
                    Maze.GOTO(440)
                continue
            elif (Maze.target == 440):
                if (w_Array[r + 1][s] != 0):
                    Maze.GOTO(530)
                else:
                    Maze.GOTO(450)
                continue
            elif (Maze.target == 450):
                if (s != v):
                    Maze.GOTO(480)
                else:
                    Maze.GOTO(460)
                continue
            elif (Maze.target == 460):
                if (z == 1):
                    Maze.GOTO(510)
                else:
                    Maze.GOTO(470)
                continue
            elif (Maze.target == 470):
                q = 1
                Maze.GOTO(490)
                continue
            elif (Maze.target == 480):
                if (w_Array[r][s + 1] != 0):
                    Maze.GOTO(510)
                else:
                    Maze.GOTO(490)
                continue
            elif (Maze.target == 490):
                x = Maze.rnd(3)
                Maze.GOTO(500)
                continue
            elif (Maze.target == 500):
                if (x == 1):
                    Maze.GOTO(940)
                elif (x == 2):
                    Maze.GOTO(1020)
                elif (x == 3):
                    Maze.GOTO(1090)
                else:
                    Maze.GOTO(510)
                continue
            elif (Maze.target == 510):
                x = Maze.rnd(2)
                Maze.GOTO(520)
                continue
            elif (Maze.target == 520):
                if (x == 1):
                    Maze.GOTO(940)
                elif (x == 2):
                    Maze.GOTO(1020)
                else:
                    Maze.GOTO(530)
                continue
            elif (Maze.target == 530):
                if (s != v):
                    Maze.GOTO(560)
                else:
                    Maze.GOTO(540)
                continue
            elif (Maze.target == 540):
                if (z == 1):
                    Maze.GOTO(590)
                else:
                    Maze.GOTO(550)
                continue
            elif (Maze.target == 550):
                q = 1
                Maze.GOTO(570)
                continue
            elif (Maze.target == 560):
                if (w_Array[r][s + 1] != 0):
                    Maze.GOTO(590)
                else:
                    Maze.GOTO(570)
                continue
            elif (Maze.target == 570):
                x = Maze.rnd(2)
                Maze.GOTO(580)
                continue
            elif (Maze.target == 580):
                if (x == 1):
                    Maze.GOTO(940)
                elif (x == 2):
                    Maze.GOTO(1090)
                else:
                    Maze.GOTO(590)
                continue
            elif (Maze.target == 590):
                Maze.GOTO(940)
                continue
            elif (Maze.target == 600):
                if (s - 1 == 0):
                    Maze.GOTO(790)
                else:
                    Maze.GOTO(610)
                continue
            elif (Maze.target == 610):
                if (w_Array[r][s - 1] != 0):
                    Maze.GOTO(790)
                else:
                    Maze.GOTO(620)
                continue
            elif (Maze.target == 620):
                if (r == h):
                    Maze.GOTO(720)
                else:
                    Maze.GOTO(630)
                continue
            elif (Maze.target == 630):
                if (w_Array[r + 1][s] != 0):
                    Maze.GOTO(720)
                else:
                    Maze.GOTO(640)
                continue
            elif (Maze.target == 640):
                if (s != v):
                    Maze.GOTO(670)
                else:
                    Maze.GOTO(650)
                continue
            elif (Maze.target == 650):
                if (z == 1):
                    Maze.GOTO(700)
                else:
                    Maze.GOTO(660)
                continue
            elif (Maze.target == 660):
                q = 1
                Maze.GOTO(680)
                continue
            elif (Maze.target == 670):
                if (w_Array[r][s + 1] != 0):
                    Maze.GOTO(700)
                else:
                    Maze.GOTO(680)
                continue
            elif (Maze.target == 680):
                x = Maze.rnd(3)
                Maze.GOTO(690)
                continue
            elif (Maze.target == 690):
                if (x == 1):
                    Maze.GOTO(980)
                elif (x == 2):
                    Maze.GOTO(1020)
                elif (x == 3):
                    Maze.GOTO(1090)
                else:
                    Maze.GOTO(700)
                continue
            elif (Maze.target == 700):
                x = Maze.rnd(2)
                Maze.GOTO(710)
                continue
            elif (Maze.target == 710):
                if (x == 1):
                    Maze.GOTO(980)
                elif (x == 2):
                    Maze.GOTO(1020)
                else:
                    Maze.GOTO(720)
                continue
            elif (Maze.target == 720):
                if (s != v):
                    Maze.GOTO(750)
                else:
                    Maze.GOTO(730)
                continue
            elif (Maze.target == 730):
                if (z == 1):
                    Maze.GOTO(780)
                else:
                    Maze.GOTO(740)
                continue
            elif (Maze.target == 740):
                q = 1
                Maze.GOTO(760)
                continue
            elif (Maze.target == 750):
                if (w_Array[r][s + 1] != 0):
                    Maze.GOTO(780)
                else:
                    Maze.GOTO(760)
                continue
            elif (Maze.target == 760):
                x = Maze.rnd(2)
                Maze.GOTO(770)
                continue
            elif (Maze.target == 770):
                if (x == 1):
                    Maze.GOTO(980)
                elif (x == 2):
                    Maze.GOTO(1090)
                else:
                    Maze.GOTO(780)
                continue
            elif (Maze.target == 780):
                Maze.GOTO(980)
                continue
            elif (Maze.target == 790):
                if (r == h):
                    Maze.GOTO(880)
                else:
                    Maze.GOTO(800)
                continue
            elif (Maze.target == 800):
                if (w_Array[r + 1][s] != 0):
                    Maze.GOTO(880)
                else:
                    Maze.GOTO(810)
                continue
            elif (Maze.target == 810):
                if (s != v):
                    Maze.GOTO(840)
                else:
                    Maze.GOTO(820)
                continue
            elif (Maze.target == 820):
                if (z == 1):
                    Maze.GOTO(870)
                else:
                    Maze.GOTO(830)
                continue
            elif (Maze.target == 830):
                q = 1
                Maze.GOTO(990)
                continue
            elif (Maze.target == 840):
                if (w_Array[r][s + 1] != 0):
                    Maze.GOTO(870)
                else:
                    Maze.GOTO(850)
                continue
            elif (Maze.target == 850):
                x = Maze.rnd(2)
                Maze.GOTO(860)
                continue
            elif (Maze.target == 860):
                if (x == 1):
                    Maze.GOTO(1020)
                elif (x == 2):
                    Maze.GOTO(1090)
                else:
                    Maze.GOTO(870)
                continue
            elif (Maze.target == 870):
                Maze.GOTO(1020)
                continue
            elif (Maze.target == 880):
                if (s != v):
                    Maze.GOTO(910)
                else:
                    Maze.GOTO(890)
                continue
            elif (Maze.target == 890):
                if (z == 1):
                    Maze.GOTO(930)
                else:
                    Maze.GOTO(900)
                continue
            elif (Maze.target == 900):
                q = 1
                Maze.GOTO(920)
                continue
            elif (Maze.target == 910):
                if (w_Array[r][s + 1] != 0):
                    Maze.GOTO(930)
                else:
                    Maze.GOTO(920)
                continue
            elif (Maze.target == 920):
                Maze.GOTO(1090)
                continue
            elif (Maze.target == 930):
                Maze.GOTO(1190)
                continue
            elif (Maze.target == 940):
                w_Array[r - 1][s] = c
                Maze.GOTO(950)
                continue
            elif (Maze.target == 950):
                c += 1
                v_Array[r - 1][s] = 2
                r -= 1
                Maze.GOTO(960)
                continue
            elif (Maze.target == 960):
                if (c == h * v + 1):
                    Maze.GOTO(1200)
                else:
                    Maze.GOTO(970)
                continue
            elif (Maze.target == 970):
                q = 0
                Maze.GOTO(270)
                continue
            elif (Maze.target == 980):
                w_Array[r][s - 1] = c
                Maze.GOTO(990)
                continue
            elif (Maze.target == 990):
                c += 1
                Maze.GOTO(1000)
                continue
            elif (Maze.target == 1000):
                v_Array[r][s - 1] = 1
                s -= 1
                if (c == h * v + 1):
                    Maze.GOTO(1200)
                else:
                    Maze.GOTO(1010)
                continue
            elif (Maze.target == 1010):
                q = 0
                Maze.GOTO(270)
                continue
            elif (Maze.target == 1020):
                w_Array[r + 1][s] = c
                Maze.GOTO(1030)
                continue
            elif (Maze.target == 1030):
                c += 1
                if (v_Array[r][s] == 0):
                    Maze.GOTO(1050)
                else:
                    Maze.GOTO(1040)
                continue
            elif (Maze.target == 1040):
                v_Array[r][s] = 3
                Maze.GOTO(1060)
                continue
            elif (Maze.target == 1050):
                v_Array[r][s] = 2
                Maze.GOTO(1060)
                continue
            elif (Maze.target == 1060):
                r += 1
                Maze.GOTO(1070)
                continue
            elif (Maze.target == 1070):
                if (c == h * v + 1):
                    Maze.GOTO(1200)
                else:
                    Maze.GOTO(1080)
                continue
            elif (Maze.target == 1080):
                Maze.GOTO(600)
                continue
            elif (Maze.target == 1090):
                if (q == 1):
                    Maze.GOTO(1150)
                else:
                    Maze.GOTO(1100)
                continue
            elif (Maze.target == 1100):
                w_Array[r][s + 1] = c
                c += 1
                if (v_Array[r][s] == 0):
                    Maze.GOTO(1120)
                else:
                    Maze.GOTO(1110)
                continue
            elif (Maze.target == 1110):
                v_Array[r][s] = 3
                Maze.GOTO(1130)
                continue
            elif (Maze.target == 1120):
                v_Array[r][s] = 1
                Maze.GOTO(1130)
                continue
            elif (Maze.target == 1130):
                s += 1
                if (c == v * h + 1):
                    Maze.GOTO(1200)
                else:
                    Maze.GOTO(1140)
                continue
            elif (Maze.target == 1140):
                Maze.GOTO(270)
                continue
            elif (Maze.target == 1150):
                z = 1
                Maze.GOTO(1160)
                continue
            elif (Maze.target == 1160):
                if (v_Array[r][s] == 0):
                    Maze.GOTO(1180)
                else:
                    Maze.GOTO(1170)
                continue
            elif (Maze.target == 1170):
                v_Array[r][s] = 3
                q = 0
                Maze.GOTO(1190)
                continue
            elif (Maze.target == 1180):
                v_Array[r][s] = 1
                q = 0
                r = 1
                s = 1
                Maze.GOTO(260)
                continue
            elif (Maze.target == 1190):
                Maze.GOTO(210)
                continue
            elif (Maze.target == 1200):
                Maze.target = -1
                continue
        k = 1
        while (k <= v):
            Maze.print("|")
            i = 1
            while (i <= h):
                if (v_Array[i][k] >= 2):
                    Maze.print("   ")
                else:
                    Maze.print("  |")
                i += 1
            Maze.print(" ")
            Maze.println()
            i = 1
            while (i <= h):
                if (v_Array[i][k] == 0):
                    Maze.print(".--")
                elif (v_Array[i][k] == 2):
                    Maze.print(".--")
                else:
                    Maze.print(".  ")
                i += 1
            Maze.print(".")
            Maze.println()
            k += 1


if __name__ == "__main__":
    Maze.main([])
