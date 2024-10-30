import smtplib

pessoaQueEnvia = "betinhopfn@gmail.com"
senha = "tqth xeqs ndsg qdno"
destinatario = "robertinhopires8@gmail.com"
assunto = "fds"
mensagem = "tome no cu"
txt = f"assunto: {assunto}\n\n{mensagem}"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(pessoaQueEnvia, senha)
server.sendmail(pessoaQueEnvia, destinatario, txt)


