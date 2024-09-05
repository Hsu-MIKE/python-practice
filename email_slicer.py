#  email的字串分析
email = 'mike34249822@gmail.com'
index = email.index('@')             #.index  找出位置
print(index)                       #顯示出@在這個字串中的第9個索引
print(email[0:index])                     #print email裡從0到index(第9位)的值，可以省略0，代表取得9以前的所有字串
print(email[(index+1):])           # :後面不要接東西就會取得到最後，不要取到@所以index+1
