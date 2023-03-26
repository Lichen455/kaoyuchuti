import tkinter as tk
from tkinter import ttk, messagebox, IntVar ,StringVar
from tkinter.ttk import Style, Checkbutton, Radiobutton
import tkinter.font as tkFont
from ttkthemes import ThemedTk
import variable
import main
import tkinter.font as font

from ttkbootstrap import Style
def center_window(root):
    # 获取屏幕尺寸以计算布局参数，使窗口居中
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    width = 800
    height = 500
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)


difficulty = '简单', '中等', '困难'


def CreateToolTip(widget, text):  # 移动鼠标显示信息
    def enter(event):
        # 创建一个提示框
        global tipwindow
        x = y = 0
        x, y, cx, cy = widget.bbox("insert")
        x += widget.winfo_rootx() + 25
        y += widget.winfo_rooty() + 20
        tipwindow = tk.Toplevel(widget)
        tipwindow.wm_overrideredirect(1)
        tipwindow.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tipwindow, text=text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "12", "normal"))
        label.pack(ipadx=1)

    def close(event):
        # 销毁提示框
        global tipwindow
        if tipwindow:
            tipwindow.destroy()

    # 绑定事件到widget上
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", close)


def on_button_click_english():
    variable.Subject = "English"
    text_font = tkFont.Font(size=2)
    top1 = tk.Toplevel()
    top1.title("选择条件")
    center_window(top1)

    def on_text_click(event):
        #     """function that gets called whenever text is clicked"""
        if text1.get("1.0", tk.END) == '若为空，则材料AI自拟\n':
            text1.delete("1.0", tk.END)  # delete all the text in the entry
            text1.insert(tk.END, '')  # Insert blank for user input
            text1.config(fg='black')

    def on_focusout(event):
        if text1.get("1.0", tk.END) == '\n':
            text1.insert(tk.END, '若为空，则材料AI自拟')
            text1.config(fg='grey')

    text1 = tk.Text(top1, width=40, height=1, wrap='char')
    text1.insert(tk.END, '若为空，则材料AI自拟')
    text1.config(fg='grey', font=("微软雅黑", 8))
    text1.bind('<FocusIn>', on_text_click)
    text1.bind('<FocusOut>', on_focusout)
    # text1.configure("Bold.TButton", font=("Helvetica", 9, "bold"))
    # default_font1 = tkFont.nametofont("TkDefaultFont")
    # text1.configure(font=9)
    label1 = tk.Label(top1, text="相关内容：")
    text2 = tk.Text(top1, width=70, height=60, wrap='char')
    text2.place(relx=0.48, rely=0.05, relwidth=0.5,relheight=0.9)
    text2.configure(font=("微软雅黑",8))
    types = '单项选择题', '完形填空题', '阅读理解题', '作文题'
    ytypes = ['记叙文', '说明文', '议论文', '应用文', '奇幻小说']
    v1 = IntVar(value=1)
    for i in range(3):
        Radiobutton(top1, text=difficulty[i], variable=v1, value=i + 1).place(relx=0.15 * i, rely=0)
    v2 = IntVar(value=1)
    checkboxes = []

    def v2_show_checkboxes():
        for i in range(len(checkboxes)):
            if v2.get() == 5:
                if i < 3:
                    checkboxes[i].place(relx=i * 0.15, rely=0.21)
                #                 elif i<5:
                #                     checkboxes[i].place(relx=(i-3)*0.25,rely=0.35)
                else:
                    checkboxes[i].place(relx=(i - 3) * 0.25, rely=0.28)
                label1.place(relx=0, rely=0.35)
                text1.place(relx=0, rely=0.42, relwidth=0.4, relheight=0.1)
            else:
                checkboxes[i].place_forget()
                label1.place(relx=0, rely=0.21)
                text1.place(relx=0, rely=0.28, relwidth=0.4, relheight=0.1)

    Radiobutton(top1, text=types[0], variable=v2, value=1, command=v2_show_checkboxes).place(relx=0, rely=0.07)
    Radiobutton(top1, text=types[1], variable=v2, value=4, command=v2_show_checkboxes).place(relx=0.25, rely=0.07)
    Radiobutton(top1, text=types[2], variable=v2, value=5, command=v2_show_checkboxes).place(relx=0., rely=0.14)
    Radiobutton(top1, text=types[3], variable=v2, value=6, command=v2_show_checkboxes).place(relx=0.25, rely=0.14)
    v3 = IntVar(value=1)

    def v3_show():

        if v3.get() == 1 or 11 or 21 or 31 or 2:
            label1.place(relx=0, rely=0.35)
            text1.place(relx=0, rely=0.42, relwidth=0.4, relheight=0.1)

    radiobutton = Radiobutton(top1, text=ytypes[0], variable=v3, value=1, command=v3_show)
    checkboxes.append(radiobutton)
    radiobutton = Radiobutton(top1, text=ytypes[1], variable=v3, value=11, command=v3_show)
    checkboxes.append(radiobutton)
    radiobutton = Radiobutton(top1, text=ytypes[2], variable=v3, value=21, command=v3_show)
    checkboxes.append(radiobutton)
    radiobutton = Radiobutton(top1, text=ytypes[3], variable=v3, value=31, command=v3_show)
    checkboxes.append(radiobutton)
    radiobutton = Radiobutton(top1, text=ytypes[4], variable=v3, value=2, command=v3_show)
    checkboxes.append(radiobutton)


    def on_submit_english():  # 获取题目的命令
        # 获取文本框1中的内容
        variable.content = text1.get("1.0",tk.END).strip()
        if variable.content=='若为空，则材料AI自拟':
            variable.content =''
        variable.type = v2.get()
        variable.difficulty=v1.get()
        if variable.type == 5:
            variable.rcqtype = v3.get()
        main.main()
        text2.delete('1.0',tk.END)
        text2.insert(tk.END, variable.text)


    button = ttk.Button(top1, text="获取题目", command=on_submit_english)
    button.place(relx=0.1, rely=0.95, relwidth=0.2, anchor='w')


