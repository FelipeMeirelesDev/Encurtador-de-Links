import tkinter as tk
import pyshorteners

def encurtar():
    encurtador = pyshorteners.Shortener();
    link_encurtado = encurtador.tinyurl.short(link_longo_entrada.get());
    link_curto_saida.insert(0, link_encurtado);

print("Teste");

janela = tk.Tk();
janela.title("Encurtador de Link");
janela.geometry("600x300");

link_longo = tk.Label(janela, text="Link para Encurtar:");
link_longo_entrada = tk.Entry(janela);
link_curto = tk.Label(janela, text="Link Encurtado:");
link_curto_saida = tk.Entry(janela);
link_butao = tk.Button(janela, text="Encurtar", command=encurtar);

link_longo.pack();
link_longo_entrada.pack();
link_curto.pack();
link_curto_saida.pack();
link_butao.pack();


janela.mainloop();

