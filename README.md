# [BLOG](https://paoschools.com/python-line-chatbot/)

# Line-chatbot
line chatbot with Dialog Flow, Ngrok, Flask
for more info you can read below or at this link : https://paoschools.com/python-line-chatbot/

<hr>
<h1>Line Covid Chatbot ด้วย Dialogflow และ Python</h1>
<!-- wp:paragraph -->
<p>ผู้เขียนบทความ : นายปัณณวัชญ์ ตราทองคำ coe#12</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">1. ความเป็นมา</h3>
<!-- /wp:heading -->

<p>&nbsp;เนื่องจากเชื้อไวรัสโคโรน่าสายพันธุ์ใหม่ 2019 หรือ COVID-19 เป็นไวรัสข้ามสายพันธุ์ที่สันนิษฐานว่าเกิดจากค้างคาวมาติดเชื้อในคน โดยเริ่มระบาดในมณฑลอู่ฮั่นของประเทศจีนในช่วงปลายปี ค.ศ.2019 จนกระทั่งมีการระบาดไปยังประเทศอื่นๆ ทั่วโลก สถานการณ์การแพร่ระบาดของ COVID-19 มีความรุนแรงเพิ่มมากขึ้น ปัจจุบันสถานการณ์การแพร่ระบาดของเชื้อ COVID-19 มีความรุนแรงเพิ่มขึ้นอย่างต่อเนื่อง องค์การอนามัยโลกได้ประกาศว่าการแพร่ระบาดของเชื้อดังกล่าวเป็นภัยพิบัติฉุกเฉินระดับโลก เพื่อให้ประชาชนสามารถเข้าถึงข้อมูลรายงานสถานการณ์ COVID-19 ได้ ผู้เขียนจึงได้จัดทำ LINE COVID CHATBOT ขึ้นมาเนื่องจาก LINE เป็นแอปพลิเคชันที่ทุกคนใช้งานกันในชีวิตประจำวันอยู่ทั่วไปแล้วนั้นเอง</p>

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">2. วัตถุประสงค์</h3>
<!-- /wp:heading -->

<p>2.1 เพื่อศึกษาหาความรู้ในการใช้ภาษา Python<br>2.2 เพื่อพัฒนาโปรแกรม Chatbot ที่ใช้ในการรับข้อมูลข่าวสารเกี่ยวกับ Covid ไปประยุกต์ใช้ได้จริง<br>2.3 เพื่อนำความรู้ที่ได้ไปใช้ต่อยอดในการศึกษาและการทำงาน</p>

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">3. ขอบเขต</h3>
<!-- /wp:heading -->

<p>3.1 โปรแกรม Chatbot สามารถรองรับการทำงานได้ทั้งใน PC, IOS และ Andriod<br>3.2 โปรแกรม Chatbot สามารถแสดงข้อมูลโควิด-19 ได้</p>

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">4. ประโยชน์ที่คาดว่าจะได้รับ</h3>
<!-- /wp:heading -->

<p>4.1 ผู้ใช้สามารถใช้โปรแกรม Line Chatbot เพื่อตรวจสอบข้อมูลโควิด-19 ได้<br>4.2 มีคำสั่งเฉพาะเพื่อค้นหาเพียงข้อมูลที่ต้องการทราบ</p>

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">5. ความรู้ที่เกี่ยวข้อง</h3>
<!-- /wp:heading -->

