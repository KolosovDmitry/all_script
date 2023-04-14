
import pandas as pd
import requests
import json

def main():
    region_list = ['08','30','34','23','61','91','92']
    reestr_new_list = []
    url = f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/erz/main/filter'
    for region in region_list:
        params = (
            ('offset' , 0),
            ('limit' , 1000),
            ('sortField' , 'devShortNm'),
            ('sortType' , 'asc'),
            ('region' , region)

        )
        response = requests.get(url, params=params)
        reestr = response.json()
        reestr = reestr['data']['developers']
        
        
        df = pd.DataFrame(reestr)
        print(df)
        dfs = df[['devFullCleanNm','devInn','devKpp','devOgrn','regRegionDesc','devLegalAddr','devOrgRegRegionCd','devPhoneNum','devEmail','devEmplMainFullNm','developerGroupName','companyGroupId']]
        columns = {
                'devFullCleanNm' : 'Полное наименование', 
                'regRegionDesc' : 'Регион',
                'devPhoneNum' : 'Телефон',
                'devEmail' : 'E-mail',
                'devInn' : 'ИНН',
                'devOgrn' : 'ОГРН',
                'devKpp' : 'КПП',
                'devLegalAddr' : 'Адрес',
                'devOrgRegRegionCd' : 'Код региона',
                'devEmplMainFullNm' : 'Руководитель компании',
                'developerGroupName' : 'Группа компаний',
                'companyGroupId' : 'ID Группа компаний'
            }
        dfs.rename(columns = columns, inplace = True)
        print(dfs)
        dfs.to_excel(f'Застройщики ЮГ_{region}.xlsx')
    



if __name__ == '__main__':
    main()