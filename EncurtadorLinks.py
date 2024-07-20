import tkinter as tk

root = tk.Tk();
root.title("Encurtador de Link");
root.geometry("600x300");

longurl_label = tk.Label(root, text="Link para ser Encurtado:");
longurl_entry = tk.Entry(root);
shorturl_label = tk.Label(root, text="Link Encurtado:");
shorturl_entry = tk.Entry(root)
button = tk.Button(root, text="Encurtar");

longurl_label.pack();
longurl_entry.pack();
shorturl_label.pack();
shorturl_entry.pack();
button.pack();

root.mainloop();