<p>ในส่วนกระบวนการการทำงานของทั้งระบบนั้นผู้เขียนได้ทำเป็นภาพแสดงการทำงานโดยย่อไว้ดังนี้</p>
<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/proceduce.jpg"><img class="size-full wp-image-2476 aligncenter" src="https://www.paoschools.com/wp-content/uploads/2021/03/proceduce.jpg" alt="" width="2000" height="500"></a></p>
<h4><strong>5.1 API</strong></h4>
<p>สำหรับระบบนี้สิ่งที่สำคัญที่สุดและไม่สามารถขาดไปได้เลยคือ API หรือ Application Programing Interface ซึ่งเป็นบริการช่องทางในการเชื่อมต่อเพื่อแลกเปลี่ยนข้อมูลจากระบบหนึ่งไปอีกระบบหนึ่ง ซึ่งผู้เขียนได้ใช้บริการ LINE Messaging API ของ LINE Developer เพื่อใช้งาน Chatbot GUI และส่วนต่อมาคือบริการข้อมูล COVID-19 API ของกรมควบคุมโรค</p>
<p>API ที่ใช้ในระบบ<br><a href="https://covid19.ddc.moph.go.th/th">กรมควบคุมโรค รายงานสถานการณ์ โควิด-19</a><br><a href="https://developers.line.biz/en/services/messaging-api/">LINE Messaging API</a></p>
<p>ในส่วนของ LINE Messaging API สามารถดูวิธีการใช้บริการได้ที่หัวข้อ 5.3 ด้านล่างนี้เลย</p>
<p>ในส่วนของ COVID-19 API นั้นทางผู้ให้บริการได้ให้ API มาในรูปแบบ JSON ซึ่ง JSON เป็นข้อมูลรูปแบบ text ที่มีการเก็บข้อมูลในรูปแบบ key, value</p>
<p>ยกตัวอย่างข้อมูลใน COVID-19 API</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>{"Confirmed":28863}</code></pre>
<!-- /wp:code -->

<p>จะให้ได้ว่าข้อมูลใน API นี้เป็นรูปแบบ JSON โดยมี key คือ Confirmed และ value คือค่าด้านหลังซึ่งมีการอัพเดทเปลี่ยนแปลงตามผู้ให้บริการ ซึ่งในหนึ่ง JSON API สามารถเก็บข้อมูลได้หลายตัวด้วยกัน เช่น</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>{"Confirmed":28863,"Recovered":27426,"Hospitalized":1343,"Deaths":94}</code></pre>
<!-- /wp:code -->

<p>โดยเราสามารถเข้าถึงข้อมูลได้ด้วยการใช้ภาษา Python โดยใช้ Library JSON และ Requests ซึ่งมีเขียนอธิบายด้านล่างในหัวข้อที่ 5.5</p>

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">5.2 ภาษา Python และ Virtual Environments venv</h4>
<!-- /wp:heading -->

<p>ส่วนแรกที่ต้องใช้คือ พื้นฐานการใช้ภาษา Python ทั่วไป โดยผู้เขียนใช้ Virtual Environments venv ในการทำโปรเจคนี้</p>
<p>เริ่มแรกให้สร้างโฟลเดอร์ที่ต้องการเก็บไฟล์โครงงานขึ้นมาก่อน จะสร้างชื่ออะไรก็ได้ ไปที่ path ข้างบนพิมพ์ว่า cmd เพื่อเปิด command line จากนั้นให้พิมพ์คำสั่งว่า</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>pip install virtualenv</code></pre>
<!-- /wp:code -->

<p>เมื่อพิมพ์เสร็จให้สร้าง virtualenv ตามด้วยชื่อ โดยผู้เขียนได้ตั้งชื่อโฟลเดอร์ว่า venv</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>virtualenv venv</code></pre>
<!-- /wp:code -->

<p>เมื่อสร้างเสร็จจะมีโฟลเดอร์ venv ปรากฏขึ้น ภายในจะเป็น python กลับมาที่ cmd ต่อจากนั้นให้พิมพ์ว่า</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>venv\Scripts\activate </code></pre>
<!-- /wp:code -->

<p>จะเห็นว่า path ของเราเปลี่ยนไปเป็นมี (venv) มาอยู่ข้างหน้าแล้ว ให้เราพิมคำสั่งว่า</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>code . </code></pre>
<!-- /wp:code -->

<p>เพื่อเข้าไปที่ Text Editor ของ vscode</p>
<p>เมื่อเปิดมาแล้วโปร<span id="rmm">แ</span>กรม vs code จะทำงานอยู่ภายใน venv เวลาจะ install ก็ต้อง activate ก่อนมันถึงจะเรียกใช้ได้&nbsp; ถ้าไม่ activate ก่อนมันจะไม่สามารถทำงานได้ เพราะมันเรียกหาไฟล์แพตเกจต่างๆที่เราลงไว้ไม่เจอ เพราะทุกอย่างอยู่ใน venv ทั้งหมด และเราสามารถเช็คได้ด้วยว่ามันทำการ activate ให้เรารึยังจากรูปด้านล่างเลย ถ้าทำการ active แล้วมันจะขึ้นมาให้แถบฟ้าๆ</p>
<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/venv.png"><img class="wp-image-2025 aligncenter" src="https://www.paoschools.com/wp-content/uploads/2021/03/venv.png" alt="" width="675" height="98"></a></p>

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">5.3 Line Messaging Api</h4>
<!-- /wp:heading -->

