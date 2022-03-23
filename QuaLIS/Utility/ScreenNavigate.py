import time
from configparser import ConfigParser

from selenium.webdriver.common.by import By

from Utility import BasicOperation, LogOperation

baseMaster=ConfigParser()
baseMaster.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementBaseMaster.ini")

auditTrail=ConfigParser()
auditTrail.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementUserManagement.ini")

pin=auditTrail.get("AuditTrail", "pin")

userManagement=auditTrail.get("AuditTrail", "userManagementIcon")

master=auditTrail.get("AuditTrail","masterIcon")

auditTrail=auditTrail.get("AuditTrail", "auditTrailIcon")

def unit(driver):

    try:
        BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "masterIcon"))

        LogOperation.logInfo("clicked the Master icon")
    except:
        LogOperation.logError("Unable to click the Master icon")

    time.sleep(2)

    try:
        element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

        driver.execute_script("arguments[0].scrollIntoView();", element)

        time.sleep(2)

        element.click()

        LogOperation.logInfo("clicked the Base Master icon")
    except:
        LogOperation.logError("Unable to click the Base Master icon")


    time.sleep(2)

    try:

        BasicOperation.scrollClickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitOfMeasurementIcon"))
        LogOperation.logInfo("clicked the unit icon")
    except:

        time.sleep(2)
        try:
            BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitOfMeasurementIcon"))
            LogOperation.logInfo("clicked the unit icon")
        except:
            LogOperation.logError("Unable to click the unit icon")

def auditTrailPreCondition(driver):

    time.sleep(2)

    try:
        BasicOperation.clickXpath(driver, master)

        LogOperation.logInfo("clicked the Master icon")
    except:
        LogOperation.logError("Unable to click the Master icon")



    time.sleep(2)

    try:
        BasicOperation.clickXpath(driver, userManagement)

        LogOperation.logInfo("clicked the User management icon")
    except:
        LogOperation.logError("Unable to click the User management icon")


    time.sleep(2)

    try:
        element = driver.find_element(By.XPATH,
                                      "//a[@href='#/audittrail' and @nformcode='78' and text()='Audit Trail']")

        driver.execute_script("arguments[0].scrollIntoView();", element)

        time.sleep(2)

        element.click()

        LogOperation.logInfo("clicked the Audit trail icon")
    except:
        LogOperation.logError("Unable to click the Audit trail icon")




def auditTrailPostCondition(driver):

    time.sleep(2)
    try:
        element = driver.find_element(By.XPATH, userManagement)

        time.sleep(2)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        time.sleep(2)
        BasicOperation.clickXpath(driver, userManagement)

        LogOperation.logInfo("clicked the User management icon")
    except:
        LogOperation.logError("Unable to click the User management icon")

