import requests
import bs4
from .models import City

def data2database():
    TripAdvisorMumbaiHotelURL = "https://www.tripadvisor.in/Hotels-g304554-Mumbai_Maharashtra-Hotels.html"

    # Add -oa30-(before mumbai) for next page

    data = {'Mumbai': {'Hotels': []}}


    def getText(rev, rat):
        o = {}
        o["Text"] = rev.text
        o["Rating"] = rat['class'][1][-2]
        return o


    res = requests.get(TripAdvisorMumbaiHotelURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    reviewList = soup.find_all('a', class_='review_count')
    HotelNames = soup.find_all('a', class_='prominent')

    for i in range(0, len(HotelNames)):
        d = {'Name': HotelNames[i].text}
        data['Mumbai']['Hotels'].append(d)

    print(data['Mumbai']['Hotels'])
    for i in range(0, 25):#len(reviewList)):
        hotelUrl = reviewList[i]['href']
        print(hotelUrl)
        res1 = requests.get("https://www.tripadvisor.in"+hotelUrl)
        res1.raise_for_status()
        newSoup = bs4.BeautifulSoup(res1.text, "lxml")
        maxPage = int(newSoup.find('div', class_="pageNumbers").findAll(
            "a", recursive="false")[-1].text)
        data['Mumbai']['Hotels'][i]["Reviews"] = []
        for page in range(0, 5):#maxPage):
            if(page == 0):
                pageNoURL = "https://www.tripadvisor.in"+hotelUrl
            else:
                index = hotelUrl.find(
                    '-Reviews-')
                pageNoURL = "https://www.tripadvisor.in" + \
                    hotelUrl[:index]+'-or' + str(page*5) + hotelUrl[index:]
            reviewPage = requests.get(pageNoURL)
            res.raise_for_status()
            reviewSoup = bs4.BeautifulSoup(reviewPage.text, "lxml")
            if(page == 0):
                desc = reviewSoup.find("div", class_="cPQsENeY")
                data['Mumbai']['Hotels'][i]['Description'] = desc.text
            reviews = reviewSoup.find_all('q',
                                          class_='location-review-review-list-parts-ExpandableReview__reviewText--gOmRC')
            ratings = reviewSoup.find('div', {"id": "component_12"}).find_all(
                'span', class_="ui_bubble_rating")

            dic = list(map(getText, reviews, ratings))

            data['Mumbai']['Hotels'][i]["Reviews"].extend(dic)
    print(data)
    for city,i in data.items():
        c = City(name=city,hotels=i['Hotels'],places={})
        c.save()
