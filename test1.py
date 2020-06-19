import SendMail

username = "46311295@qq.com"  # 用户名（发件人的邮箱账号或用户名）
passwd = "xefqwobdzspgbijb"  # 16位的SMTP授权码（不含空格）
recv = ['46311295@qq.com']  # 收件人，多个要传list ['a @ qq.com','b @ qq.com]
title = " 邮件标题"  # 邮件标题
content = '''
               <h1>邮件测试</h1>
               <p>图片展示：</p>
               <p><img src="cid:image1"></p>
          '''  # 邮件正文
file = r'E:\\TEMP\\google\\对有些人和行为,我只有一个“滚”2020-06-19.png'  # 绝对路径
image = file  # 图片路径（绝对路径）
email_host = 'smtp.qq.com'  # smtp服务器地址,默认为qq邮箱的服务器

SendMail.SendMail(username=username, passwd=passwd, recv=recv, title=title, content=content, file=file, image=image)
