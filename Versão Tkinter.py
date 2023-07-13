from tkinter import *
janela = Tk()
janela.title('MERCADO')
janela.geometry('500x500')
janela.configure(background='#020402') 

dici = {}
lista = []

#FUNÇÕES --------------------------------------------

def inserir(): 
    #APAGAR REMOVER
    botao_confirmar_remover.place_forget()
    entry_remoção.place_forget()
    remoção.place_forget()
            
    entry_produto.place(relx=0.5, rely=0.65, anchor=CENTER)
    entry_preço.place(relx=0.5, rely=0.70, anchor=CENTER)
    entry_quantidade.place(relx=0.5, rely=0.75, anchor=CENTER)
        
    #pergunta do lado
    pergunta1.place(relx=0.3, rely=0.65, anchor=CENTER)
    pergunta2.place(relx=0.3, rely=0.70, anchor=CENTER)
    pergunta3.place(relx=0.3, rely=0.75, anchor=CENTER)
    
    botao_confirmar_inserir.place(relx=0.7, rely=0.65, anchor=CENTER)
    botao_verlista.place(relx=0.7, rely=0.75, anchor=CENTER)

    #repostas
    resposta1 = entry_produto.get() 
    resposta2 = float(entry_preço.get()) 
    resposta3 = int(entry_quantidade.get()) 
    
    #total unitário
    tt = resposta2*resposta3
    
    #ADICIONAR dicionário+lista
    lista.append(resposta2)
    lista.append(resposta3)
    lista.append(tt)
    dici[resposta1] = lista[:]
    lista.clear() 
    
    #LIMPAR entry
    entry_produto.delete(0, END)
    entry_preço.delete(0, END)
    entry_quantidade.delete(0, END)
 
def remover():
    #APAGAR INSERIR
    botao_confirmar_inserir.place_forget()
    botao_verlista.place_forget()
    pergunta1.place_forget()
    pergunta2.place_forget()
    pergunta3.place_forget() 
    entry_preço.place_forget()
    entry_produto.place_forget()
    entry_quantidade.place_forget()   
       
    remoção.place(relx=0.3, rely=0.70, anchor=CENTER)
    entry_remoção.place(relx=0.65, rely=0.70, anchor=CENTER)
    botao_confirmar_remover.place(relx=0.83, rely=0.70, anchor=CENTER)
    
    #REMOÇÃO item lista
    resposta4 = entry_remoção.get()
    dici[resposta4] = ['██', '██', '██']
    
    #ATUALIZAR lista
    botao_verlista.place(relx=0.83, rely=0.78, anchor=CENTER)
    
    #LIMPAR entry
    entry_remoção.delete(0, END)

def ver_lista():    
    #LISTA
    #title lista
    espaço6 = Label(janela, text='PRODUTO', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10)) 
    espaço6.place(relx=0.20, rely=0.25, anchor=CENTER)
        
    espaço7 = Label(janela, text='PREÇO', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10)) 
    espaço7.place(relx=0.40, rely=0.25, anchor=CENTER)
        
    espaço8 = Label(janela, text='QUANTIDADE', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10)) 
    espaço8.place(relx=0.60, rely=0.25, anchor=CENTER)
        
    espaço9 = Label(janela, text='TOTAL', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10)) 
    espaço9.place(relx=0.80, rely=0.25, anchor=CENTER)
    
    #lista
    passo = 0
    for k, v in dici.items():
        #condição apagar
        if v[1] == '██':
            produto = Label(janela, text=k, background='#020402')
            produto.place(relx=0.20, rely=0.30+passo, anchor=CENTER)
            
            preço = Label(janela, text=v[0], background='#020402') 
            preço.place(relx=0.40, rely=0.30+passo, anchor=CENTER)
            
            quantidade = Label(janela, text=v[1], background='#020402') 
            quantidade.place(relx=0.60, rely=0.30+passo, anchor=CENTER)
            
            total = Label(janela, text=v[2], background='#020402') 
            total.place(relx=0.80, rely=0.30+passo, anchor=CENTER) 
            passo += 0.05
            #---------------------------------------------------
        else:
            produto = Label(janela, text=k, background='#020402', foreground='#EFFFC8')
            produto.place(relx=0.20, rely=0.30+passo, anchor=CENTER)
            
            preço = Label(janela, text=v[0], background='#020402', foreground='#EFFFC8') 
            preço.place(relx=0.40, rely=0.30+passo, anchor=CENTER)
            
            quantidade = Label(janela, text=v[1], background='#020402', foreground='#EFFFC8') 
            quantidade.place(relx=0.60, rely=0.30+passo, anchor=CENTER)
            
            total = Label(janela, text=v[2], background='#020402', foreground='#EFFFC8') 
            total.place(relx=0.80, rely=0.30+passo, anchor=CENTER) 
            passo += 0.05

