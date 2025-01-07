import streamlit as st
import requests
import pandas as pd

# Streamlit page setup
st.set_page_config(page_title="Real Estate Listings Viewer", layout="wide")
st.title("Real Estate Listings from Pages 1 to 10")
st.markdown("This page fetches and displays real estate listings from pages 1 to 10 using the Naver Real Estate API.")

# Define the cookies and headers as provided
cookies = { 'NNB': '3HAWHHPJWHYGM',
    'ASID': '0d7d3eea000001921d91da9a0000005a',
    '_fwb': '61t8ZH4ydAsPMVIFAXv6dj.1727151714434',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '61t8ZH4ydAsPMVIFAXv6dj.1727151714434',
    'NaverSuggestPlus': 'unuse',
    'BNB_FINANCE_HOME_TOOLTIP_PAYMENT': 'true',
    'NV_WETR_LAST_ACCESS_RGN_M': '"MDkxNDA1NDA="',
    'NV_WETR_LOCATION_RGN_M': '"MDkxNDA1NDA="',
    'NaverSuggestUse': 'unuse%26unuse',
    'wcs_bt': '4f99b5681ce60:1733369889',
    '_ga': 'GA1.2.1765370731.1728275446',
    '_ga_EFBDNNF91G': 'GS1.1.1733906175.1.1.1733906218.0.0.0',
    'nid_inf': '70638033',
    'NID_AUT': 'ieNJMxOs2xMSY5bNHTVC18q5BwyPzs4YsFHbGdajlI0Ji+VwXe2PggbZH5HcVK1r',
    'NID_JKL': 'JgDkvZC2kaW2NnXQyDZl4+Hk8Juno7qLnQHMJV2S4Gw=',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    'NAC': 'VaQrBcgduaFl',
    'NACT': '1',
    'page_uid': 'i3yMylqo1aVssPPtWMVssssstCl-177934',
    'NID_SES': 'AAABtHh7xbqZVZxY5lL8cQGWMOHCKqzPnAHg+gGMdH27LcGJPzhnv8Xm3HKaGswNE41082ZXhLsUK0c/fNzi5bsb1XpkjhbOMRQa/UFRqLBxR4PZ3IRhHnrxyb9XriEOkRN6gxDJnKwP94JQE6THnSzeopxjbLpHu/bQkCSoUiRo5EGAYD1TGBGrrbde2A0ih6Em72vxgyxGkehoIVVrT+3EYkl5Qeu+C2l2Z84tH++4LxJtDggbN32ln0UXFnxiL+jf63sUJX3rakNio/fWDkd1xpLHGqDFMjOel4ndOl0UJQhqoM0GAii7T3gvaU2EEAVY0AJtok7ZkG0Af4q7S0rfzgEUouDzIRXhWPJRb/NgMuH0G/flhDoFELvgC2QwHZXa7g6KY1Yj8vTzbafbdD9CYp9HpTv2JtnsvEmf0ReqU0AxGwLWDvTE+1yhqM02wIGZPwQ2ohhCVRvgHTuXdyRHUbmhOjghbrm2sRmFMtkm3URSAkHvdxZSr0GdhAxZKyveSrtsUae3tMdhrT6uagHBKh7mbvmKs4EYb73QRx+fIl54b/fSgj0ryhhzmYYclF6Q3t0K6EkZN4AolYiN/PC7k1k=',
    'SRT30': '1736221013',
    'realestate.beta.lastclick.cortar': '1100000000',
    'BUC': 'kKFXU5z9J7feF-KxXFX1yNdSF_swrhgor5k3y6_RSp4=',
    'REALESTATE': 'Tue%20Jan%2007%202025%2013%3A25%3A34%20GMT%2B0900%20(Korean%20Standard%20Time)',}