<p>เพื่อให้เราสามารถใช้งานโปรแกรม Chat bot ของ LINE ได้ เราจำเป็นต้องสมัคร LINE Developer เพื่อขอการใช้งาน Messaging API โดยในที่นี้ผู้เขียนขอไม่ลงรายละเอียด แต่สามารถทำตามแหล่งอ้างอิงที่ผู้เขียนได้ทำตามได้เลย</p>
<p id="b1aa" class="dy dz ea eb b ec ed ee ef eg eh ei ej ek el em en eo ep eq er es et eu ev ew ex"><a href="https://medium.com/linedevth/%E0%B8%9B%E0%B8%90%E0%B8%A1%E0%B8%9A%E0%B8%97%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-line-bot-b2cb90643901">ปฐมบทการสร้าง LINE Bot</a></p>
<p>ซึ่งเมื่อเราสร้างเสร็จสิ้นตามทุกขั้นตอนแล้ว ก็ให้เราทำการเพิ่ม LINE Chat bot เพื่อใช้งานในขั้นต่อไป</p>
<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/line-msg-api.png"><img class="size-full wp-image-2043 aligncenter" src="https://www.paoschools.com/wp-content/uploads/2021/03/line-msg-api.png" alt="" width="537" height="500"></a></p>

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">5.4 การใช้ Dialogflow</h4>
<!-- /wp:heading -->

<p>ในส่วนต่อมาคือ Dialogflow เราใช้เพื่อสร้าง Intent ในการโต้ตอบระหว่างผู้ใช้กับ Chat bot&nbsp;<br>สามารถสมัครใช้งานได้ที่ Link :&nbsp;<a href="https://dialogflow.cloud.google.com/#/getStarted">https://dialogflow.cloud.google.com/#/getStarted</a></p>
<p>เมื่อสมัครใช้งานเสร็จเรียบร้อยแล้ว ให้ทำการเชื่อมต่อการใช้งานกับ LINE หลังจากนั้นใช้เพื่อสร้าง Intent ในการโต้ตอบระหว่างผู้ใช้กับ Chat bot ซึ่งผู้เขียนได้ทำการใส่อ้างอิงข้อมูลการใช้งาน Dialogflow ไว้แล้วในส่วนอ้างอิง</p>
<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/dialogflow.png"><img class="aligncenter wp-image-2039 size-full" src="https://www.paoschools.com/wp-content/uploads/2021/03/dialogflow.png" alt="" width="986" height="625"></a></p>

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">5.5 Library JSON, Flask และ Requests</h4>
<!-- /wp:heading -->

<p>ก่อนที่จะไปลงรายละเอียดในการใช้งาน Library แต่ละตัวนั้นมาดูที่วิธีการติดตั้งกันก่อน โดยผู้เขียนใช้ Flask Microframework เพื่อใช้งาน Python ร่วมกับ webserver และใช้ Requests ซึ่งเป็น HTTP Library โดยให้พิมพ์คำสั่งเพื่อติดตั้ง Flask และ Requests</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>pip install flask</code></pre>
<!-- /wp:code -->

<p>และ</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>pip install requests</code></pre>
<!-- /wp:code -->

<p>หลังจากที่ติดตั้งเสร็จเรียบร้อยแล้ว ในส่วน Library ที่ผู้เขียนใช้เป็นหลักนั้น ส่วนแรกคือ JSON encoder and decoder โดยใช้สำหรับการอ่านและเขียน JSON ซึ่งมีคำสั่งต่างๆที่จำเป็นต้องใช้อยู่ใน Library นี้ โดยเราสามารถเรียกใช้คำสั่งได้โดยการเขียนโค้ดว่า</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>import json</code></pre>
<!-- /wp:code -->