def on_button_click_history():
    variable.Subject = "History"
    top = tk.Toplevel()
    top.title("选择条件")
    center_window(top)

    def on_text_click(event):
        #     """function that gets called whenever text is clicked"""
        if text1.get("1.0", tk.END) == '若为空，则材料AI自拟\n':
            text1.delete("1.0", tk.END)  # delete all the text in the entry
            text1.insert(tk.END, '')  # Insert blank for user input
            text1.config(fg='black')

    def on_focusout(event):
        if text1.get("1.0", tk.END) == '\n':
            text1.insert(tk.END, '若为空，则材料AI自拟')
            text1.config(fg='grey')

    text1 = tk.Text(top, width=40, height=1, wrap='char')
    text1.insert(tk.END, '若为空，则材料AI自拟')
    text1.config(fg='grey',font=("微软雅黑", 8))
    text1.bind('<FocusIn>', on_text_click)
    text1.bind('<FocusOut>', on_focusout)
    label1 = tk.Label(top, text="相关内容：")
    label3 = tk.Label(top, text="材料内容：")
    label2 = tk.Label(top, text="题目数量：")
    text3 = tk.Text(top, width=10, height=1)
    text2 = tk.Text(top, width=70, height=60, wrap='char')
    text2.configure(font=("微软雅黑", 8))
    text2.place(relx=0.48, rely=0.05, relwidth=0.5,relheight=0.9)
    checkboxes = []

    def on_submit_history():  # 获取题目的命令
        # 获取文本框1中的内容
        variable.content = text1.get("1.0", tk.END).strip()
        if variable.content=='若为空，则材料AI自拟':
            variable.content =''
        variable.num=text3.get("1.0", tk.END).strip()
        #         # 根据文本框1中的内容生成应答
        #         response = "You said: " + content

        #         response+=f'\n已选：{types[v2.get()-1]}'

        #         response+=f'\n已选：{difficulty[v1.get()-1]}'
        variable.type = v3.get()
        variable.ctype = v2.get()
        if variable.ctype==2:
            variable.type=0
        variable.difficulty = v1.get()
        # 将应答插入到文本框2中

    #         text2.delete("1.0", tk.END)
    #         text2.insert(tk.END, response)
        main.main()
        text2.delete('1.0', tk.END)
        text2.insert(tk.END,variable.text)

    button = ttk.Button(top, text="获取题目", command=on_submit_history)
    button.place(relx=0.1, rely=0.95, relwidth=0.2, anchor='w')

    #     vars1 = [tk.IntVar() for _ in range(3)]

    def v2_show_checkboxes():  # 显示复选框
        for i in range(len(checkboxes)):
            if v2.get() == 1:  # 选单选
                checkboxes[i].place(relx=0.12 * i, rely=0.15)
            else:
                checkboxes[i].place_forget()
                label1.place_forget()
        if v2.get() == 2:  # 选简答
            label3.place(relx=0, rely=0.15)
            text1.place(relx=0, rely=0.22, relwidth=0.4, relheight=0.3)
            label2.place(rely=0.53)
            text3.place(relx=0.13, rely=0.55)
        else:
            text1.place_forget()
            label3.place_forget()
            label2.place_forget()
            text3.place_forget()

    def v3_show():
        for i in range(4):
            if v3.get() == i + 1:
                label1.place(relx=0, rely=0.22)
                text1.place(relx=0, rely=0.30, relwidth=0.2, relheight=0.1)
                if i == 0:
                    text1.place(relx=0, rely=0.30, relwidth=0.4, relheight=0.3)
                break
            else:
                text1.place_forget()
                label1.place_forget()

    types = ['单选题', '简答题']
    xtypes = '材料题', '年份题', '政策题', '意义题'
    v1 = IntVar(value=1)
    for i in range(3):
        Radiobutton(top, text=difficulty[i], variable=v1, value=i + 1).place(relx=0.15 * i, rely=0)
    v2 = IntVar(value=1)
    for i in range(2):
        Radiobutton(top, text=types[i], variable=v2, value=i + 1, command=v2_show_checkboxes).place(relx=0.25 * i,
                                                                                                    rely=0.07)

    v3 = IntVar(value=1)
    for i in range(4):
        radiobutton = Radiobutton(top, text=xtypes[i], variable=v3, value=i + 1, command=v3_show)
        checkboxes.append(radiobutton)

