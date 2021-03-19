# Magic8GamePython
Building Magic8ball game in Python using socket and threading.

Inspired from : https://magic-8ball.com/

## Requirement
Python

## Setup
Untuk menjalankan aplikasi:
- Pertama jalankan server.js dengan ```python server.js {hostIP}``` default port(8080) jika ingin menjalankan di port lain silahkan menjalankan dengan ```python server.js {hostIP} -p{port}```
- Lalu jalankan client.js dengan ```python client.js {hostIP}``` default port(8080) jika ingin menjalankan di port lain silahkan menjalankan dengan ```python client.js {hostIP} -p{port}```
- untuk bantuan silahkan mengetik ```python client.js atau server.js -h```

## Penjelasan App
-Pada awal masuk anda akan diminta untuk mengisi pertanyaan yang anda ingin tau jawabannya
-Kemudian nanti server akan memberikan jawaban dari pertanyaan yang anda berikat

List Jawaban :
["It is certain","Without a doubt","You may rely on it","Yes definitely","It is decidedly so","As I see it, yes","Most likely","Yes","Outlook good","Signs point to yes","Reply hazy try again","Better not tell you now","Ask again later","Cannot predict now","Concentrate and ask again","Don't count on it","Outlook not so good","My sources say no","Very doubtful","My reply is no"]
Sumber Jawaban : https://en.wikipedia.org/wiki/Magic_8-Ball

## Library:
- socket
- threading
- argparse
- os
- random
