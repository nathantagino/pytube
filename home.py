import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from pytube import YouTube
import os

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def download_video():
    url = url_video.get("1.0", "end-1c")  
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        default_filename = video_stream.default_filename
        save_path = os.path.join(os.path.expanduser('~'), 'Downloads', default_filename)

        # Abrir uma caixa de diálogo para selecionar o local de salvamento do arquivo
        file = asksaveasfile(initialfile=default_filename, defaultextension=".mp4", initialdir=save_path)
        
        if file:
            video_stream.download(output_path=os.path.dirname(file.name))
            messagebox.showinfo("Download Concluído", "O vídeo foi baixado com sucesso!")
        else:
            messagebox.showinfo("Download Cancelado", "O download foi cancelado pelo usuário.")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante o download:\n\n{e}")

# layout janela
window = tk.Tk()
window.title("Pytube - Downloads de Video")
window.minsize(600, 400)
window.maxsize(600, 400)
logotipo =   PhotoImage(file=r"logotipo.png")
photoimage = logotipo.subsample(2, 2)
logo = Label(master = window, image = photoimage)
logo.place(x=130, y=50)

descricao = tk.Label(master=window, text="LINK do Video:")
descricao.place(x=20, y=180)
url_video = tk.Text(window, height=1, width=45)
url_video.place(x=130, y=180)
btn_download = tk.Button(master=window, text="Download", command=download_video)  
btn_download.place(x=520, y=175)
creditos = tk.Label(master=window, text="Desenvolvido por Nathan Tagino - 2023")
creditos.place(x=200, y=360)
center(window)
window.mainloop()
