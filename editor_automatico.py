import pyautogui
import time

#abrir o arquivos
pyautogui.alert('Não mexa em nada')
pyautogui.PAUSE = 0.9
pyautogui.press('win')
pyautogui.write('Explorador de Arquivos')
pyautogui.press('Enter')
time.sleep(1)
pyautogui.moveTo(676,133)
pyautogui.click()


#Area de Trabalho Win+d
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('Enter')
pyautogui.moveTo(385,284)
#pyautogui.mouseInfo()
pyautogui.rightClick()
pyautogui.moveTo(485,190)
pyautogui.click()
pyautogui.write('Teste01')
pyautogui.press('Enter')
pyautogui.moveTo(385,284)
pyautogui.doubleClick()
