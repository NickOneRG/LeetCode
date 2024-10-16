"""
A. Matnni formatlash
Vaqt chegarasi	1 ikkinchi
Xotirani cheklash	256.0 MB
Kirish	stdin yoki input.txt
Xulosa	stdout yoki output.txt
Unexpected text node: '
                            
                        '
C++ tilidan foydalansangiz, unda kirish ma'lumotlarini hisoblash uchun bu vazifada sizga 
Unexpected text node: '
                            
                        '
std::getline funksiyasi kerak bo'lishi mumkin. Bu haqida batafsil bu yerda o'qishingiz mumkin Kichik inglizcha harflar, oraliqlar va vergullardan iborat matn berilgan. 
Unexpected text node: '
                            
                        '
len matnda 
Unexpected text node: '
                            
                        '
3 ga ko'paytirilgan maksimal so'z uzunligiga teng bo'lsin. Matnni quyidagicha formatlashingiz zarur:

har bir satrda belgilar 
Unexpected text node: '
                                
                            '
len tadan ko'p bo'lmasligi kerak
vergul so'z oldidan unga “yopishadi”, ya'ni u so'z bilan bitta satrda bo'lishi kerak
vergul oldidan oraliq qoldirilmaydi
vergul satrning oxirgi belgisi hisoblanmasa, undan keyin oraliq qo'yiladi
agar so'z 
Unexpected text node: '
                                
                            '
i satriga kirmasa, 
Unexpected text node: '
                                
                            '
i satri tugaydi, so'z esa 
Unexpected text node: '
                                
                            '
(i+1) satrida yoziladi
har qanday satrda oxirgi belgi harf yoki vergul bo'lishi kerak
Kirish formati
Yagona kiritish satrida kichik inglizcha harflar, vergullar va oraliqlardan iborat 
Unexpected text node: '
                            
                        '
w (
Unexpected text node: '
                            
                        '
1≤∣w∣≤10 
5
 ) satri joylashgan.

Quyidagilar kafolatlanadi:

har qanday ikkita vergul orasidagi matnda bo'sh bo'lmagan so'z bor
matn harfdan boshlanadi
matnda ketma-ket kelgan ikkita oraliq yo'q
Chiqish formati
Vazifa shartlariga muvofiq formatlangan matn chiqaring.

Misol 1
Kirish	Xulosa
once upon a time, in a land far far away lived a princess , whose beauty was yet unmatched

once upon a time, in a land
far far away lived a
princess, whose beauty was
yet unmatched

Misol 2
Kirish	Xulosa
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex

a, b, c, d, e, f,
g, h, i, j, k, l,
m, n, o, p, yandex

Izohlar
Birinchi misolda eng uzun so'z «unmatched» hisoblanadi, shuning uchun 
Unexpected text node: '
                            
                        '
len=9 va formatlangan matnning har bir satrida 
Unexpected text node: '
                            
                        '
27 dan ortiq belgi bo'lmasligi kerak. Birinchi vergul «time» so'ziga, ikkinchisi – «princess» so'ziga tegishli, shuning uchun formatlangan matnda bu vergullar tegishli so'zlar tugashi bilan qo'yiladi. Vergullardan keyin bittadan oraliq qoldirilgan.

Ikkinchi misolda eng uzun so'z – «yandex», shuning uchun 
Unexpected text node: '
                            
                        '
len=6. Formatlangan matnning har bir satrida belgilar 18 dan ko'p bo'lmasligi kerak. Formatlangan matnning birinchi satri 
Unexpected text node: '
                              '
17 belgilarini o'z ichiga oladi, chunki, unga keyingi so'zni joylashtirish uchun 3 ta belgi qo'shish zarur: oraliq, «g» va «,».
"""




class Solution:
    def str_formating(self, sentence: str) -> str:
        sentence = sentence.replace(',', ', ')
        words = sentence.split()
        len_limit = max(len(word.strip(',')) for word in words) * 3

        format_text, curr_line = [], []
        curr_len = 0

        for word in words:
            if curr_len + len(word) + len(curr_line) > len_limit:
                format_text.append(' '.join(curr_line))
                curr_line = [word]
                curr_len = len(word)
            else:
                curr_line.append(word)
                curr_len += len(word)

        if curr_line:
            format_text.append(' '.join(curr_line))

        for i in range(len(format_text)):
            format_text[i] = format_text[i].replace(' ,', ',')

        return "\n".join(format_text)


# Example usage:
m = Solution()
print(m.str_formating("once upon a time, in a land far far away lived a princess, whose beauty was yet unmatched"))
print(m.str_formating("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex"))
