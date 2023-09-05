# Bling-Api-V3

Esse script foi desenvolvido para facilitar e obter o Access Token da API V3 do Bling, assim podendo aliviar agilidade do desenvolvimento do seu software.

1° É preciso criar um arquivo texto com as credenciais Client_id e Client_secret e depois informar o caminho para o paramentHeader
<pre>
dados.txt
client_id:bd7865c12ba70b496xxxxxxxbdfb72ca1,
client_secret:28703e2b44bd5408xxxxxxxx43131d5320f58caa606b4a4d459c
</pre>
<pre>
BlingV3().parmentHeader("dados.txt")
</pre>
  
--------------------------------

2° Informar ao paramentro paramentCode o code da url em formato String
<pre>
BlingV3().paramentCode("82972ca43131d5320f58xxxxxx")
</pre>
--------------------------------

3° Devesse criar um variavel que ira obter objeto com Access Token
<pre>
listObject = BlingV3().tokenApi()
</pre>
<pre>
{'access_token': '8ee52a9xxxxxxxaf28810ed9', 'expires_in': 21600, 'token_type': 'Bearer', 'scope': '9xx08 98xx9 98x0 9x313 9xx14 98xx5 1xxxxx4 57xx04 156xxx2 5xxxx6 6631498 106xxxx10 1xxxx097 199xxxx9 20xxxx821 2206xxx74 3xxx7553 3182xxx56 3xxx57559 31xx565 318xxx570 3182xxx76 3xxxx5 363xxx90 363xx591 3xxx167 3xxxx3556 363953706 79158xxxx 87xxxxx881 164xxxx4 178xxxxxx11 18xxx35257 58xxxx180 623xxx327 13xxx012976 13645xx97 13645xxx998', 'refresh_token': 'cf9783bxxxxxc1df0d914dab2'}
</pre>
Além disso, sera gerado um arquivo credential e dentro tera um arquivo .txt com todos os dados da requisição.

----------------------------------

4° Caso queira solicitar um novo Access token atraves do Refresh Toke
devera criar um objeto que recebe os novos parametro.
<pre>
BlingV3().parmentHeader('dados.txt')
listObj = BlingV3().refreshToken("cf9783b3a3c960xxxxxxxx0d914dab2")
</pre>
Será atualizado tambem o arquivo .txt contendo os dados da requisição

------------------------------------------------------------------------------------
<br>
<br>

<h2>Exemplo Access Token</h2>
<pre>
BlingV3().paramentHeader('/home/matheus/Documents/Api/dados.txt')
BlingV3().paramentCode('3b3a3c960xxxxxxxx0d914dab2')
listObject = BlingV3().tokenApi()
</pre>

--------------------------------
<br>
<br>

<h2>Exemplo Refresh Token</h2>
<pre>
BlingV3().paramentHeader('/home/matheus/Documents/Api/dados.txt')
listObject = BlingV3().refreshToken('3b3a3c960xxxxxxxx0d914dab2')
</pre>

-------------------------------
