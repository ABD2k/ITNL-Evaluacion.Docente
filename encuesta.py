from selenium import webdriver
from selenium.webdriver.support.ui import Select
from random import randint
from time import sleep
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()


print("Autor: Alberto Barrientos Davila")
print("Fecha: 2022-11-02")
user = input("No. Control: ")
contra = input("Contraseña: ")
sleep(5)

driver = webdriver.Chrome()
driver.get("https://itnleon.mindbox.app/login/alumno")
correo = driver.find_element_by_id("ncontrol")
correo.clear()
correo.send_keys(user)
passw = driver.find_element_by_id("password")
passw.clear()
passw.send_keys(contra)
driver.find_element_by_css_selector("button.btn-block").click()
driver.get("https://itnleon.mindbox.app/alumnos/evaluaciones/encuesta-docente/preguntas")
paginas = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div/p/strong").text.replace("Evaluación ","").split(" de ")
print(paginas[0], paginas[1])
paginas[0]=int(paginas[0])
paginas[1]=int(paginas[1])
while(paginas[0]<paginas[1]):
    answer=driver.find_elements_by_xpath("//select[@class='form-control']")
    for i in answer:
        i=Select(i).select_by_value(str(randint(1,5)))
    driver.find_element_by_id("eval").submit()
    sleep(1)
    paginas[0]+=1
#obtener todos los textarea
answer=driver.find_elements_by_xpath("//textarea[@class='form-control']")
for i in answer:
    i.send_keys("Buen profesor :)")
driver.find_element_by_id("eval").submit()
input("Preciona enter para terminar")

print("Terminado Revisa tu cuenta")