headers = { 'accept': '*/*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MzYyMjM5MzQsImV4cCI6MTczNjIzNDczNH0.Tw2YuOz_UUVr8YNNKGQWgTdQ8ZML5Sq9zvKpsPQQpOI',
    # 'cookie': 'NNB=3HAWHHPJWHYGM; ASID=0d7d3eea000001921d91da9a0000005a; _fwb=61t8ZH4ydAsPMVIFAXv6dj.1727151714434; landHomeFlashUseYn=Y; _fwb=61t8ZH4ydAsPMVIFAXv6dj.1727151714434; NaverSuggestPlus=unuse; BNB_FINANCE_HOME_TOOLTIP_PAYMENT=true; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDA1NDA="; NV_WETR_LOCATION_RGN_M="MDkxNDA1NDA="; NaverSuggestUse=unuse%26unuse; wcs_bt=4f99b5681ce60:1733369889; _ga=GA1.2.1765370731.1728275446; _ga_EFBDNNF91G=GS1.1.1733906175.1.1.1733906218.0.0.0; nid_inf=70638033; NID_AUT=ieNJMxOs2xMSY5bNHTVC18q5BwyPzs4YsFHbGdajlI0Ji+VwXe2PggbZH5HcVK1r; NID_JKL=JgDkvZC2kaW2NnXQyDZl4+Hk8Juno7qLnQHMJV2S4Gw=; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; NAC=VaQrBcgduaFl; NACT=1; page_uid=i3yMylqo1aVssPPtWMVssssstCl-177934; NID_SES=AAABtHh7xbqZVZxY5lL8cQGWMOHCKqzPnAHg+gGMdH27LcGJPzhnv8Xm3HKaGswNE41082ZXhLsUK0c/fNzi5bsb1XpkjhbOMRQa/UFRqLBxR4PZ3IRhHnrxyb9XriEOkRN6gxDJnKwP94JQE6THnSzeopxjbLpHu/bQkCSoUiRo5EGAYD1TGBGrrbde2A0ih6Em72vxgyxGkehoIVVrT+3EYkl5Qeu+C2l2Z84tH++4LxJtDggbN32ln0UXFnxiL+jf63sUJX3rakNio/fWDkd1xpLHGqDFMjOel4ndOl0UJQhqoM0GAii7T3gvaU2EEAVY0AJtok7ZkG0Af4q7S0rfzgEUouDzIRXhWPJRb/NgMuH0G/flhDoFELvgC2QwHZXa7g6KY1Yj8vTzbafbdD9CYp9HpTv2JtnsvEmf0ReqU0AxGwLWDvTE+1yhqM02wIGZPwQ2ohhCVRvgHTuXdyRHUbmhOjghbrm2sRmFMtkm3URSAkHvdxZSr0GdhAxZKyveSrtsUae3tMdhrT6uagHBKh7mbvmKs4EYb73QRx+fIl54b/fSgj0ryhhzmYYclF6Q3t0K6EkZN4AolYiN/PC7k1k=; SRT30=1736221013; realestate.beta.lastclick.cortar=1100000000; BUC=kKFXU5z9J7feF-KxXFX1yNdSF_swrhgor5k3y6_RSp4=; REALESTATE=Tue%20Jan%2007%202025%2013%3A25%3A34%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/110938?ms=37.5478511,127.014318,17&a=APT:PRE:ABYG:JGC&e=RETAIL&ad=true',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',}

# Function to get data from the API for pages 1 to 10
@st.cache_data
def fetch_all_data():
    all_articles = []
    for page in range(1, 11):
        try:
            # Make the request for the specific page
            url = f'https://new.land.naver.com/api/articles/complex/111515?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount=300&maxHouseHoldCount&showArticle=false&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page={page}&complexNo=111515&buildingNos=&areaNos=&type=list&order=prc'
            response = requests.get(url, cookies=cookies, headers=headers)

            # Verify response is valid JSON
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articleList", [])
                all_articles.extend(articles)
            else:
                st.warning(f"Failed to retrieve data for page {page}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
        except ValueError:
            st.error(f"Non-JSON response for page {page}.")

    return all_articles

# Fetch data for all pages
data = fetch_all_data()

# Transform data into a DataFrame if data is available
if data:
    df = pd.DataFrame(data)
    # Select columns to display
    df_display = df[["articleNo", "articleName", "realEstateTypeName", "tradeTypeName", "floorInfo",
                     "dealOrWarrantPrc", "areaName", "direction", "articleConfirmYmd", "articleFeatureDesc",
                     "tagList", "buildingName", "sameAddrMaxPrc", "sameAddrMinPrc", "realtorName"]]

    # Display the table in Streamlit with a clean, readable layout
    st.write("### Real Estate Listings - Pages 1 to 10")
    st.dataframe(df_display)
else:
    st.write("No data available.")