<p>และคำสั่งที่จำเป็นต้องใช้เพื่อแปลงข้อมูล JSON เพื่ออ่านและส่งข้อมูลมีดังนี้</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>json.dumps()
คือการแปลง Python Object (Dict) ไปเป็น JSON String หรือ Object

json.loads()
คือการแปลง JSON  String ไปเป็น Python Object (Dict)</code></pre>
<!-- /wp:code -->

<p>ต่อมาในส่วนของ Library Requests สามารถเรียกใช้งานโดยเขียนโค้ดไว้ว่า</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>import requests</code></pre>
<!-- /wp:code -->

<p>หลังจากนั้นให้เขียนโค้ดดังนี้เพื่อเก็บข้อมูล API ไว้</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>r = requests.get('ลิ้งของผู้ให้บริการ API', auth=('user', 'pass'))
--หากในส่วนผู้ให้บริการ API ไม่ได้มีการเข้ารหัสไว้สามารถเขียนได้ดังนี้
r = requests.get('https://covid19.th-stat.com/api/open/today')</code></pre>
<!-- /wp:code -->

<p>ต่อมาในส่วนของ Library Flask ผู้เขียนใช้เพื่อสร้าง web server ในการเชื่อมต่อระหว่าง Dialogflow โดยสามารถเรียกใช้งานได้ดังนี้</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>from flask import Flask
</code></pre>
<!-- /wp:code -->

<p>หลังจากนั้นเราใช้ Flask เพื่อเขียนให้โปรแกรมของเราทำงานในรูปแบบ web server โดยใช้ port localhost:5000</p>

<!-- wp:code -->
<pre class="wp-block-code"><code># Flask HTTP METHOD
app = Flask(__name__)

