from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)

id_ = 'thgreatseo@gmail.com'
password = 'sendlettert0them'

title = "TEST"
content = '''이것은 편지 보내기 프로그램의 TEST입니다.
이 편지가 무사히 보내진다면 앞으로 다양한 사람들이 이 계정을 사용하게 될 수 있으므로 보내는 실질적 사람이 '서재현'이 아닐 수 있습니다.
또한 뉴스 같은 내용을 크롤링하여 대량 발송할 수 있으므로 원치 않는다면 편지로 알려주세요.
건승을 빕니다.'''

# url에 접근한다.
driver.get('https://www.thecamp.or.kr/pcws/common/loginView.do')
driver.find_element_by_name('loginUserId').send_keys(id_)
driver.find_element_by_name('loginUserPassword').send_keys(password)

driver.find_element_by_xpath("//div[@class='input_4']/button").click()

driver.find_element_by_xpath("//div[@id='leftMyGroupListDiv']/a[@class='present_selected']").click()
driver.find_element_by_xpath("//div[@id='leftMyGroupSelectDiv']/a[@group_id='934'][@unit_code='6142027'][@school_type='1']").click()

# 위문편지
driver.find_element_by_xpath("//a[@menu_id='201']/img[@alt='위문편지 쓰기']").click()

# 제목, 내용 입력
driver.find_element_by_xpath("//input[@class='letter_post_foot'][@id='title']").send_keys(title)
driver.find_element_by_xpath("//textarea[@id='contents']").send_keys(content)

# 전송
driver.find_element_by_xpath("//div[@class='post_btn']/button[@id='btnWrite']").click()
driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']").find_element_by_tag_name('button').click()
driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button")click()
