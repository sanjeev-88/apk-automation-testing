import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

cap = {
    "appium:deviceName": "emulator-5554",
    "platformName": "android",
    "appium:appActivity": "com.atg.world.activity.SplashActivity",
    "appium:appWaitDuration": "50000",
    "appium:appExecTimeout": "50000",
    "appium:appPackage": "com.ATG.World",
    "appium:noReset": True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', cap)
time.sleep(2)

# step 1: Grant Storage and Media Permission
try:
    el1 = driver.find_element(by=AppiumBy.ID, value="com.android.packageinstaller:id/permission_allow_button")
    el1.click()                     #click Allow Button
    time.sleep(1)
    print('Permission to Access Media Given')
except:
    print('Permission granted already')

logIn = 'Pass'
# step 2:Log Into the app
try:
    el1 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/getStartedTv")
    el1.click()                         #Click Get Started Button
    time.sleep(1)
    el2 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/login_email")
    el2.click()                         #Click Sign In Button
    time.sleep(1)
    el3 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/email_phone_login")
    el3.send_keys("hello@atg.world")    #Typing Email Address
    time.sleep(2)
    el7 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/signinbutton")
    el7.click()                         #Click Next Button
    time.sleep(2)
    el3 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/password")
    el3.send_keys("Pass@123")           #Typing Password
    time.sleep(2)
    el6 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/passwordloginbutton")
    el6.click()                         #Click Log In Button
    time.sleep(2)
    print('Log In Sucessful')
except:
    print('Already Logged In')


# step 3:If 'Got It' Button Shows Up Press It
try:
    el1 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/btnGotit")
    el1.click()                         #Click Got It Button
    print('"Got It" Button Showed Up')
except:
    print('"Got It" Button did not show up')


# step 4:Go to Post Option and Select Image
try:
    el2 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/fab")
    el2.click()                             #Click Fab Button at the corner
    el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView")
    el3.click()                             #Click Image Button
    time.sleep(2)
except:
    logIn = 'Failed'
    print('login Unsuccessful (Invalid ID or Password)')


if logIn != 'Failed':
    # step 5:Select 1st Image
    try:
        el3 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/image_cell")
        el3.click()                         #Click 1st Image
        el4 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/toolbar_post_action")
        el4.click()                         #Click Next Button
        el5 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/caption_edit_text")
        el5.send_keys("Test Image")         #Type Post Caption
    except:
        print('No Image Present')


    # step 6:Hit Post
    try:
        el6 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]")
        el6.click()                         #Click Post Button
        time.sleep(5)
        el7 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/selection_done_btn")
        el7.click()                         #Click Done Button
        time.sleep(5)
    except:
        print('Skip post button')


    # step 7:Go Back To Home Page
    driver.back()                       #Go Back To Home Page
    time.sleep(1)


    # step 8:If 'Got It' Button Shows Up Press It
    try:
        el1 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/btnGotit")
        el1.click()                         #Click Got It Button
        print('"Got It" Button Showed Up')
    except:
        print('"Got It" Button did not show up')


    # step 9:Checking Post In My Posts
    el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"Profile\"]/android.widget.FrameLayout/android.widget.ImageView")
    el1.click()                         #Click Profile
    time.sleep(1)
    el2 = driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/myPostsLabelTextView")
    el2.click()                         #Click My Posts