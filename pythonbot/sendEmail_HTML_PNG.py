# HTML 文本中添加图片

# 要把一个图片嵌入到邮件正文中，如果直接在HTML邮件中链接图片地址是不行的，
# 大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。

# 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，
# 然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。

import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr



# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = sys.argv[1]  # 用户名
mail_pass = sys.argv[2] # 口令 163和QQ邮箱的第三方是另外的授权密码，而非原邮箱密码

sender = "276125681@qq.com"  # 发送者的邮箱
receivers = ["13917732040@139.com"]  # 接收邮件，其他人的邮箱

# 创建一个根实例
msgRoot = MIMEMultipart("related")

msgRoot["From"] = formataddr(["小东", sender])  # 发送人
msgRoot["To"] = formataddr(["小明", receivers[0]])  # 接收人

subject = 'HTML带图片的邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')  # 邮件主题

# 创建一个存放正文的实例，并添加进根实例
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>Python 邮件发送测试...</p>
<p>图片演示：</p>
<p><img src="cid:0"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 创建图片实例，并添加进根实例
fp = open('./Shanghai.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<0>')
msgRoot.attach(msgImage)

try:
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
    smtpObj.quit()
except smtplib.SMTPException:
    print("Error: 无法发送邮件")