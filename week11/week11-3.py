# 輾轉相除法 (剪髮 大約就是 除法取餘數)
a = 12346789012
b = 98765432101

def ged(a, b): #上週教過 函式 的定義
  print(a, b) #想讓你看到過程, 所以把 a, b 印出來
  if a==0: return b # 終止條件,遇到0的話, 另一邊是答案
  if b==0: return a # 終止條件, 遇到0的話, 另一邊是答案
  return ged(b, a%b) # 函式呼叫函式, 一直做到成功為止

ans = ged(a, b) #問專業的 ged()函式, 看答案是什麼
print(ans)