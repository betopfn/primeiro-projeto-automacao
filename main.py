import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_address = 'betinhopfn@gmail.com'
sender_password = 'tqth xeqs ndsg qdno'
receiver_address = 'robertinhopires8@gmail.com'

tabelaVendas = pd.read_excel("Vendas.xlsx")


pd.set_option("display.max_columns", None)


faturamento = tabelaVendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()

quantidade = tabelaVendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()

ticketMedio = (faturamento["Valor Final"] / quantidade["Quantidade"]).to_frame()
ticketMedio = ticketMedio.rename(columns={0: "Ticket Medio"})
print(ticketMedio)


#construindo a mensage, BETOO
html = f'''
<html>
  <head>
    <style>
      table {{
        width: 100%;
        border-collapse: collapse;
      }}
      th, td {{
        padding: 8px 12px;
        border: 1px solid #ddd;
        text-align: center;
      }}
      th {{
        background-color: #f2f2f2;
      }}
      tr:nth-child(even) {{
        background-color: #f9f9f9;
      }}
    </style>
  </head>
  <body>
    <p>Prezados,<br><br>
       Segue o relatório de vendas por cada loja.<br><br>
    </p>
    <h3>Faturamento:</h3>
    {faturamento.to_html(formatters={"Valor Final": "R${:,.2f}".format}, border=0, index=True)}
    <h3>Quantidade vendida:</h3>
    {quantidade.to_html(border=0, index=True)}
    <h3>Ticket médio dos produtos em cada loja:</h3>
    {ticketMedio.to_html(formatters={"Ticket Medio": "R${:,.2f}".format}, border=0, index=True)}
  </body>
</html>
'''


message = MIMEMultipart('alternative')
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = "Relatório de vendas"

##anexando o html que criasse
message.attach(MIMEText(html, 'html'))

# Enviar o e-mail via SMTP
try:
    # Configurações do servidor SMTP (exemplo com Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    #conectando ao server smtp
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()  # Identificar-se com o servidor
    server.starttls()  # Iniciar a conexão segura
    server.ehlo()

    # fazeno login
    server.login(sender_address, sender_password)


    server.sendmail(sender_address, receiver_address, message.as_string())


    server.quit()

    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')