import pyautogui as py
import time

time.sleep(5)

#Principal
py.hotkey('ctrl', 'shiftleft', 'shiftright', 'right')
py.hotkey('shiftleft', 'shiftright', 'down')
py.hotkey('ctrl', 'd')
time.sleep(1)
py.hotkey('ctrl', 'shiftleft', 'shiftright', 'pagedown')

#Nubank
time.sleep(1)
py.hotkey('shiftleft', 'shiftright', 'down')
py.hotkey('ctrl', 'd')
time.sleep(1)
py.hotkey('ctrl', 'up')
py.hotkey('ctrl', 'c')
for _ in range(4):
    py.hotkey('ctrl', 'shiftleft', 'shiftright', 'pagedown')

#Principal - Atualização Nu
time.sleep(1)
py.press('down')
py.press('enter')
time.sleep(0.5)
py.press('left')
py.hotkey('ctrl', 'shiftleft', 'shiftright', 'left')
py.press('backspace')
time.sleep(0.5)
py.hotkey('ctrl', 'shift', 'v')
time.sleep(0.5)
py.hotkey('ctrl', 'left')
py.press('backspace', presses=3) #tirar o espaço e o cifrão
py.press('right') #dígitos antes do ponto
time.sleep(0.5)
py.press('del')
py.press('enter') 
for _ in range(3):
    py.hotkey('ctrl', 'shiftleft', 'shiftright', 'pagedown')

#Clear
time.sleep(1)
py.hotkey('ctrl', 'c')
time.sleep(1)
for _ in range(2):
    py.hotkey('ctrl', 'shiftleft', 'shiftright', 'pagedown')

#Principal - Atualização Clear
time.sleep(1)
py.press('up')
py.press('right')
py.press('enter')
time.sleep(0.5)
py.press('left')
py.hotkey('ctrl', 'shiftleft', 'shiftright', 'left')
py.press('backspace')
time.sleep(0.5)
py.hotkey('ctrl', 'shift', 'v')
time.sleep(0.5)
py.hotkey('ctrl', 'left')
py.press('backspace', presses=3) #tirar o espaço e o cifrão
py.press('right') #dígitos antes do ponto
time.sleep(0.5)
py.press('del')
py.press('enter') 
for _ in range(2):
    py.hotkey('ctrl', 'shiftleft', 'shiftright', 'pagedown')

#XP
time.sleep(1)
py.hotkey('ctrl', 'shiftleft', 'shiftright', 'right')
py.hotkey('shiftleft', 'shiftright', 'down')
py.hotkey('ctrl', 'd')
time.sleep(1)
py.hotkey('ctrl', 'up')
py.hotkey('ctrl', 'c')
for _ in range(3):
    py.hotkey('ctrl', 'shiftleft', 'shiftright', 'pagedown')

#Principal - Atualização XP
time.sleep(1)
py.press('up')
py.press('right')
py.press('enter')
time.sleep(0.5)
py.press('left')
py.hotkey('ctrl', 'shiftleft', 'shiftright', 'left')
py.press('backspace')
time.sleep(0.5)
py.hotkey('ctrl', 'shift', 'v')
time.sleep(0.5)
py.hotkey('ctrl', 'left')
py.press('backspace', presses=3) #tirar o espaço e o cifrão
py.press('right', presses=2) #dígitos antes do ponto
time.sleep(0.5)
py.press('del')
py.press('enter')
for _ in range(4):
    py.hotkey('ctrl', 'shiftleft', 'shiftright', 'pagedown') 

#Cryptos
time.sleep(1)
py.hotkey('ctrl', 'c')
time.sleep(1)
py.hotkey('ctrl', 'shiftleft', 'shiftright', 'pagedown')

#Principal - Atualização Cryptos
time.sleep(1)
py.press('up')
py.press('right')
py.press('enter')
time.sleep(0.5)
py.press('left')
py.hotkey('ctrl', 'shiftleft', 'shiftright', 'left')
py.press('backspace')
time.sleep(0.5)
py.hotkey('ctrl', 'shift', 'v')
time.sleep(0.5)
py.hotkey('ctrl', 'left')
py.press('backspace', presses=3) #tirar o espaço e o cifrão
py.press('right', presses=2) #dígitos antes do ponto
time.sleep(0.5)
py.press('del')
py.press('enter')

#Atualização %
for _ in range(3):
    py.hotkey('ctrl', 'down')
time.sleep(0.5)
py.hotkey('ctrl', 'shiftleft', 'shiftright', 'left')
py.hotkey('shiftleft', 'shiftright', 'down')
py.hotkey('shiftleft', 'shiftright', 'right')
time.sleep(0.5)
py.hotkey('ctrl', 'd')
time.sleep(0.5)

#Atualização Tabela Gráfico
for _ in range(2):
    py.hotkey('ctrl', 'up')
time.sleep(0.5)
py.hotkey('ctrl', 'shiftleft', 'shiftright', 'left')
py.hotkey('shiftleft', 'shiftright', 'right')
py.hotkey('ctrl', 'c')
time.sleep(0.5)
for _ in range(6):
    py.hotkey('ctrl', 'down')
time.sleep(0.5)
py.press('down')
py.hotkey('ctrl', 'left')
py.press('right')
py.hotkey('ctrl', 'shift', 'v')
py.hotkey('ctrl', 'right')
py.press('right')
py.press('up')
time.sleep(0.5)
py.hotkey('shiftleft', 'shiftright', 'down')
py.hotkey('ctrl', 'd')