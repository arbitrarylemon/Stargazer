import win32com.client
import time
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("%{TAB}") 
time.sleep(1)
shell.SendKeys("<script>alert{(}'hi'{)}</script>")
time.sleep(1)
shell.SendKeys("{ENTER}")

