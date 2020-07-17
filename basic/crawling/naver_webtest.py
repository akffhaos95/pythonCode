# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os, sys, urllib.request, json, datetime, time

def cineBoxInfo():
    #naver
    client_id = "clientid"
    client_secret = "clientsecret"
    movieDate = time.strftime('%Y%m%d', time.localtime(time.time()))
    encText = urllib.parse.quote("어벤져스")
    #for i in range(1, 1000, 100):
        #url = "https://openapi.naver.com/v1/search/blog?display=100&start=%s&query=%s"%(i,encText) # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        #url = "https://openapi.naver.com/v1/search/movie.json?query=%s"%(encText)
    #movie api
    key = 'movie_key'
    movie = []
    for day in range(0, 1):
        datetime_obj = datetime.datetime.strptime(movieDate, "%Y%m%d").date()
        # targetDt = '202007'+str(day).zfill(2)
        url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=%s&targetDt=%s"%(key, datetime_obj)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            #print(response_body.decode('utf-8'))
            result = json.loads(response_body.decode('utf-8'))
            for i in result['boxOfficeResult']['dailyBoxOfficeList']:
                i['day'] = targetDt
                movie.append(i)
            #     print(i)
            # dic = {}
            # for i in result['items']:
            #     dic[i['title'].replace('<b>','').replace('</b>','')] = i['userRating']
        else:
            print("Error Code:" + rescode)
    print(movie)
