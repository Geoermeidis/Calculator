import re
import math

k = 0
h = 0
answer = "c"
while answer == "c":
    op = input("Enter a sequence: ")
    seq = re.findall("\d+|[+*-/^=()]|sin|cos|cot|tan|e|pi|tau", op)
    print(seq)
    if seq[len(seq) - 1] != "=":
        seq.append("=")
        op = op + "="


    def tri(se):  # seq = se , module that transforms degrees to radians
        se[i + 1] = math.radians(float(se[i + 1]))



    def mod(se, m, m1):  # seq=se,  j=m,  n1=m1 module that deletes the 3 calculated elements and provides the result
        del se[m - 1]
        del se[m - 1]
        del se[m - 1]
        se.insert(m - 1, m1)
        m = 0

    p = op.count("(")  # Parenthesis count

    i = 0
    while i < len(seq):
        if seq[i] == "e":  # Euler constant
            seq[i] = math.e
        elif seq[i] == "pi":  # Pi constant
            seq[i] = math.pi
        elif seq[i] == "tau":  # Tau constant
            seq[i] = math.tau
        elif seq[i] == "sin":  # ΗΜΙΤΟΝΟ
            tri(seq)
            seq[i] = math.sin(float(seq[i + 1]))
            del seq[i + 1]
        elif seq[i] == "cos":  # ΣΥΝΙΜΗΤΟΝΟ
            tri(seq)
            seq[i] = math.cos(float(seq[i + 1]))
            del seq[i + 1]
        elif seq[i] == "tan":  # ΕΦΑΠΤΟΜΕΝΗ
            tri(seq)
            seq[i] = math.tan(float(seq[i + 1]))
            del seq[i + 1]
        elif seq[i] == "cot":  # ΣΥΝΕΦΑΠΤΟΜΕΝΗ
            tri(seq)
            seq[i] = 1 / math.tan(float(seq[i + 1]))
            del seq[i + 1]
        i += 1

    if p != 0:
        for j in range(0, p):
            n = len(seq)
            for i in range(0, n - 1):
                if seq[i] == "(":  # ΑΡΧΗ ΠΑΡΕΝΘΕΣΗΣ
                    k = i
                if seq[i] == ")":
                    h = i  # ΤΕΛΟΣ
                    break
            for i in range(k + 1, h - 1):  # ΠΡΑΞΕΙΣ ΠΑΡΕΝΘΕΣΗΣ
                if seq[i] == "^":  # ΔΥΝΑΜΗ
                    n1 = float(seq[i - 1]) ** float(seq[i + 1])
                    mod(seq, i, n1)
                    h -= 2
            n = h
            i = k + 1
            while i <= n - 1:
                if seq[i] == "*":  # ΠΟΛΛΑΠΛΑΣΙΑΣΜΟΣ
                    n1 = float(seq[i - 1]) * float(seq[i + 1])
                    mod(seq, i, n1)
                    n -= 2
                    i = k + 1
                    print(seq)
                elif seq[i] == "/":  # ΔΙΑΙΡΕΣΗ
                    try:
                        n1 = float(seq[i - 1]) / float(seq[i + 1])
                        mod(seq, i, n1)
                        n -= 2
                        i = k + 1
                        print(seq)
                    except ZeroDivisionError:  # ΔΙΑΙΡΕΣΗ ΜΕ ΜΗΔΕΝ
                        print("Error due to zero division")
                        quit()
                i += 1
            i = k + 1
            while i <= n - 1:
                if seq[i] == "+":  # ΠΡΟΣΘΕΣΗ
                    n1 = float(seq[i - 1]) + float(seq[i + 1])
                    mod(seq, i, n1)
                    n -= 2
                if seq[i] == "-":  # ΑΦΑΙΡΕΣΗ
                    n1 = float(seq[i - 1]) - float(seq[i + 1])
                    mod(seq, i, n1)
                    n -= 2
                i += 1
            seq.remove("(")
            seq.remove(")")
            print(seq)

    n = len(seq)  # Length of the list 'sequence(seq)'
    j = 0
    while j <= n - 1:
        if seq[j] == "^":  # ΔΥΝΑΜΗ
            n1 = float(seq[j - 1]) ** float(seq[j + 1])
            mod(seq, j, n1)
        else:
            j += 1
        n = len(seq)
        print(seq)


    j = 0
    while j <= n - 1:
        if seq[j] == "*":  # ΠΟΛ/ΜΟΣ
            n1 = float(seq[j - 1]) * float(seq[j + 1])
            mod(seq, j, n1)
        elif seq[j] == "/":  # ΔΙΑΙΡΕΣΗ
            try:
                n1 = float(seq[j - 1]) / float(seq[j + 1])
                mod(seq, j, n1)
            except ZeroDivisionError:
                print("Error due to zero division")
                quit()
        else:
            j += 1
        n = len(seq)
        print(seq)

    su = float(seq[0])
    i = 1
    while seq[i] != "=":
        if seq[i] == "+":  # ΠΡΟΣΘΕΣΗ
            su = su + float(seq[i + 1])
        if seq[i] == "-":  # ΑΦΑΙΡΕΣΗ
            su = su - float(seq[i + 1])
        i += 2
    print(op, su)
    answer = (input("Press [q] to quit or [c] to continue: "))
