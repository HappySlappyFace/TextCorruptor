from random import *

inputText = input("enter your string: ")
inputPerc = int(input("give your Percentage: "))
alphabetArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                 "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

uppercaseArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
lowecaseArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                 "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

Cursed1 = ['₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'ł', 'J', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Q', 'Ɽ', '₴', '₮', 'Ʉ',
           'V', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '卂', '乃', '匚', 'ᗪ', '乇', '千', 'Ꮆ', '卄', '丨', 'ﾌ', 'Ҝ', 'ㄥ', '爪', '几', 'ㄖ',
           '卩', 'Ɋ', '尺', '丂', 'ㄒ', 'ㄩ', 'ᐯ', '山', '乂', 'ㄚ', '乙']
Cursed2 = ['𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺', '𝕻', '𝕼',
           '𝕽', '𝕾', '𝕿', '𝖀', '𝖁', '𝖂', '𝖃', '𝖄', '𝖅', '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃',
           '𝕄', 'ℕ', '𝕆', 'ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕍', '𝕎', '𝕏', '𝕐', 'ℤ']

ch1 = ""


def curseify(x):
    if inputText[i] in uppercaseArray:
        x = ord(x)-65
        e = getrandbits(1)
        if e == 1:
            x = Cursed1[x+26]
            return x
        else:
            x = Cursed1[x]
            return x

    elif inputText[i] in lowecaseArray:
        x = ord(x)-97
        e = getrandbits(1)
        if e == 1:
            x = Cursed2[x+26]
            return x
        else:
            x = Cursed2[x]
            return x


for i in range(len(inputText)):
    aux = randrange(0, 99)
    if inputText[i] in alphabetArray:
        if aux < inputPerc:
            t = curseify(inputText[i])
            ch1 = ch1 + t
        else:
            ch1 = ch1 + inputText[i]
    else:
        ch1 = ch1 + inputText[i]
print(ch1)