@app.route('/', methods=&#91;'POST', 'GET'])
---
ใส่ฟังก์ชันของโปรแกรมตามต้องการ
---
#Flask deploy web server on http port 5000 
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">5.6 Ngrok</h4>
<!-- /wp:heading -->

<p>Ngrok เป็นตัวช่วยในการทำให้ localhost server ของเรามี public url ทำให้เราสามารถทำ url นี้ไปใช้ webhook เพื่อติดต่อสื่อสารส่งข้อมูลกับ Dialogflow ได้ สามารถดูรายละเอียดวิธีใช้งานได้ในหัวข้อต่อไป</p>
<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/ngrok.png"><img class="aligncenter wp-image-2084 size-full" src="https://www.paoschools.com/wp-content/uploads/2021/03/ngrok.png" alt="" width="963" height="399"></a></p>

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">6.ผลการดำเนินงาน</h3>
<!-- /wp:heading -->

<p>ตัวอย่างภาพการทำงานของระบบโดยเริ่มการทำงานที่ผู้ใช้สามารถดูได้ดังรูป<a href="https://www.paoschools.com/wp-content/uploads/2021/03/flow-1.png"><img class="alignnone size-full wp-image-2799" src="https://www.paoschools.com/wp-content/uploads/2021/03/flow-1.png" alt="" width="1131" height="480"></a></p>
<p>เริ่มต้นการทำงานโปรแกรมด้วยการรันโปรแกรมใน Python</p>
<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/st01.png"><img class="size-full wp-image-2091 aligncenter" src="https://www.paoschools.com/wp-content/uploads/2021/03/st01.png" alt="" width="690" height="284"></a></p>
<p>เมื่อรันแล้วจะเห็นได้ว่า มีการใช้งานบน Port 5000 ให้เราไปที่ Ngrok เพื่อสร้าง public url ให้พิมพ์คำสั่งว่า</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>ngrok http 5000</code></pre>
<!-- /wp:code -->

<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/st02.png"><img class="aligncenter wp-image-2093 size-full" src="https://www.paoschools.com/wp-content/uploads/2021/03/st02.png" alt="" width="978" height="476"></a><br>เมื่อรันแล้วจะได้ public url ให้เรา copy เพิ่อไปเชื่อมต่อ webhook ใน dialogflow</p>
<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/st03.png"><img class="size-full wp-image-2099 aligncenter" src="https://www.paoschools.com/wp-content/uploads/2021/03/st03.png" alt="" width="959" height="477"></a><a href="https://www.paoschools.com/wp-content/uploads/2021/03/st04.png"><img class="size-full wp-image-2101 aligncenter" src="https://www.paoschools.com/wp-content/uploads/2021/03/st04.png" alt="" width="985" height="624"></a></p>
<p>หลังจากนั้นกด Save แล้วสามารถใช้งาน LINE Chat bot ได้เลย</p>
<p>ในขั้นตอนแรกเป็นการใช้คำสั่ง help เพื่อแสดงวิธีการใช้คำสั่งทั้งหมดในการแสดงข้อมูล</p>
<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/Screenshot_2021-03-24-13-01-24-294_jp.naver_.line_.android.jpg"><img class="aligncenter wp-image-2104 size-large" src="https://www.paoschools.com/wp-content/uploads/2021/03/Screenshot_2021-03-24-13-01-24-294_jp.naver_.line_.android-473x1024.jpg" alt="" width="473" height="1024"></a><br>สามารถเรียกข้อมูลโควิด-19 ได้ตามคำสั่งดังรูป</p>
<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/Screenshot_2021-03-24-13-02-35-290_jp.naver_.line_.android.jpg"><img class="wp-image-2106 size-large aligncenter" src="https://www.paoschools.com/wp-content/uploads/2021/03/Screenshot_2021-03-24-13-02-35-290_jp.naver_.line_.android-473x1024.jpg" alt="" width="473" height="1024"></a> <a href="https://www.paoschools.com/wp-content/uploads/2021/03/Screenshot_2021-03-24-13-02-45-021_jp.naver_.line_.android.jpg"><img class="wp-image-2107 size-large aligncenter" src="https://www.paoschools.com/wp-content/uploads/2021/03/Screenshot_2021-03-24-13-02-45-021_jp.naver_.line_.android-473x1024.jpg" alt="" width="473" height="1024"></a></p>
<p>นอกจากนี้หากใช้แอพ LINE ใน IOS หรือ Android จะมีส่วนที่เรียกว่า Rich Menu ซึ่งลิ้งตรงกับรายงานสถานการณ์โควิด-19 ของกรมควบคุมโรคได้โดยตรง โดยไม่ต้องพิมพ์คำสั่ง</p>
<p><a href="https://www.paoschools.com/wp-content/uploads/2021/03/Screenshot_2021-03-24-13-02-52-583_jp.naver_.line_.android.jpg"><img class="wp-image-2108 size-large aligncenter" src="https://www.paoschools.com/wp-content/uploads/2021/03/Screenshot_2021-03-24-13-02-52-583_jp.naver_.line_.android-473x1024.jpg" alt="" width="473" height="1024"></a> <a href="https://www.paoschools.com/wp-content/uploads/2021/03/Screenshot_2021-03-24-13-03-02-178_jp.naver_.line_.android.jpg"><img class="wp-image-2109 size-large aligncenter" src="https://www.paoschools.com/wp-content/uploads/2021/03/Screenshot_2021-03-24-13-03-02-178_jp.naver_.line_.android-473x1024.jpg" alt="" width="473" height="1024"></a></p>

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">โค้ดทั้งหมด</h4>
<!-- /wp:heading -->

<!-- wp:group -->
<div class="wp-block-group"><!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column {"width":"100%"} -->
<div class="wp-block-column" style="flex-basis:100%"><!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column {"width":"100%"} -->
<div class="wp-block-column" style="flex-basis:100%"><!-- wp:code -->
<pre class="wp-block-code"><code>#Import Library
#import statements load Python code that allow us to work with the JSON data format and the HTTP protocol.
import json
import os
import requests
from flask import Flask
from flask import request
from flask import make_response

# Flask
app = Flask(__name__)

@app.route('/', methods=&#91;'POST', 'GET'])

def MainFunction():

    #รับ intent จาก DailogflowJay
    question_from_dailogflow_raw = request.get_json(silent=True, force=True)

    #เรียกใช้ฟังก์ชัน generate_answer เพื่อแยกส่วนของคำถาม
    answer_from_bot = generating_answer(question_from_dailogflow_raw)
    
    #ตอบกลับไปที่ Dailogflow
    r = make_response(answer_from_bot)
    r.headers&#91;'Content-Type'] = 'application/json' #การตั้งค่าประเภทของข้อมูลที่จะตอบกลับไป

    return r

def generating_answer(question_from_dailogflow_dict):

    #Print intent ที่รับมาจาก Dailogflow
    print(json.dumps(question_from_dailogflow_dict, indent=4 ,ensure_ascii=False))

    #เก็บต่า ชื่อของ intent ที่รับมาจาก Dailogflow
    intent_group_question_str = question_from_dailogflow_dict&#91;"queryResult"]&#91;"intent"]&#91;"displayName"] 

    #ลูปตัวเลือกของฟังก์ชั่นสำหรับตอบคำถามกลับ
    if intent_group_question_str == 'dev':
        answer_str = covid_dev()
    elif intent_group_question_str == 'covid':
        answer_str = covid_today()
    elif intent_group_question_str == 'confirmed':
        answer_str = c_confirmed()
    elif intent_group_question_str == 'recovered':
        answer_str = c_recovered()
    elif intent_group_question_str == 'hospitalized':
        answer_str = c_hospitalized()
    elif intent_group_question_str == 'deaths':
        answer_str = c_deaths()   
    elif intent_group_question_str == 'test_text':
        answer_str = test_text()
    else: answer_str = "Error"

    #สร้างการแสดงของ dict 
    answer_from_bot = {"fulfillmentText": answer_str}
    
    #แปลงจาก dict ให้เป็น JSON
    answer_from_bot = json.dumps(answer_from_bot, indent=4) 
    
    return answer_from_bot
    
def test_text():
    answer_function = 'ข้อความจาก python'
    return answer_function

def covid_today():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)

    json_confirmed = json_data&#91;'Confirmed']
    c_confirmed = json.dumps(json_confirmed)

    json_recovered = json_data&#91;'Recovered']
    c_recovered = json.dumps(json_recovered)

    json_hospitalized = json_data&#91;'Hospitalized']
    c_hospitalized = json.dumps(json_hospitalized)

    json_deaths = json_data&#91;'Deaths']
    c_deaths = json.dumps(json_deaths)

    answer_function = 'ยอดติดเชื้อสะสม : ' + c_confirmed + ' คน\n' + 'รักษาหายแล้ว : ' + c_recovered + ' คน\n' + 'รักษาอยู่ในโรงพยาบาล : ' + c_hospitalized + ' คน\n' + 'เสียชีวิต : ' + c_deaths + ' คน'
    return answer_function

def covid_dev():
    c = requests.get('https://covid19.th-stat.com/api/open/today')
    c.json()
    data = json.loads(c.text)
    data = json.dumps(data)
    answer_function3 = data
    #answer_function2 = '{"line":{"text": ' + data + ',"type": "text"} }'
    return answer_function3

def c_confirmed():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data&#91;'Confirmed']
    c_confirmed = json.dumps(covid)
    answer_function = 'ยอดติดเชื้อสะสม : ' + c_confirmed + ' คน'
    return answer_function

def c_recovered():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data&#91;'Recovered']
    c_recovered = json.dumps(covid)
    answer_function = 'รักษาหายแล้ว : ' + c_recovered + ' คน'
    return answer_function

def c_hospitalized():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data&#91;'Hospitalized']
    c_hospitalized = json.dumps(covid)
    answer_function = 'รักษาอยู่ในโรงพยาบาล : ' + c_hospitalized + ' คน'
    return answer_function

def c_deaths():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data&#91;'Deaths']
    c_deaths = json.dumps(covid)
    answer_function = 'เสียชีวิต : ' + c_deaths + ' คน'
    return answer_function

#Flask 
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
</code></pre>
<!-- /wp:code -->

<!-- wp:group -->
<div class="wp-block-group"><!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column {"width":"100%"} -->
<div class="wp-block-column" style="flex-basis:100%"><!-- wp:group -->
<div class="wp-block-group"></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">7. สรุปผลและข้อเสนอแนะ</h3>
<!-- /wp:heading -->

<p>โปรแกรมสามารถใช้งานได้อย่างถูกต้องและไม่มีปัญหา ทั้งนี้มีองค์ประกอบอย่างอื่นขึ้นอยู่กับผู้ใช้ เช่น พิมพ์คำสั่งไม่ถูกต้อง การเชื่อมต่ออินเตอร์เน็ตไม่เสถียร หรือจากฝั่งผู้ให้บริการข้อมูล เช่น กรมควบคุมโรคมีการอัพเดทข้อมูล หรือ การข้อผิดพลาดทำให้ไม่สามารถให้บริการข้อมูล API ได้ และในส่วนของทางฝั่งโปรแกรมผู้เขียนได้ใช้ ngrok ได้การเปิด public url ซึ่งต้องทำทุกครั้ง ทำให้ลำบากต่อการแก้ไข<br>ข้อเสนอแนะ<br>- การประยุกต์ใช้กับ Database Server หรือ Public Server จะทำให้สามารถดึงประสิทธิของการใช้งานมาได้ดีกว่าหากเทียบกับการใช้งานในรูปแบบ localhost ที่เครื่องของผู้เขียนเอง แต่อาจมีค่าใช้จ่ายในส่วน Server เพิ่มเติมเข้ามา<br>- ในส่วนของผู้ให้บริการข้อมูล API อย่างกรมควบคุมโรค มีการอัพเดทข้อมูลที่ล่าช้าในบางครั้ง และหากเกิดปัญหาที่ทำให้ไม่สามารถเรียกข้อมูลมาได้ จะทำห้ไม่สามารถเรียกใช้งานในส่วนของโปรแกรมนี้ได้เลย</p>

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">8.ข้อมูลอ้างอิง</h3>
<!-- /wp:heading -->

<ol>
<li>API ที่ใช้ในระบบ<br><a href="https://covid19.ddc.moph.go.th/th">กรมควบคุมโรค รายงานสถานการณ์ โควิด-19</a><br><a href="https://developers.line.biz/en/services/messaging-api/">LINE Messaging API</a></li>
<li>ข้อมูลอ้างอิงเกี่ยวกับการใช้งาน Python&nbsp;<br><a href="https://medium.com/@chanisarauttamawetin/virtual-environments-in-python-%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B9%86%E0%B8%81%E0%B8%B1%E0%B8%9A-vscode-4d23d29dd57e">venv</a><br><a href="https://stackpython.co/tutorial/json-python">การใช้งาน JSON ร่วมกับ Python ครบจบในบทความเดียว</a><br><a href="https://lengyi.medium.com/%E0%B9%83%E0%B8%8A%E0%B9%89-python-%E0%B8%94%E0%B8%B6%E0%B8%87%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5-api-%E0%B8%82%E0%B8%AD%E0%B8%87-corona-virus-covid-19-aa3233c85537">ใช้ Python ดึงข้อมูล API ของ Corona-virus (COVID-19)</a><br><a href="https://www.dataquest.io/blog/python-api-tutorial/">Python API Tutorial: Getting Started with APIs</a><br><a href="https://coronavirus.data.gov.uk/details/developers-guide">Documentations for the API — v.1</a><br><a href="https://www.youtube.com/watch?v=yEiBeyEASRM">ดึงข้อมูล COVID-19 จาก API ที่ส่งค่ากลับมาเป็น JSON ด้วย Python</a><br><a href="https://stackpython.medium.com/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-chatbot-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-python-59e9805c3f1b">สร้าง CHATBOT ด้วย PYTHON</a><br><a href="https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3">How To Use Web APIs in Python 3</a><br><a href="https://realpython.com/api-integration-in-python/">API Integration in Python</a><br><a href="https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html">HTTP Requests in Python 3</a><br><a href="https://www.geeksforgeeks.org/python-convert-json-to-string/">Python – Convert JSON to string</a></li>
<li>ข้อมูลอ้างอิงเกี่ยวกับการใช้ LINE และ Dialogflow<br><a href="https://medium.com/@prapon/%E0%B8%AA%E0%B8%AD%E0%B8%99-%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%97%E0%B8%B3-line-messaging-api-ec29e8e9858e">สอน+วิธีทำ Line Messaging Api</a><br><a href="https://medium.com/datawiz-th/%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-line-chatbot-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-dialogflow-python-%E0%B9%81%E0%B8%A5%E0%B8%B0-firebase-%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%A1%E0%B8%B2%E0%B8%81%E0%B9%86-c4631c041848">สร้าง Line Chatbot ด้วย Dialogflow, Python, และ Firebase🔥🔥🔥 ง่ายมากๆ!!!</a><br><a href="https://www.mikkipastel.com/online-course-building-line-chatbot-using-dialogflow/">Building LINE Chatbot using DialogFlow</a><br><a href="https://medium.com/linedevth/%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99-dialogflow-%E0%B8%9C%E0%B9%88%E0%B8%B2%E0%B8%99-api-detectintent-c841a96e0701">ใช้งาน Dialogflow ผ่าน API detectIntent</a><br><a href="https://ai-no-tsubasa.blogspot.com/2018/10/use-message-objects-line-on-dialogflow-with-custom-payload.html">วิธีใช้ Message objects เพิ่มลูกเล่นในการตอบกลับของ Line บน Dialogflow ด้วย Custom payload</a><br><a href="https://medium.com/linedevth/line-x-dialogflow-%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-chatbot-line-%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B9%86-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-dialogflow-%E0%B9%81%E0%B8%A5%E0%B8%B0-line-bot-designer-%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B9%80%E0%B8%96%E0%B8%AD%E0%B8%B0-572476c2eacd">[Dialogflow x LINE] สร้าง Chatbot LINE แบบง่ายๆ ด้วย Dialogflow และ LINE Bot Designer กันเถอะ</a><br><a href="https://dialogflow-fulfillment.readthedocs.io/en/latest/api/webhook-client/">Webhook client</a></li>
<li>ข้อมูลอ้างอิงเกี่ยวกับการใช้ Flask<br><a href="https://piravit-chenpittaya.medium.com/flask-%E0%B9%80%E0%B8%A3%E0%B8%B4%E0%B9%88%E0%B8%A1%E0%B8%95%E0%B9%89%E0%B8%99%E0%B9%80%E0%B8%82%E0%B8%B5%E0%B8%A2%E0%B8%99%E0%B9%80%E0%B8%A7%E0%B9%87%E0%B8%9A%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B9%86%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-flask-6eed2ad869ee">Flask — เริ่มต้นเขียนเว็บง่ายๆด้วย Flask</a><br><a href="https://rpa-robot.medium.com/chatbot03-backend-web-service-with-flask-d27db255c66e">Chatbot03 : Backend web service with Flask</a><br><a href="https://medium.com/@chanisarauttamawetin/%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%9A%E0%B8%AD%E0%B8%97%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%82%E0%B8%B5%E0%B8%A2%E0%B8%99-python-%E0%B9%83%E0%B8%8A%E0%B9%89-flask-%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%84%E0%B9%88%E0%B8%B2%E0%B8%88%E0%B8%B2%E0%B8%81-api-%E0%B9%80%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A1%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B8%81%E0%B8%B1%E0%B8%9A-line-api-a4e652a7506a">Line API กับเขียน Python ใช้ Flask รับค่าจาก API</a></li>
<li>ข้อมูลอ้างอิงจาก Youtube<br><a href="https://youtube.com/playlist?list=PLeohJaMRzYHohBzFbKJknovLFmQGwbBS-">Python Line Chatbot</a><br><a href="https://youtu.be/ua1x54x5HOk">Python using JSON web API | EP.1 อัพเดทสถานการณ์ Covid-19 และแจ้งเตือนผ่าน Line Notify</a><br><a href="https://youtu.be/MjoVmZfU6Ws">EP 18 การประยุกต์ใช้ LIFF กับ ริชเมนูและ Line Chat Bot</a><br><a href="https://youtu.be/yEiBeyEASRM">ดึงข้อมูล COVID-19 จาก API ที่ส่งค่ากลับมาเป็น JSON ด้วย Python</a><br><a href="https://youtu.be/auDjKfWMagk">คอร์สเรียน Python REST APIs with Flask สำหรับมือใหม่ (Full Course)</a><br><a href="https://youtu.be/EApp94TCtig">ทดสอบ LINE Chatbot ที่พัฒนาด้วย LINE Messaging API เเบบไม่ต้อง Deploy ขึ้นเซิฟเวอร์&nbsp;</a></li>
</ol>
