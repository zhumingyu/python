"""
replace(old, new, count)
old:搜索值
new:要替换的新值
count:可选，最大的替换次数  
"""
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)

x = txt.replace("one", "three", 2)
print(x)