def cancelar():
    #APAGAR INSERIR
    botao_confirmar_inserir.place_forget()
    botao_verlista.place_forget()
    pergunta1.place_forget()
    pergunta2.place_forget()
    pergunta3.place_forget() 
    entry_preço.place_forget()
    entry_produto.place_forget()
    entry_quantidade.place_forget()   
   
    #APAGAR REMOVER
    botao_confirmar_remover.place_forget()
    entry_remoção.place_forget()
    remoção.place_forget()
        
    entry_resp_cancelar.place(relx=0.58, rely=0.8, anchor=CENTER) #entry tornar visivél
    pergunta.place(relx=0.25, rely=0.8, anchor=CENTER)
    resposta = entry_resp_cancelar.get() 
    botao_confirmar.place(relx=0.8, rely=0.8, anchor=CENTER)
    
    if resposta == 'S':
        janela.destroy()
        
    if resposta == 'N':
        mensagem.place(relx=0.5, rely=0.85, anchor=CENTER)
        #APAGAR CANCELAR
        entry_resp_cancelar.place_forget()
        botao_confirmar.place_forget()
        pergunta.place_forget()
        mensagem.place_forget()

def pagar():
    #APAGAR CABEÇARIO LISTA
    espaço6.place_forget()
    espaço7.place_forget()
    espaço8.place_forget()
    espaço9.place_forget()
    
    #APAGAR INSERIR
    botao_confirmar_inserir.place_forget()
    botao_verlista.place_forget()
    pergunta1.place_forget()
    pergunta2.place_forget()
    pergunta3.place_forget() 
    entry_preço.place_forget()
    entry_produto.place_forget()
    entry_quantidade.place_forget()   
   
    #APAGAR REMOVER
    botao_confirmar_remover.place_forget()
    entry_remoção.place_forget()
    remoção.place_forget()
    
    #OUTRO APAGAR (mais clean)
    botao_cancelar.place_forget()
    botao_cancelar.place_forget()
    botao_pagar.place_forget()
    
    pg = 0
    for v in dici.values():
        if v[2] != '██':
            pg += v[2]
    pagamento_geral = (f'Valor a ser pago: R$ %.2f'%pg)
        
    valor = Label(janela, text=pagamento_geral, background='#020402', foreground='#EFFFC8')
    valor.place(relx=0.5, rely=0.60, anchor=CENTER)
    
    escolha.place(relx=0.5, rely=0.64, anchor=CENTER)
    
    botao_vista.place(relx=0.34, rely=0.69, anchor=CENTER)
    botao_credito.place(relx=0.6, rely=0.69, anchor=CENTER)
    
    return pg

def vista():
    pg = 0
    for v in dici.values():
        if v[2] != '██':
            pg += v[2]
    desconto = (10*pg)/100
    pg = pg - desconto
    txt_final = (f'O pagamento final com desconto é: R$ %.2f' %pg)
    
    final = Label(janela, text=txt_final, background='#020402', foreground='#EFFFC8')
    final.place(relx=0.5, rely=0.74, anchor=CENTER)
    
    botao_ok.place(relx=0.5, rely=0.8, anchor=CENTER)
         
def credito():
    pg = 0
    for v in dici.values():
        if v[2] != '██':
            pg += v[2]
    desconto = (5*pg)/100
    pg = pg - desconto
    txt_final = (f'O pagamento final com desconto é: R$ %.2f' %pg)
    
    final = Label(janela, text=txt_final, background='#020402', foreground='#EFFFC8')
    final.place(relx=0.5, rely=0.74, anchor=CENTER)
    
    botao_ok.place(relx=0.5, rely=0.8, anchor=CENTER)

