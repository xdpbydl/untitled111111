import win32com.client


"""打开wordk,写入、粘贴内容，保存。"""
word = win32com.client.Dispatch('Word.Application')
word_file = r'E:\TEMP\6TEST\12.docx'
try:
    doc = word.Documents.Open(word_file)
except:
    doc = word.Documents.Add()
# doc.Content.Copy()
# doc.Content.PasteAndFormat()
# 运行下句代码后，s获得新建文档的光标焦点，也就是图中的回车符前
s = word.Selection
# 用“Hello, World!“替换s代表的范围的文本
# s.Text = 'Hello, world!'
s.Paste()
doc.Save(NoPrompt=True)
word.Quit()
