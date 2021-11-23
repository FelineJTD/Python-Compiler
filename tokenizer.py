import re

def tokenizer(texts):
    # buka dulu txtnya
    # buat dulu regex special case
    special_cases = [r'\=', r'\+', r'\-', r'\*', r'/', r'\%', '(', ')', '[', ']'
                     , '{', '}', r'\#', r'\>', r'\<', r'\>\=', r'\<\=', r'\=\=', r'\!\='
                     , r'\`\`\`', ':', '\n', '"',",",".", r'\*\*',"'","#", "=="]
    # Buat spasi dan tempWord
    spasi = " "
    tempWord = ""
    # ntar tokenized nyimpen hasil akhir
    tokenized = []
    for i in range(len(texts)):
        # selama dia bukan spasi, concat ke tempWord
        if texts[i] != spasi:
            tempWord += texts[i]
        # Cek klo setelah ini spasi atau dia ada di spesial case, klo iya, berarti dia udah satu kata dan diappend
        if i + 1 < len(texts):
            if (texts[i + 1] in special_cases or texts[i + 1] == spasi or tempWord in special_cases):
                tokenized.append(tempWord)
                tempWord = ""
    tokenized.append(tempWord) # buat append sisa terakhir

    tempToken = tokenized
    tokenized = []
    # buang string kosong
    for token in tempToken:
        if token != "" or token != '':
            tokenized.append(token)
    # print(tokenized)
    return tokenized


# print(tokenizer("input.txt"))