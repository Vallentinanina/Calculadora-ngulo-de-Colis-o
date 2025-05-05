from math import acos, degrees, sqrt
import tkinter as tk
from tkinter import messagebox

def calcular_angulo():
    try:
        vA = float(entry_vA.get())
        aB = float(entry_aB.get())
        y0 = float(entry_y0.get())

        # Cálculo do ângulo
        A = (y0 * aB) / (vA ** 2)
        B = 1
        C = -A
        discriminante = B**2 - 4 * A * C

        if discriminante < 0:
            messagebox.showinfo("Resultado", "Não há colisão possível para os valores informados.")
            return

        cos_theta1 = (-B + sqrt(discriminante)) / (2 * A)
        cos_theta2 = (-B - sqrt(discriminante)) / (2 * A)
        solucoes_validas = [degrees(acos(cos)) for cos in [cos_theta1, cos_theta2] if 0 <= cos <= 1]
        #arrumando a velocidade
        if vA <= 0 or vA > 100:
             messagebox.showinfo("Resultado", "Não há colisão possível para os valores informados.")
             return
         
        if aB <= 0 or aB > 100:
             messagebox.showinfo("Resultado", "Não há colisão possível para os valores informados.")
             return

        if solucoes_validas:
            resultado = f"Ângulo θ para colisão: {solucoes_validas[0]:.2f}°"
            label_resultado.config(text=resultado)
        else:
            messagebox.showinfo("Resultado", "Não há colisão possível para os valores informados.")

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos!")

def reboot():
    """Limpa todos os campos e o resultado."""
    entry_vA.delete(0, tk.END)
    entry_aB.delete(0, tk.END)
    entry_y0.delete(0, tk.END)
    label_resultado.config(text="")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Colisão")
root.geometry("500x450")  # Aumentei a altura para o novo botão
root.configure(bg="#f0f0f0")

# Estilo
fonte = ("Papyrus", 14)
tk.Label(root, text="Calculadora de Ângulo de Colisão", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

# Campos de entrada
tk.Label(root, text="Velocidade da partícula A (m/s):", font=fonte, bg="#f0f0f0").pack()
entry_vA = tk.Entry(root, font=fonte)
entry_vA.pack(pady=5)

tk.Label(root, text="Aceleração da partícula B (m/s²):", font=fonte, bg="#f0f0f0").pack()
entry_aB = tk.Entry(root, font=fonte)
entry_aB.pack(pady=5)

tk.Label(root, text="Posição y inicial da partícula A (m):", font=fonte, bg="#f0f0f0").pack()
entry_y0 = tk.Entry(root, font=fonte)
entry_y0.pack(pady=5)

# Frame para os botões (organização)
frame_botoes = tk.Frame(root, bg="#f0f0f0")
frame_botoes.pack(pady=10)

# Botão de cálculo
btn_calcular = tk.Button(frame_botoes, text="Calcular Ângulo θ", command=calcular_angulo, font=fonte, bg="#4CAF50", fg="black")
btn_calcular.grid(row=0, column=0, padx=5)

# Botão de reboot
btn_reboot = tk.Button(frame_botoes, text="Reiniciar", command=reboot, font=fonte, bg="#f44336", fg="black")
btn_reboot.grid(row=0, column=1, padx=5)

# Exibição do resultado
label_resultado = tk.Label(root, text="", font=("Papyrus", 14, "bold"), bg="#f0f0f0")
label_resultado.pack(pady=10)

root.mainloop()