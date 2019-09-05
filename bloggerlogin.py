from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import getpass       

print ('////////////////////////////////////////////////////////')
print ('              AutoPost Blogger V1.0               ')
print ('////////////////////////////////////////////////////////')
a= input('Ingrese su usuario: ')
b = getpass.getpass(prompt= 'Contraseña: ')

driver = webdriver.Chrome() 
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.blogger.com%2Fhome&ltmpl=blogger&service=blogger&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

email = driver.find_element_by_xpath("//input[@name='identifier']")
email.clear()
email.send_keys(a)
emailsiguiente = driver.find_element_by_id("identifierNext")
emailsiguiente.click() 
driver.implicitly_wait(10) # seconds

passa = driver.find_element_by_name("password")
passa.send_keys(b)
contrasiguiente = driver.find_element_by_id("passwordNext")
contrasiguiente.click()

driver.implicitly_wait(10) # seconds
driver.execute_script("alert('AutoPost Blogger V1.0 by UltraDiego');")