# B. Minifikatsiyada avtomatik toʻldirish
# Vaqt chegarasi	2 soniyalar
# Xotirani cheklash	256.0 MB
# Kirish	stdin yoki input.txt
# Xulosa	stdout yoki output.txt
# Kichik inglizcha harflardan tuzilgan
# N ta turli xil soʻzdan iborat lugʻat berilgan.

# Sizga 
# Q soʻrovlari keladi, shundan 
# i-soʻrov kichik inglizcha harflar va 
                          
# k 
# i
#   sonidan iborat 
# p 
# i

#   satridan tuzilgan. 
# i-soʻrovga javoban, 
# p 
# i
# ​
#   prefiksli soʻzlar orasida lugʻatdan leksikografik tartibdagi 
# k 
# i
# ​
#  -soʻzni chiqarishingiz zarur.

# Kirish formati
# Birinchi kiritish satrida 
# N va 
# Q (
# 1≤N≤3⋅10 
# 5
#  ,1≤Q≤5⋅10 
# 3
#  ) sonlari – lugʻat hajmi va soʻrovlar soni joylashgan.

# Keyingi 
# N ta satrdan 
# i-satrda kichik inglizcha harflardan iborat yagona satr 
# w 
# i
# ​
#   (
# 1≤∣w 
# i
# ​
#  ∣≤2⋅10 
# 6
#  ) – lugʻatning 
# i-soʻzi joylashgan.

# Quyidagilar kafolatlanadi: - lugʻatdan olinadigan soʻzlarning jami uzunligi 
# 2⋅10 
# 6
#   dan oshmaydi - soʻz leksikografik tartibda saralangan - lugʻatdagi soʻzlar har xil

# Keyingi 
# Q ta satrda soʻrovlar berilgan. Har bir soʻrov
# k 
# i
# ​
#   (
# 1≤k 
# i
# ​
#  ≤10 
# 9
#  ) butun soni bilan va kichik inglizcha harflardan (
# 1≤∣p 
# i
# ​
#  ∣≤10 
# 3
#  ) iborat 
# p 
# i
# ​
#   satri bilan taʼriflanadi.

# Chiqish formati
# Q ta satr chiqaring, ulardan 
# i-satr 
# i-soʻrovga javobni oʻz ichiga olishi kerak. Mos satr mavjud boʻlsa, unda uning lugʻatdagi tartib raqamini chiqaring. Yoki − 
# −1 chiqaring.

# Misol
# Kirish	Xulosa
# 10 3
# aa
# aaa
# aab
# ab
# abc
# ac
# ba
# daa
# dab
# dadba
# 4 a
# 2 da
# 4 da
# 4
# 9
# -1
# Izohlar
# Leksikografik tartib.

# Leksikografik tartib – bu lugʻatda soʻzlarning keltirilish tartibi.

# Rasmiy tavsifi: agar 
# p 
# i
# ​
#  <q 
# i
# ​
#   boʻlgan 
# i pozitsiyasi mavjud boʻlsa va barcha 
# j<i uchun 
# p 
# j
# ​
#  =q 
# j
# ​
#   bajarilgan boʻlsa, unda 
# p satri leksikografik jihatdan 
# q satridan kichik boʻladi. Agar bunday pozitsiya 
# i mavjud boʻlmasa, 
# p uzunligi 
# q uzunligidan kichik boʻlganda, 
# p leksikografik jihatdan 
# q dan kichik boʻladi. Masalan, 
# abdc<abe и 
# abc<abcd.

# Misolda berilgan soʻrovlarni koʻrib chiqamiz:

# a prefiksli soʻzlar — bu {
# aa,aaa,aab,ab,abc,ac}. Ulardan 4-soʻz — 
# ab. U lugʻatda 
# 4 raqamiga ega.
# da prefiksli soʻzlar — bu {
# daa,dab,dadba}. Ulardan 2-soʻz — 
# dab. U lugʻatda 
# 9 raqamiga ega.
# da prefiksli soʻzlar — bu {
# daa,dab,dadba}. Ular hammasi boʻlib 3 ta, shuning uchun bu soʻrovga javob 
# −1 sonidir.
# Vazifa shartlarini yuklab olish






import sys
from bisect import bisect_left

def main():
    input = sys.stdin.read
    data = input().splitlines()

    N, Q = map(int, data[0].split())
    words = data[1:N + 1]  

    res = []

    for i in range(N + 1, N + Q + 1):
        k, prefix = data[i].split()
        k = int(k)

        start_ind = bisect_left(words, prefix)
        end_ind = bisect_left(words, prefix + '{') 

        count = end_ind - start_ind
        
        if count >= k:
            res.append(str(start_ind + k - 1 + 1))  
        else:
            res.append("-1")

    sys.stdout.write("\n".join(res) + "\n")

if __name__ == "__main__":
    main()
