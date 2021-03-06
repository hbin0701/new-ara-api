import uuid
import requests
from bs4 import BeautifulSoup as bs

from django.contrib.auth import get_user_model

from apps.core.models import Article
from apps.user.models import UserProfile
from ara.settings import PORTAL_ID, PORTAL_PASSWORD

LOGIN_INFO = {
    'userid': PORTAL_ID,
    'password': PORTAL_PASSWORD
}

BASE_URL = 'https://portal.kaist.ac.kr'


def crawl_all():
    # Session 생성, with 구문 안에서 유지
    with requests.Session() as session:
        login_req = session.post('https://portalsso.kaist.ac.kr/ssoProcess.ps', data=LOGIN_INFO)
        if login_req.status_code != 200:
            raise Exception('login failed')

        main_req = session.get(f'{BASE_URL}/ennotice/today_notice')

        def get_board(page_num):
            board_req = session.get(
                f'{BASE_URL}/board/list.brd?boardId=today_notice&lang_knd=ko&userAgent=Chrome&isMobile=false&page={page_num}&sortColumn=REG_DATIM&sortMethod=DESC')
            soup = bs(board_req.text, 'lxml')
            link = []
            titles = soup.select('table > tbody > tr > td > a')
            for title in titles:
                link.append(title.attrs['href'])

            return link

        def get_article(url):
            article_req = session.get(url)
            soup = bs(article_req.text, 'lxml')
            title = soup.select('table > tbody > tr > td.req_first')[0].contents[0]
            raw = soup.select('table > tbody > tr:nth-child(4) > td')
            writer = soup.select('table > tbody > tr > td > label')[0].contents[0]
            dt = soup.select('table > tbody > tr:nth-child(2) > td:nth-child(4)')[0].contents[0]

            html = ''
            for r in raw:
                html += str(r)

            content_text = ' '.join(bs(html, features='html5lib').find_all(text=True))

            return {
                'title': title,
                'content_text': content_text,
                'content': html,
                'writer': writer,
                'dt': dt,
            }

        links = []
        i = 1
        while True:
            link = get_board(i)
            if link:
                links.extend(link)
                i += 1
            else:
                break

        for link in links:
            board_id = link.split('/')[-2]
            num = link.split('/')[-1]
            full_link = f'{BASE_URL}/board/read.brd?cmd=READ&boardId={board_id}&bltnNo={num}&lang_knd=ko'
            info = get_article(full_link)

            exist = UserProfile.objects.filter(nickname=info['writer'])
            if exist:
                user = exist[0].user
            else:
                user = get_user_model().objects.create(username=str(uuid.uuid1()), is_active=False)
                user_profile = UserProfile.objects.create(
                    is_past=True,
                    user=user,
                    nickname=info['writer'],
                )

            Article.objects.create(
                parent_board_id=1,  # 포탈공지 게시판
                created_at=info['dt'],
                title=info['title'],
                content=info['content'],
                content_text=info['content_text'],
                created_by=user,
                url=full_link,
            )

