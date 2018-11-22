"""
split(separator, max)
spearator:指定分隔符,默认为所有空字符，包括空格，换行(\n),制表符(\t)等
max:默认max-1次，分割次数
"""
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(str.split())
print(str.split(' ', 1))
