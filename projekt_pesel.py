import random
import linecache
import time


class Pesel:
    ordinal_number = 0
    n = 1
    wage = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    pesel_tab = []
    i = 0
    years = []
    months = []
    days = []
    ordinal_num_tab = []

    def get_birth_year(self):
        global birth_year
        while True:
            try:
                birth_year = int(linecache.getline('dane_wejściowe.txt', Pesel.i))
                print("Rok urodzenia:", birth_year)
                time.sleep(0.5)
                if 1900 < birth_year < 2299:
                    break
                else:
                    print("Rok musi być liczbą z przedziału 1900 - 2299, wciśnij p jeśli chcesz podać ponownie rok, lub wciśnij inny klawisz jeśli chcesz zakończyć")
                    Pesel.i += 1
                    n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
                    print(n)
                    if n == "p":
                        Pesel.i += 1
                        continue
                    else:
                        Pesel.want(self)
            except (ValueError, Exception):
                print("Podałeś złą formę roku, wciśnij p jeśli chcesz podać ponownie rok, lub wciśnij inny klawisz jeśli chcesz zakończyć")
                Pesel.i += 1
                n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
                print(n)
                if n == "p":
                    Pesel.i += 1
                    continue
                else:
                    Pesel.want(self)
        return birth_year

    def get_birth_month(self):
        global birth_month
        while True:
            try:
                Pesel.i += 1
                birth_month = int(linecache.getline('dane_wejściowe.txt', Pesel.i))
                print("Miesiąc urodzenia: " + str(birth_month))
                time.sleep(0.5)
                if 1 <= birth_month <= 12:
                    break
                else:
                    print("Miesiąc powinien być liczbą z przedziału 1-12, wciśnij p jeśli chcesz podać ponownie miesiąc, lub wciśnij inny klawisz jeśli chcesz zakończyć")
                    Pesel.i += 1
                    n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
                    print(n)
                    if n == "p":
                        continue
                    else:
                        Pesel.want(self)
            except (ValueError, Exception):
                print("Podałeś złą formę miesiąca, wciśnij p jeśli chcesz podać ponownie miesiąc, lub wciśnij inny klawisz jeśli chcesz zakończyć")
                Pesel.i += 1
                n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
                print(n)
                if n == "p":
                    continue
                else:
                    Pesel.want(self)
        return birth_month

    @staticmethod
    def set_month(birth_year, birth_month):
        month = birth_month
        if 2000 <= birth_year <= 2099:
            month += 20
        elif 2100 <= birth_year <= 2199:
            month += 40
        elif 2200 <= birth_year <= 2299:
            month += 60
        return month

    def get_birth_day(self, birth_month, birth_year):
        one_month = [1, 3, 5, 7, 8, 10, 12]
        second_month = [4, 6, 9, 11]
        while True:
            Pesel.i += 1
            birth_day = int(linecache.getline('dane_wejściowe.txt', Pesel.i))
            print("Dzień urodzenia:", birth_day)
            time.sleep(0.5)
            if birth_month in one_month:
                if 0 < birth_day <= 31:
                    break
                else:
                    print("Podałeś zły numer, wciśnij p jeśli chcesz podać ponownie numer dnia, lub wciśnij inny klawisz jeśli chcesz zakończyć")
                    Pesel.i += 1
                    n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
                    print(n)
                    if n == "p":
                        continue
                    else:
                        Pesel.want(self)
            elif birth_month in second_month:
                if 0 < birth_day <= 30:
                    break
                else:
                    print("Podałeś zły numer, wciśnij p jeśli chcesz podać ponownie numer dnia, lub wciśnij inny klawisz jeśli chcesz zakończyć")
                    Pesel.i += 1
                    n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
                    print(n)
                    if n == "p":
                        continue
                    else:
                        Pesel.want(self)
            else:
                if birth_month == 2:
                    if birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0):  # leap year
                        if 0 < birth_day <= 29:
                            break
                        else:
                            print("Podałeś zły numer, wciśnij p jeśli chcesz podać ponownie numer dnia, lub wciśnij inny klawisz jeśli chcesz zakończyć")
                            Pesel.i += 1
                            n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
                            print(n)
                            if n == "p":
                                continue
                            else:
                                Pesel.want(self)
                    else:
                        if 0 < birth_day <= 28:
                            break
                        else:
                            print("Podałeś zły numer, wciśnij p jeśli chcesz podać ponownie numer dnia, lub wciśnij inny klawisz jeśli chcesz zakończyć")
                            Pesel.i += 1
                            n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
                            print(n)
                            if n == "p":
                                continue
                            else:
                                Pesel.want(self)
        return birth_day

    def get_sex(self):
        while True:
            Pesel.i += 1
            sex = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
            time.sleep(0.5)
            if sex == "k":
                print("Płeć: kobieta")
                break
            elif sex == "m":
                print("Płeć: mężczyzna")
                break
            else:
                print("Płeć:", sex)
                print("Podałeś niepoprawną formę płci, wciśnij p jeśli chcesz podać ponownie płeć, lub wciśnij inny klawisz jeśli chcesz zakończyć")
                Pesel.i += 1
                n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
                print(n)
                if n == "p":
                    continue
                else:
                    Pesel.want(self)
        return sex

    def verification(self, birth_year, birth_day, birth_month, month, sex):
        Pesel.i += 1
        n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
        print("Czy chcesz dokonać wpisu " + str(birth_year) + ", " + str(birth_month) + ", " + str(birth_day) + ", " + sex +"? Klawisz t - tak, pozostałe - nie:", n)
        time.sleep(0.5)
        if n != "t":
            Pesel.want(self)
        else:
            Pesel.pesel(self, birth_year, month, birth_day, sex)
            Pesel.want(self)

    def want(self):
        Pesel.i += 1
        n = linecache.getline('dane_wejściowe.txt', Pesel.i).strip()
        print("Czy chcesz dokonac kolejnego wpisu? Klawisz t - tak, pozostałe - nie:", n ,"\n")
        time.sleep(0.5)
        if n == "t":
            Pesel.main(self)

    def pesel(self, birth_year, month, birth_day, sex):
        temp_pesel = []

        Pesel.years.append(birth_year)
        Pesel.months.append(month)
        Pesel.days.append(birth_day)
        Pesel.ordinal_num_tab.append(Pesel.ordinal_number)
        temp_pesel.append((birth_year % 100)//10)
        temp_pesel.append((birth_year % 100)%10)
        temp_pesel.append(month // 10)
        temp_pesel.append(month % 10)
        temp_pesel.append(birth_day // 10)
        temp_pesel.append(birth_day % 10)
        temp_pesel.append(Pesel.ordinal_number // 100)
        temp_pesel.append(Pesel.ordinal_number // 10)
        temp_pesel.append(Pesel.ordinal_number % 10)
        Pesel.ordinal_number += 1
        if sex == "k":
            num_sex = random.randrange(0, 9, 2)
        else:
            num_sex = random.randrange(1, 9, 2)
        temp_pesel.append(num_sex)
        while True:
            sum = 0
            for i in range(0, 10):
                res = Pesel.wage[i] * temp_pesel[i]
                sum += res
            control_num = 10 - (sum % 10)
            if control_num == 10:
                Pesel.pesel(self, birth_year, month, birth_day, sex)
            else:
                break
        temp_pesel.append(control_num)
        temp_pesel_str = "".join(map(str, temp_pesel))
        Pesel.pesel_tab.append(temp_pesel)
        print("Wygenerowany pesel: ", temp_pesel_str)
        return Pesel.pesel_tab, Pesel.years, Pesel.months, Pesel.days, Pesel.ordinal_num_tab

    @staticmethod
    def change(j, pesel_tab, years, months, days, ordinal_num_tab):
        temp = pesel_tab[j]
        pesel_tab[j] = pesel_tab[j + 1]
        pesel_tab[j + 1] = temp
        temp = years[j]
        years[j] = years[j + 1]
        years[j + 1] = temp
        temp = months[j]
        months[j] = months[j + 1]
        months[j + 1] = temp
        temp = days[j]
        days[j] = days[j + 1]
        days[j + 1] = temp
        temp = ordinal_num_tab[j]
        ordinal_num_tab[j] = ordinal_num_tab[j + 1]
        ordinal_num_tab[j + 1] = temp
        return pesel_tab, years, months, days, ordinal_num_tab

    @staticmethod
    def sort(pesel_tab, years, months, days, ordinal_num_tab):
        length = len(pesel_tab)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if years[j] < years[j+1]:
                    continue
                elif years[j] > years[j+1]:
                    Pesel.change(j, pesel_tab, years, months, days, ordinal_num_tab)
                else:
                    if months[j] < months[j+1]:
                        continue
                    elif months[j] < months[j+1]:
                        Pesel.change(j, pesel_tab, years, months, days, ordinal_num_tab)
                    else:
                        if days[j] < days[j+1]:
                            continue
                        elif days[j] > days[j+1]:
                            Pesel.change(j, pesel_tab, years, months, days, ordinal_num_tab)
                        else:
                            if ordinal_num_tab[j] < ordinal_num_tab[j+1]:
                                continue
                            else:
                                Pesel.change(j, pesel_tab, years, months, days, ordinal_num_tab)
        pesel_tab_str = []
        for i in pesel_tab:
            pesel_str = "".join(map(str, i))
            pesel_tab_str.append(pesel_str)
        return pesel_tab_str

    def write_into_file(self, pesel_tab_str):
        filepath = 'pesele.txt'
        try:
            with open(filepath, 'w+') as f:
                f.write("Wygenerowane pesele posortowane od najstarszego do najmłodszego:\n")
                for item in pesel_tab_str:
                    f.write("%s\n" % item)
                print("Pesele zostały pomyślnie zapisane w pliku " + filepath)
        except IOError:
            print("Podany plik nie istnieje!")
        finally:
            f.close()


    def main(self):
        global plik
        try:
            plik = open('dane_wejściowe.txt', "r")
            Pesel.i += 1
            birth_year = self.get_birth_year()
            birth_month = self.get_birth_month()
            month = self.set_month(birth_year, birth_month)
            birth_day = self.get_birth_day(birth_month, birth_year)
            sex = self.get_sex()
            self.verification(birth_year, birth_day, birth_month, month, sex)
        except IOError:
            print("Podany plik nie istnieje!")
        finally:
            plik.close()
        return Pesel.pesel_tab

pesel1 = Pesel()
pesel1.main()
pesel1.write_into_file(pesel1.sort(pesel1.pesel_tab, pesel1.years, pesel1.months, pesel1.days, pesel1.ordinal_num_tab))
input()