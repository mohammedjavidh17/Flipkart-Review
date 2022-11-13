from bs4 import BeautifulSoup
import requests
import pandas as pd

#Data:
Review = pd.DataFrame(columns=['Stars', 'Review1', 'Review', 'Customer', 'Certified', 'Locaition', 'Time'])
print(Review)
#sample Links
link = "https://www.flipkart.com/chama-2021-coco-3c-3x3-speedcube-high-speed-smooth-turning-magic-cube-puzzle-stickerless-brainteaser-game-toy-1-pieces/p/itm014cd1fff6058?pid=PUZG82P7UGAZXDAD&lid=LSTPUZG82P7UGAZXDADBWZ41D&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_76ad1ace-9c8f-425f-8f78-c597753d9b66_11_0QSUNVNUV7Y1_MC.PUZG82P7UGAZXDAD&ppt=hp&ppn=homepage&ssid=izogmiwmnk0000001668335894219&otracker=clp_pmu_v2_Indoor%2BToys_1_11.productCard.PMU_V2_Chama%2B2021%2BCoco%2B3C%2B3x3%2BSpeedCube%2BHigh%2BSpeed%2BSmooth%2BTurning%2BMagic%2BCube%2BPuzzle%2BStickerless%2BBrainteaser%2BGame%2BToy%2B%25281%2BPieces%2529_toysclp-store_PUZG82P7UGAZXDAD_neo%2Fmerchandising_0&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Indoor%2BToys_LIST_productCard_cc_1_NA_view-all&cid=PUZG82P7UGAZXDAD"
#link = "https://www.flipkart.com/sony-zv-e10l-mirrorless-camera-interchangeable-lens-vlog/p/itmaad9258ddded5?pid=DLLG6G8U8P2NGEHG&lid=LSTDLLG6G8U8P2NGEHGGVZNLB&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=hp_omu_Best%2Bof%2BElectronics_4_3.dealCard.OMU_Q5LU1U8PHMK6_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_4_NA_view-all_3&fm=neo%2Fmerchandising&iid=740d8092-e70b-4eab-b283-e0caac347193.DLLG6G8U8P2NGEHG.SEARCH&ppt=hp&ppn=homepage&ssid=7x6bu5bhao0000001668325217866"
#link = "https://www.flipkart.com/canon-eos-m50-mark-ii-mirrorless-camera-ef-m15-45mm-stm-lens/p/itm7a4f536cb1255?pid=DLLGFY7XYG8YFMQT&lid=LSTDLLGFY7XYG8YFMQTSG43XC&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_5&otracker=hp_omu_Best%2Bof%2BElectronics_4_3.dealCard.OMU_Q5LU1U8PHMK6_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_4_NA_view-all_3&fm=neo%2Fmerchandising&iid=740d8092-e70b-4eab-b283-e0caac347193.DLLGFY7XYG8YFMQT.SEARCH&ppt=hp&ppn=homepage&ssid=7x6bu5bhao0000001668325217866"

#Get Review page linkS
root = requests.get(link).text
soup = BeautifulSoup(root, 'lxml')
dta = soup.find(class_ = "col JOpGWq")
temp = [i['href'] for i in dta.find_all('a', href=True)][-1]
rLink = "https://www.flipkart.com"+temp
dta.clear()


#get links of every pages
rt = requests.get(rLink).text
sp = BeautifulSoup(rt, 'lxml')
lnksLst = sp.find('div', class_ = "_2MImiq _1Qnn1K").find_all('a', href = True)
lnks = [i['href'] for i in lnksLst]
lnksLst.clear()

TempList = []
#get review from each page
for Link in lnks:
    Link = "https://www.flipkart.com"+Link
    rtl = requests.get(Link, timeout=10).text
    spl = BeautifulSoup(rtl, 'lxml')
    dta = spl.find_all('div', class_ = "_27M-vq")[1:]
    for x in dta:
        TempList1 = []
        vl = x.find_all('div', class_ = 'row')[0].text
        TempList1.append(vl[0])
        TempList1.append(vl[1:])
        TempList1.append(x.find_all('div', class_ = 'row')[1].text[:-9])
        y = x.find('div', class_ = 'row _3n8db9').find_all('p')
        buf = str(y[1].text).split(',')
        TempList1.append(str(y[0].text))
        try:
            TempList1.append(buf[0])
            TempList1.append(buf[1])
        except:
            TempList1.append('None')
        TempList1.append(str(y[2].text))
        #TempList1.append(str(y[3].text))
        TempList.append(TempList1)
        print("...")

    print("........")
print(pd.DataFrame(TempList, columns=['Stars', 'Review1', 'Review', 'Customer', 'Certified', 'Locaition', 'Time']))

lnks.clear()
