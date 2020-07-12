from selenium import webdriver

driver = webdriver.Chrome(executable_path= r'D:\chromedriver.exe')

driver.get("https://web.whatsapp.com/")


name= input('Enter name of the group or the person: ')

number_of_msgs = int(input("Enter how many messages do you want to send: "))

for i in range(number_of_msgs):


    msg=input('Enter the message that you have to send: ')

    number= int(input('Enter number of messages do you want to send: '))
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()

    msgbox = driver.find_element_by_class_name('_3uMse')

    for i in range(number):
        msgbox.send_keys(msg)
        button = driver.find_elements_by_class_name('_1U1xa')[0]
        button.click()
    
input("Enter any key after scanning any QR code!!!")