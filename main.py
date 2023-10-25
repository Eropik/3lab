ch=int(input("Меню для 3 лабораторной\n Выберите задачу(0 exit): "))
match ch:
    case 1:
        file = open("y.txt", "r")
        lines_f = file.readlines()
        file.close()
        print(lines_f)
        b = 0
        strt = ""
        for i in lines_f:
            ind = lines_f[b].split()
            if int(ind[2]) < 15:
                b = 0
                for t in ind:
                    strt += (ind[b] + " ")
                    b += 1
            b += 1
        print(strt)
    case 2:
        file1 = open("F1.txt", "w")
        while (True):
            strt = str(input("enter F1: "))
            if strt != " ":
                file1.write(strt + "\n")
                if strt[0].isdigit():
                    file2 = open("F2.txt", "a")
                    file2.write(strt + "\n")
                    file2.close()
            else:
                break
        file1.close()

    case 3:
        def list_sum(lst):
            sum = 0
            for i in lst:
                sum += i
            return sum

        def normal_list(lst):
            for i in range(len(lst)):
                lst[i] = lst[i].replace("\n", '')
                lst[i] = lst[i].replace("lab", '')
                lst[i] = lst[i].replace("lk", '')
                lst[i] = lst[i].replace("pr", '')
                lst[i] = lst[i].split(':')
                lst[i][1] = list_sum(list(map(int, lst[i][1].split())))
            return dict(lst)


        file_obj = open("Subj.txt", "r+")
        subjects = file_obj.readlines()
        file_obj.close()
        print(normal_list(subjects))

    case 4:
        import json
        def revenue(lst):
            return lst[0] - lst[1]

        def average(lst):
            aver = 0
            for i in lst:
                aver += i[1]
            return aver / len(lst)

        def normal_lst(lst):
            for i in range(len(lst)):
                lst[i] = lst[i].replace("\n", '')
                lst[i] = lst[i].split("OOO")
                lst[i][1] = revenue(list(map(int, lst[i][1].split())))
            return lst


        file_obj = open("Firm.txt", "r+")
        firms = file_obj.readlines()
        file_obj.close()
        norm = normal_lst(firms)

        unprofit = []
        for i in range(len(norm)):
            if norm[i][1] < 0:
                copy = norm[i].copy()
                unprofit.append(copy)
                norm[i][1] = 0
        average = {"averaga:": average(norm)}
        print(average)
        unprofit = dict(unprofit)
        norm = dict(norm)
        final = (norm, unprofit, average)
        print(final)
        json_obj = json.dumps(final)
        with open("data.json", "w") as out:
            json.dump(final, out)
    case 0:
        print("bye")