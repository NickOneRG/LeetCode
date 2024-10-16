"""
A. Matnni formatlash
Vaqt chegarasi	1 ikkinchi
Xotirani cheklash	256.0 MB
Kirish	stdin yoki input.txt
Xulosa	stdout yoki output.txt
C++ tilidan foydalansangiz, unda kirish ma'lumotlarini hisoblash uchun bu vazifada sizga 
std::getline funksiyasi kerak bo'lishi mumkin. Bu haqida batafsil bu yerda o'qishingiz mumkin Kichik inglizcha harflar, oraliqlar va vergullardan iborat matn berilgan. 
len matnda 
3 ga ko'paytirilgan maksimal so'z uzunligiga teng bo'lsin. Matnni quyidagicha formatlashingiz zarur:

har bir satrda belgilar 
len tadan ko'p bo'lmasligi kerak
vergul so'z oldidan unga “yopishadi”, ya'ni u so'z bilan bitta satrda bo'lishi kerak
vergul oldidan oraliq qoldirilmaydi
vergul satrning oxirgi belgisi hisoblanmasa, undan keyin oraliq qo'yiladi
agar so'z 
i satriga kirmasa, 
i satri tugaydi, so'z esa 
(i+1) satrida yoziladi
har qanday satrda oxirgi belgi harf yoki vergul bo'lishi kerak
Kirish formati
Yagona kiritish satrida kichik inglizcha harflar, vergullar va oraliqlardan iborat 
w (
1≤w≤10 
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
len=9 va formatlangan matnning har bir satrida 
27 dan ortiq belgi bo'lmasligi kerak. Birinchi vergul «time» so'ziga, ikkinchisi  «princess» so'ziga tegishli, shuning uchun formatlangan matnda bu vergullar tegishli so'zlar tugashi bilan qo'yiladi. Vergullardan keyin bittadan oraliq qoldirilgan.

Ikkinchi misolda eng uzun so'z  «yandex», shuning uchun 
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


if __name__ == '__main__':
    # Example usage:
    m = Solution()
    print(m.str_formating(input()))
    # print(m.str_formating("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex "))
    for i in m.str_formating("a , b, c d,e,f  ,g,h,i,j,k,l,m,n,o,p , yandex , ").split("\n"):
        print(i+"|")




def format_text(input_text):
    # Split the text into words while preserving commas
    words = []
    current_word = []
    
    for char in input_text:
        if char in [' ', ',']:
            if current_word:
                words.append(''.join(current_word))
                current_word = []
            if char == ',':
                words.append(',')
        else:
            current_word.append(char)
    
    if current_word:
        words.append(''.join(current_word))
    
    max_length = max(len(word) for word in words if word != ',') * 3
    
    result = []
    current_line = []
    current_length = 0
    
    for word in words:
        if word == ',':
            if current_line:
                current_line[-1] += ','
                current_length += 1 
        else:
            if current_length + len(word) + (1 if current_length > 0 else 0) > max_length:
                result.append(' '.join(current_line))
                current_line = [word] 
                current_length = len(word)
            else:
                if current_length > 0:
                    current_line.append(' ') 
                    current_length += 1 
                current_line.append(word)
                current_length += len(word)

    
    if current_line:
        result.append(''.join(current_line))
    
    return '\n'.join(result)

# input_text = input().strip()
input_text = "once upon a time, in a land far far away lived a princess , whose beauty was yet unmatched"
formatted_text = format_text(input_text)
print(formatted_text)
