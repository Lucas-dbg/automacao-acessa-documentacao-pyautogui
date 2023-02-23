import pyautogui 
from time import sleep

# Clica no ícone do chrome
pyautogui.click(728,740, duration=1)

# Clica na barra de pesquisa
pyautogui.click(322,53, duration=0.3)

# clica na barra de pesquisa do google
pyautogui.click(521,410, duration=0.3)

# insere o testo que será pesquisado
pyautogui.write("Documentação pyautogui")

# precionar enter 
pyautogui.press('enter')

# Clicar no link da documentação
pyautogui.click(367,398, duration=0.3)

