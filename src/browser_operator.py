
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import random


def report_leave_school(config, timeout):
    # init the driver
    if config["driver"] == "Chrome":
        driver = webdriver.Chrome()
    elif config["driver"] == "Edge":
        driver = webdriver.Edge()
    else:
        return

    driver.get(url="https://ehall.nuaa.edu.cn/")
    # time.sleep(timeout)
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, 'username')))
    element.send_keys(config["username"])
    # login
    # driver.find_element_by_id("username").send_keys(config["username"])
    driver.find_element_by_id("password").send_keys(config["password"])
    submit = driver.find_element_by_class_name("auth_login_btn")
    submit.click()
    time.sleep(1)
    # time.sleep(timeout)
    # select freedom service
    request_page = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.LINK_TEXT, '疫情防控期学生出校申请/报备')))
    # request_page = driver.find_element_by_link_text("疫情防控期学生出校申请/报备")
    request_page.click()
    time.sleep(timeout)

    # open up the form
    driver.switch_to.window(driver.window_handles[1])
    form_page = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, 'preview_start_button')))
    # form_page = driver.find_element_by_id("preview_start_button")
    form_page.click()
    # time.sleep(timeout)

    ####################### fill in the form ########################

    if "assistant" in config:
        assistant = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/div/div/div/div/input')))
        # assistant = driver.find_element_by_xpath(
        # r'/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/div/div/div/div/input')
        # assistant.click()
        # assistant.send_keys(Keys.BACKSPACE)
        # assistant.send_keys(Keys.BACKSPACE)

        # 清空导员选择
        driver.execute_script(
            'document.querySelector(".xdTableContentRow > td > div > table > tbody > tr:nth-child(4) > td:nth-child(2) > div > div > div > div >input").value="";')

        assistant.send_keys(config["assistant"])
        # time.sleep(timeout)
        new_assistant = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/div/div/div/div/div[1]/div')))
        # new_assistant = driver.find_element_by_xpath(
        #     r'/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/div/div/div/div/div[1]/div')
        new_assistant.click()

    if "supervisor" in config:
        pass
        # teacher = find_form.find_element_by_xpath(r'//tbody/tr[4]/td[4]/div/font/div/div/div/input')
        # teacher.clear()
        # teacher.send_keys('刘哲')
    time.sleep(3)
    temp = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, r'//*[@id="V1_CTRL70"]')))
    # campus = Select(driver.find_element_by_xpath(r'//*[@id="V1_CTRL70"]'))
    campus = Select(temp)
    campus.select_by_visible_text(config["campus"])

    date = driver.find_element_by_xpath(r'//*[@id="V1_CTRL78"]')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    date.clear()
    date.send_keys(config["date"])

    reason = driver.find_element_by_xpath(r'//*[@id="V1_CTRL80"]')
    reason.click()
    reason.clear()
    reason.send_keys(config["reason"])

    kind = driver.find_element_by_xpath(r'//*[@id="V1_CTRL107"]')
    # kind.location_once_scrolled_into_view
    kind.click()

    is_leave = driver.find_element_by_xpath(r'//*[@id="V1_CTRL87"]')
    # is_leave.location_once_scrolled_into_view
    is_leave.click()

    is_return = driver.find_element_by_xpath(r'//*[@id="V1_CTRL88"]')
    # is_return.location_once_scrolled_into_view
    is_return.click()
    time.sleep(1)
    promise = driver.find_element_by_xpath(r'//*[@id="V1_CTRL90"]')
    # ensure.location_once_scrolled_into_view
    promise.click()

    submit_button = driver.find_element_by_xpath(
        r'/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[3]/ul/li[1]/a')
    submit_button.click()

    # time.sleep(timeout)
    final_check = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/button[1]')))

    # final_check = driver.find_element_by_xpath(
    #     r'/html/body/div[7]/div/div[2]/button[1]')
    final_check.click()

    driver.quit()


def health_clockin(config, timeout):
    if config["driver"] == "Chrome":
        driver = webdriver.Chrome()
    elif config["driver"] == "Edge":
        driver = webdriver.Edge()
    else:
        return
    driver.get(url="https://m.nuaa.edu.cn/ncov/wap/default/index")
    # time.sleep(timeout)
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/input')))
    element.send_keys(config["username"])
    # driver.find_element_by_xpath(
    #     "/html/body/div[1]/div[2]/div[1]/input").send_keys(config["username"])

    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/input").send_keys(config["password"])
    submit = driver.find_element_by_class_name("btn")
    submit.click()
    # time.sleep(timeout)
    location = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/section/div[4]/ul/li[9]/div/input')))
    # location = driver.find_element_by_xpath(
    #     '/html/body/div[1]/div/div/section/div[4]/ul/li[9]/div/input')
    location.click()
    time.sleep(timeout)

    submit = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/section/div[5]/div/a')
    submit.click()
    # time.sleep(timeout)
    confirm = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div[2]')))
    # confirm = driver.find_element_by_xpath(
    #     '/html/body/div[4]/div/div[2]/div[2]')
    confirm.click()
    driver.close()
    driver.quit()
