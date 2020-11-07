import tkinter as tk

#计算最优值
def LCSLength(m, n, x, y, c, b):
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i+1][j+1] = c[i][j]+1
                b[i+1][j+1] = 1
            elif c[i+1][j] >= c[i][j+1]:
                c[i+1][j+1] = c[i+1][j]
                b[i+1][j+1] = 2
            else:
                c[i+1][j+1] = c[i][j+1]
                b[i+1][j+1] = 3

#构造最长公共子序列
def LCS(i, j, x, b):
    if i==0 or j==0:
        return
    if b[i][j] == 1:
        LCS(i-1,j-1,x,b)
        print(x[i-1], end=' ')
        text.insert(tk.INSERT, x[i-1]+' ')
    elif b[i][j] == 2:
        LCS(i,j-1,x,b)
    else:
        LCS(i-1,j,x,b)

#得出所有最长公共子序列
def GetLCS(i,j,c,x,y,s):
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            s+=x[i-1]
            i-=1
            j-=1
        else:
            if c[i-1][j]>c[i][j-1]:
                i-=1
            elif c[i-1][j]<c[i][j-1]:
                j-=1
            else:
               GetLCS(i-1,j,c,x,y,s)
               GetLCS(i,j-1,c,x,y,s)
               return
    allResult.insert(tk.INSERT,s[::-1]+'\n')
    print(s[::-1])

def Input():
    length.delete('1.0','end')
    text.delete('1.0', 'end')
    formC.delete('1.0', 'end')
    formB.delete('1.0', 'end')
    m = int(entry_XLength.get())
    n = int(entry_YLength.get())
    x = entry_XSequence.get()
    y = entry_YSequence.get()
    c = [[0 for x in range(n+1)]for y in range(m+1)]
    b = [[0 for x in range(n+1)] for y in range(m+1)]
    LCSLength(m,n,x,y,c,b)
    LCS(m,n,x,b)
    s=''
    GetLCS(m,n,c,x,y,s)
    length.insert(tk.INSERT,c[m][n])
    formC.insert(tk.INSERT,c)
    formB.insert(tk.INSERT,b)
    print(c)
    print(b)

#Input()

window = tk.Tk()
window.title('最长公共子序列')
window.geometry('800x600')
tk.Label(window, text = '最长公共子序列', font=('楷体',25)).place(x=300,y=50)
tk.Label(window, text = "X序列的长度",font=('楷体',12)).place(x=50, y=150)
var_XLength = tk.StringVar()
entry_XLength = tk.Entry(window, textvariable=var_XLength, font=('Arial',12))
entry_XLength.place(x=150, y=150)
tk.Label(window, text = "X序列", font=('楷体',12)).place(x=400,y=150)
var_XSequence = tk.StringVar()
entry_XSequence = tk.Entry(window, textvariable=var_XSequence, font=('Arial',12))
entry_XSequence.place(x=450, y=150)
tk.Label(window, text = "Y序列的长度", font=('楷体',12)).place(x=50,y=200)
var_YLength = tk.StringVar()
entry_YLength = tk.Entry(window, textvariable=var_YLength, font=('Arial',12))
entry_YLength.place(x=150, y=200)
tk.Label(window, text = "Y序列", font=('楷体',12)).place(x=400,y=200)
var_YSequence = tk.StringVar()
entry_YSequence = tk.Entry(window, textvariable=var_YSequence, font=('Arial',12))
entry_YSequence.place(x=450, y=200)
btn = tk.Button(window, text = "冲！", font=('圆体',15),command = Input)
btn.place(x=350,y=230)

tk.Label(window, text = "最长长度", font=('楷体',12)).place(x=50,y=300)
length = tk.Text(window, font=("楷体", 15))
length.place(x=150, y=300,height=30,width=200)

tk.Label(window, text = "结果", font=('楷体',12)).place(x=400,y=300)
text = tk.Text(window, font=("楷体", 15))
text.place(x=450, y=300, width=200,height=30)

tk.Label(window, text = "c表", font=('楷体',12)).place(x=50,y=350)
formC = tk.Text(window, font=("楷体", 15))
formC.place(x=150, y=350, width=200,height=100)

tk.Label(window, text = "b表", font=('楷体',12)).place(x=400,y=350)
formB = tk.Text(window, font=("楷体", 15))
formB.place(x=450, y=350, width=200,height=100)

tk.Label(window, text = "所有结果", font=('楷体',12)).place(x=50,y=480)
allResult = tk.Text(window, font=("楷体", 15))
allResult.place(x=150, y=480, width=600,height=100)

window.mainloop()