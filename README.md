# Web Scraping IDEB

O IDEB é o Índice de Desenvolvimento da Educação Básica na qual é um indicador criado pelo governo federal para medir a qualidade do ensino nas escolas públicas.
O Web Scraping abaixo retorna automáticamente as informações de uma determinada escola públlica de acordo com o seu código.

1) Para executar o Web Scraping primeiro saiba o código da escola pública que se deseja obter informações.

2) Você irá precisar do Python instalado em sua máquina. Caso não tenha-o faça download em: https://www.python.org/downloads/.

3) Instale o Python em sua máquina. Em caso de dúvidas consulte: https://python.org.br/instalacao-windows/

4) Após instalar o Python abra o seu Cmd/Power Shell em caso de Windows ou Prompt Comando no caso de linux, e execute os comandos (um por vez) abaixo no terminal para instalar as bibliotecas necessárias para execução do robô:
  * <i>pip install pandas</i>
  * <i>pip install lxml</i>
  * <i>pip install beautifulsoup4</i>
  * <i>pip install selenium</i>
  * <i>pip install webdriver-manager</i>

5) Edite o arquivo <b>webscraping.py</b> em seu editor de texto de preferencia. Substitua <i>"codigo_escola"</i> pelo numero do código da escola que voce deseja obter informações e salve o arquivo.

6) Para executar o robô abra seu Cmd/Power Shell ou Prompt Comando navegue até aonde se encontra o arquivo <i>webscraping.py</i> e então digite: <b> python ./webscraping.py </b>

7) Após o robô abrir o navegador e coletar as informações será criado um arquivo chamado <b> dataBase.csv </b> na qual você poderá abrir no Excel ou Power BI ou qualquer outro leitor de CSV.

