from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import gspread

CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_bin = os.environ.get('OOGLE_CHROME_BIN' 'hromedriver')
options  = webdriver.ChromeOptions()
options.binary_location = chrome_bin
options.add_argument(' -- disable-gpu')
options.add_argument(' -- no-sandbox')
options.add_argument('-- headless')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)


# options = Options()

final = []

# chrome_options = Options()
# chrome_options.add_argument("user-data-dir=selenium")
# driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get("https://www.linkedin.com/in/soham-mhatre/detail/recent-activity/shares/")

activity = driver.find_element_by_class_name('pv-recent-activity-detail__feed-container')
#Post Caption
for post in activity.find_elements_by_class_name("occludable-update"):
    caption = ''
    for text in post.find_element_by_class_name('feed-shared-text').find_elements_by_class_name('break-words'):
        caption+=text.text
#Post Video
    num_video = len(post.find_elements_by_tag_name('video'))
#Post Images
    # res = requests.get("https://www.linkedin.com/in/soham-mhatre/detail/recent-activity/shares/")
    # html_page = res.content
    # soup = BeautifulSoup(html_page, 'html.parser')
    # for div in soup.find_all('div',{'class' : 'ivm-image-view-model'} ):
    #     print("first")
    #     for image in div.find_all("img"):
    #       print(image.get('src'))

    num_images = len(post.find_element_by_class_name("ivm-image-view-model").find_elements_by_tag_name('img'))
    print(post.find_element_by_class_name("ivm-image-view-model").find_elements_by_tag_name('img')[0].get_attribute('src'))
#Post Likes and Comments
    likes,comments = 0,0
    for x in post.find_elements_by_class_name('v-align-middle'):
        if 'Comments' in x.text:
            comments = x.text.split()[0]
        else:
            likes = x.text
    final.append([caption,num_video,num_images,likes,comments])

df = pd.DataFrame(final,columns=['Caption',"num_video","num_images","likes","comments"])
gc = gspread.service_account(filename='client-access.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1F9e3pi0GlBY948PSauL7nRrKc8LaIX0CZVRz9klj3YU/edit#gid=0')

worksheet = sh.get_worksheet(0)
worksheet.update([df.columns.values.tolist()] + df.values.tolist())

i = 1