def on_button_click_API():
    top2 = tk.Toplevel()
    top2.title("请输入API")
    width = 500 # 窗口宽度
    height = 200 # 窗口高度
    screen_width = top2.winfo_screenwidth() # 屏幕宽度
    screen_height = top2.winfo_screenheight() # 屏幕高度
    x = (screen_width // 2) - (width // 2) # x 坐标
    y = (screen_height // 2) - (height // 2) # y 坐标
    top2.geometry(f"{width}x{height}+{x}+{y}") # 设置窗口位置和大小
    api = tk.StringVar()

    signin = ttk.Frame(top2)
    signin.pack(padx=10, pady=10, fill='x', expand=True)
    api_label = ttk.Label(signin, text="API Key:")
    api_label.pack(fill='x', expand=True)
    api_entry = ttk.Entry(signin, textvariable=api)

    # def on_text_click(event):
    #     #     """function that gets called whenever text is clicked"""
    #     if text1.get("1.0", tk.END) == 'Enter your text here\n':
    #         text1.delete("1.0", tk.END)  # delete all the text in the entry
    #         text1.insert(tk.END, '')  # Insert blank for user input
    #         text1.config(fg='black')
    #
    # def on_focusout(event):
    #     if text1.get("1.0", tk.END) == '\n':
    #         text1.insert(tk.END, 'Enter your text here')
    #         text1.config(fg='grey')
    #
    # text1 = tk.Text(top2, width=40, height=1, wrap='char')
    # text1.insert(tk.END, 'Enter your text here')
    # text1.config(fg='white')
    # text1.bind('<FocusIn>', on_text_click)
    # text1.bind('<FocusOut>', on_focusout)
    # api_entry = tk.Text(top2, width=40, height=1, wrap='char')
    # api_entry.insert(tk.END, 'Enter your text here')
    # api_entry.config(fg='black')
    # api_entry.bind('<FocusIn>', on_text_click)
    # api_entry.bind('<FocusOut>', on_focusout)
    api_entry.pack(fill='x', expand=True)
    api_entry.focus()
    def login_clicked():
        variable.api_Key=api_entry.get()
        f = open("data/apikey.tls", "w")
        f.write(variable.api_Key)
        f.close()
        top2.destroy()
#         print(x)
    # login button
    login_button = ttk.Button(signin, text="Enter", command=login_clicked)
    login_button.pack(fill='x', expand=True, pady=10)
# style=Style(theme='darkly')
# root=style.master
# root = ThemedTk(theme="arc", toplevel=True, themebg=True)
root =tk.Tk()
root.iconbitmap('book.ico')
# 统一改变字体大小
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=15)

root.title("选择科目")
center_window(root)
subject = '历史', '英语'

# xd = 1, 3, 5, 1, 3, 5, 1, 3, 5
yd = 1, 1, 1, 2, 2, 2, 3, 3, 3
# style = ttk.Style()
# style.configure('my.TButton', bordercolor='red')

button0 = ttk.Button(root, text=subject[0], command=on_button_click_history)
button0.place(x=180, y=yd[0] * 100, width=200, height=100)
button1 = ttk.Button(root, text=subject[1], command=on_button_click_english)
button1.place(x=420, y=yd[1] * 100, width=200, height=100)
style = ttk.Style()
# 定义一个 Bold.TButton 样式
style.configure("Bold.TButton", font=("Helvetica", 15, "bold"))
f=font.Font(size=10)
button2=tk.Button(root,text='点击输入API',font=f,command=on_button_click_API).place(relx=0.8,rely=0.02,relheight=0.05)

root.mainloop()