def fechar():
    janela.destroy()

#JANELA --------------------------------------------------
title = Label(janela, text='Mercado', background='#020402', foreground='#E2510E', font=('amarillo',15))
title.place(relx=0.5, rely=0.065, anchor=CENTER)

#LISTA --------------------------------------------------
#title lista
espaço6 = Label(janela, text='PRODUTO', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10)) 
espaço6.place(relx=0.20, rely=0.25, anchor=CENTER)
    
espaço7 = Label(janela, text='PREÇO', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10)) 
espaço7.place(relx=0.40, rely=0.25, anchor=CENTER)
    
espaço8 = Label(janela, text='QUANTIDADE', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10)) 
espaço8.place(relx=0.60, rely=0.25, anchor=CENTER)
    
espaço9 = Label(janela, text='TOTAL', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10)) 
espaço9.place(relx=0.80, rely=0.25, anchor=CENTER)

#INSERIR --------------------------------------------------
botao_inserir = Button(janela, text='INSERIR PRODUTO', command=inserir, background='#E2510E', font=('Consola Mono Bold', 10))
botao_inserir.place(relx=0.35, rely=0.15, anchor=CENTER)

pergunta1 = Label(janela, text='Nome do produto:', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10))
pergunta2 = Label(janela, text='Preço unitário:', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10))
pergunta3 = Label(janela, text='Quantidade:', background='#020402', foreground='#EFFFC8', font=('Consola Mono Bold', 10))

entry_produto = Entry(janela, width=10) 
entry_preço = Entry(janela, width=10) 
entry_quantidade = Entry(janela, width=10) 

botao_confirmar_inserir = Button(janela, text='CONFIRMAR', command=inserir, background='#E2510E', font=('Consola Mono Bold', 8)) 

#ATUALIZAR LISTA --------------------------------------------------
botao_verlista = Button(janela, text='ATUALIZAR LISTA', command=ver_lista, background='#E2510E', font=('Consola Mono Bold', 8))    

#REMOVER --------------------------------------------------
botao_remover = Button(janela, text='REMOVER PRODUTO', command=remover, background='#E2510E', font=('Consola Mono Bold', 10))
botao_remover.place(relx=0.65, rely=0.15, anchor=CENTER)

remoção = Label(janela, text='Digite o nome do produto que deseja remover: ', background='#020402', foreground='#EFFFC8')
entry_remoção = Entry(janela, width=13) 
botao_confirmar_remover = Button(janela, text='CONFIRMAR', command=remover, background='#E2510E', font=('Consola Mono Bold', 9)) 

#PAGAR --------------------------------------------------
botao_pagar = Button(janela, text='PAGAR', command=pagar, background='#E2510E', font=('Consola Mono Bold', 10)) 
botao_pagar.place(relx=0.4, rely=0.90, anchor=CENTER)

escolha = Label(janela, text='ESCOLHA A FORMA DE PAGAMENTO', background='#020402', foreground='#EFFFC8')

botao_vista = Button(janela, text='À VISTA 10%', command=vista, background='#E2510E', font=('Consola Mono Bold', 9)) 
botao_credito = Button(janela, text='CARTÃO DE CRÉDITO 5%', command=credito, background='#E2510E', font=('Consola Mono Bold', 9)) 

botao_ok = Button(janela, text='              OK              ', command=fechar, background='#E2510E', font=('Consola Mono Bold', 10))

#CANCELAR --------------------------------------------------
botao_cancelar = Button(janela, text='CANCELAR COMPRA', command=cancelar, background='#E2510E', font=('Consola Mono Bold', 10)) 
botao_cancelar.place(relx=0.60, rely=0.90, anchor=CENTER)

pergunta = Label(janela, text='Tem certeza que deseja cancelar? [S/N]', background='#020402', foreground='#EFFFC8') 

botao_confirmar = Button(janela, text='CONFIRMAR', command=cancelar, background='#E2510E', font=('Consola Mono Bold', 10)) 
entry_resp_cancelar = Entry(janela, width=15) 

mensagem = Label(janela, text='')
mensagem = Label(janela, text='Sentimos muito por não concluir a compra :(')
mensagem = Label(janela, text='Então vamos continuar a compra :)')

janela.mainloop()
