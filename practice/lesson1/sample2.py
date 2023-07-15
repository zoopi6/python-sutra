# 文字列の扱い方

# スライス
word = 'Python'

print(word[2]) # pythonのインデクスは0から。この場合は、tが出力されるはず

# 最後の文字を出力する場合は-1
print(word[-1])

# 文字列の書き換えは不可
# word2 = 'Python'
# word2[0] = 'j'

word2 = 'Python'
word3 = 'j' + word2[1:]
print(word3)

# format
print('wordは{0}'.format(word))

#fstring
print(f'word2は {word2}')
