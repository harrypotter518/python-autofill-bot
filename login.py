from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import Select
import numpy as np
import json

with open('data.json') as json_file:
    data = json.load(json_file)

def id_converter(id):
    real_id= id[0:start_pos]+ unique_key +id[id.find('0a'):]
    return real_id

usernameStr = 'dvoryanovalex@outlook.com'
passwordStr = 'Harry20010102'

browser = webdriver.Chrome()
browser.get('https://online.immi.gov.au/lusc/login')

# fill in username and hit the next button

username = browser.find_element_by_id('username')
username.send_keys(usernameStr)
password = browser.find_element_by_id('password')
password.send_keys(passwordStr)
loginButton = browser.find_element_by_name('login')
loginButton.click()

continueButton = browser.find_element_by_name('continue')
continueButton.click()
newappButton = browser.find_element_by_id('btn_newapp')
newappButton.click()

##student vias###

#browser.get(data['url_info']['student_visa_url'])

browser.get("https://online.immi.gov.au/elp/app?action=new&formId=STU-AP-500")

###page1
agreeCheck = browser.find_element_by_tag_name("input[type='checkbox']")
agreeCheck.click()

full_id= agreeCheck.get_attribute("id")

unique_key =full_id[4:full_id.find('0a')]
start_pos=full_id.find(unique_key)

next1Button = browser.find_element_by_id( id_converter(data["page1"]["next1btn"][1]) )
next1Button.click()
#html= browser.page_source

for page_info in data:
    browser.implicitly_wait(500)
    if page_info != "url_info"  and page_info !="page1":
        for title in data[page_info]:
            data_len = len(np.shape(data[page_info][title]))
            if data_len == 1 :
                if data[page_info][title][2] == 0:  ## button ##
                    button = browser.find_element_by_id( id_converter(data[page_info][title][1]) )
                    button.click()
                elif data[page_info][title][2] == 1:  ## input[type="text"] ##
                    inputtext = browser.find_element_by_id( id_converter(data[page_info][title][1]) )
                    inputtext.send_keys(data[page_info][title][0])
                elif data[page_info][title][2] == 2:  ## input[type="radio"] ##
                    inputradio =  browser.find_element_by_xpath("//*[@value='"+ data[page_info][title][0] +"'][@name='"+ id_converter(data[page_info][title][1])+"']")
                    inputradio.click()     
                elif data[page_info][title][2] == 3:    ####select option####
                    browser.implicitly_wait(500)
                    selectoption = Select(browser.find_element_by_id(id_converter(data[page_info][title][1])))
                    selectoption.select_by_visible_text(data[page_info][title][0])
                else:  ####datepicker####
                    inputtext = browser.find_element_by_id( id_converter(data[page_info][title][1]) )
                    inputtext.send_keys(data[page_info][title][0])
            else:
                for i in range(data_len) :
                    if data[page_info][title][i][2] == 0:  ## button ##
                        button = browser.find_element_by_id( id_converter(data[page_info][title][i][1]) )
                        button.click()
                    elif data[page_info][title][i][2] == 1:  ## input[type="text"] ##
                        inputtext = browser.find_element_by_id( id_converter(data[page_info][title][i][1]) )
                        inputtext.send_keys(data[page_info][title][i][0])
                    elif data[page_info][title][i][2] == 2:  ## input[type="radio"] ##
                        inputradio =  browser.find_element_by_xpath("//*[@value='"+ data[page_info][title][i][0] +"'][@name='"+ id_converter(data[page_info][title][i][1])+"']")
                        inputradio.click()     
                    elif data[page_info][title][i][2] == 3:    ####select option####
                        browser.implicitly_wait(500)
                        selectoption = Select(browser.find_element_by_id(id_converter(data[page_info][title][i][1])))
                        selectoption.select_by_visible_text(data[page_info][title][i][0])
                    else:  ####datepicker####
                        inputtext = browser.find_element_by_id( id_converter(data[page_info][title][i][1]) )
                        inputtext.send_keys(data[page_info][title][i][0])

        

        
            



        







