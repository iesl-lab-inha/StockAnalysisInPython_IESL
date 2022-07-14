import pandas as pd
krx_list = pd.read_html('C:/Users/hards/Downloads/상장법인목록.xls')
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format) #종목코드 0생략들을 커버함 {:06d]는 여섯자리 숫자형식으로 표현
print(krx_list[0]) #리스트의 첫번째 원소 출력
print('\n')

df = pd.read_html('https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&SearchType=13')[0] #URL을 이요해 인터넷 상 파일 읽기 뒤의 [0]은 결과를 데이터프레임으로 받음
df['종목코드'] = df['종목코드'].map('{:06d}'.format) #마찬가지로 여섯자리 숫자형식으로 표현
df = df.sort_values(by = '종목코드') #오름차순 정렬
print(df)