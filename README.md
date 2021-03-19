# Magic8GamePython
Building Magic8ball game in Python using socket and threading.

Inspired from : https://magic-8ball.com/

## Requirement
Python

## Setup
Untuk menjalankan aplikasi:
- Pertama jalankan server.py dengan ```python server.py {IPaddress}``` default port(8080) jika ingin menjalankan di port lain silahkan menjalankan dengan ```python server.py {IPaddress} -p{port}```
Contoh : python server.py 127.0.0.1 atau python server.py 127.0.0.1 -p 8081
- Lalu jalankan client.py dengan ```python client.py {IPaddress}``` default port(8080) jika ingin menjalankan di port lain silahkan menjalankan dengan ```python client.py {IPaddress} -p{port}```
Contoh : python client.py 127.0.0.1 atau python client.py 127.0.0.1 -p 8081
- untuk bantuan silahkan mengetik ```python client.py atau server.py -h```
- Pastikan port dan hostIP antara client dan server sama.

## Penjelasan App
Cara menjalankan App : 
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
