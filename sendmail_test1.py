import SendMail
import private as pv


m = SendMail.SendMail(username=pv.fasong, passwd=pv.key, title="Test2020", recv=["88ahu@163.com"], content = '''
<h5>这是一份测试邮件，！！！！</h5>
<p>图片展示：</p>
<p><img src="cid:image1"></p>
 ''', file='E:/TEMP/untitled111111/WX_File.xlsx', image='E:/TEMP/untitled111111/test.png')
m.send_mail()

