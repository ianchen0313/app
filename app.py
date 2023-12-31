import streamlit as st
import pickle
import pandas as pd
import sklearn

# initialize section
with open('trained_model', 'rb') as f:
    model = pickle.load(f)
    
def setup_quesion(title='title'):
    value = st.radio(title,['無','有'], horizontal=True, key=title)
    if value == '無':
        value = 0
    else:
        value = 1 
    return value

def predict():
    features = pd.DataFrame({
    '是否有高血壓':[high_blood_pressure],
    '是否有高血脂':[high_blood_oil], 
    '是否有糖尿病':[high_blood_sugar], 
    '是否有骨質疏鬆症':[bone_lack], 
    '是否有肝臟疾病':[liver_problem],  
    '是否有子宮卵巢疾病':[womon_proble],
    '是否關節疼痛':[joint_pain], 
    '是否下背部疼痛或腰痛':[back_pain], 
    '是否坐骨神經痛':[sit_pain], 
    '是否頭痛或偏頭痛':[head_pain], 
    '是否痛風':[gout], 
    '是否使用慢性處方籤':[longterm_drug],
    '是否曾吸菸':[smoke], 
    '年齡':[age]})
    result = model.predict(features)[0]
    if result:
        st.write('你被診斷有腎臟病')
        health_info()
        hospital(region)
        
    else:
        st.write('你被診斷為沒有腎臟病')
        health_info()
            
def health_info():
    st.text("""
    衛教
    1.運動：
    (1)有氧運動：一周3~5天，一天20~60分鐘，如游泳、騎腳踏車、走路
    (2)阻力運動：一周2~3天，一組10~15反覆，要練習到8~10種肌群，如彈力帶、機器
    2.飲食：
    (1)注意鈉、蛋白、脂肪含量。選擇低飽和脂肪，反式脂肪，膽固醇，鹽(鈉)和添加糖的食物
    (2)避免醃漬類食品、避免罐頭、冷凍食品等加工食品
    (3)不吃高鹽高脂速食如漢堡、炸雞、鹹酥雞、披薩、泡麵、火鍋、滷味
    (4)每天飲食限鹽少於2,300毫克
    (5)限蛋白飲食
    (6)低鉀、低磷飲食(大部分包裝食品或飲料都含有磷)
    *推薦甜品選擇：愛玉、仙草、粉粿等食用前添加少量蜂蜜；果凍、粉圓、西谷米、涼圓
    *推薦食物選擇：炒冬粉、水晶餃、地瓜
    *小心高磷食物：麵筋、毛豆、蠶豆、花生、杏仁、巧克力、碳酸飲料、奶製品
    *小心高鉀食物：低鈉或薄鹽醬油（因減少的鈉會由鉀代替，鉀易過高）、高湯、果汁、香蕉、香瓜、榴槤，奇異果、草莓、柑橘、咖啡、茶、運動飲料、堅果類、巧克力、梅子汁、蕃茄醬，九層塔、木耳、菠菜、空心菜、海帶
    *小心高鈉食物：各種醃製食品，如：醬菜、豆腐乳、肉鬆、麵線、鹽、味增、沙茶醬、烏醋、蕃茄醬、豆瓣醬等調味料，蘇打餅乾、培根、熱狗、香腸、芹菜、菠菜、罐頭食品、汽水
                    """)

def hospital(region):
    lookup_table = {
        '基隆市':[('基隆長庚','https://www.cgmh.org.tw/tw/Services/DeptInfo/2/21000/21500'),
                 ('基隆醫院', 'https://www.kln.mohw.gov.tw/?aid=51&pid=114')],
        '台北市':[('台北醫院', 'https://www.tph.mohw.gov.tw/?aid=51&pid=7'),
                 ('台北馬偕', 'https://www.mmh.org.tw/departmain.php?id=4')],
        '新北市':[('土城醫院', 'https://www.cgmh.org.tw/tw/Services/DeptInfo/V/V1000/V1500'),
                 ('亞東醫院', 'https://www.femh.org.tw/doctor/doctor?t=2')],
        '桃園市':[('桃園榮總', 'https://www.tyvh.gov.tw/team/'),
                 ('桃園醫院', 'https://www.tygh.mohw.gov.tw/?aid=51&pid=132')],
        '新竹縣':[('台大醫院新竹分院', 'https://www.hch.gov.tw/?aid=51&pid=8'),
                 ('中國醫藥大學新竹附設醫院', 'https://www.cmu-hch.cmu.edu.tw/Doctor/Department?detail=7&current=1&source=dep')],
        '新竹市':[('新竹馬偕', 'https://www.hc.mmh.org.tw/departmain.php?depid=4#staff'),
                 ('國軍桃園總醫院新竹分院', 'https://813.mnd.gov.tw/department/sn5/')],
        '苗栗縣':[('苗栗醫院', 'https://www.mil.mohw.gov.tw/?aid=51&pid=51')],
        '台中市':[('台中榮總','https://www.vghtc.gov.tw/APIPage/DoctorInfoList?WebMenuID=dc264319-1d78-4ad8-a7ba-647440dbad6b&SECTION_ID=NEPH&SECTION=%E8%85%8E%E8%87%9F%E7%97%85%E7%A7%91'),
                 ('台中慈濟醫院','https://taichungsub.tzuchi.com.tw/12/doctors')],
        '彰化縣':[('彰化基督教醫院', 'https://www.cch.org.tw/NEPHRO/'),
                 ('彰化醫院', 'https://www.chhw.mohw.gov.tw/?aid=51&pid=31')],
        '雲林縣':[('台大醫院雲林分院', 'https://www.ylh.gov.tw/?aid=51&pid=35'),
                 ('雲林基督教醫院', 'https://yl.cch.org.tw/doctor_1_detial.aspx?cID=74&key=0105')],
        '嘉義縣':[('朴子醫院', 'https://www.puzih.mohw.gov.tw/?aid=51&pid=41&page_name=list&pageNo=2'),
                 ('嘉義長庚', 'https://www.cgmh.org.tw/tw/Systems/AreaInfo/9')],
        '嘉義市':[('嘉義醫院', 'https://www.chyi.mohw.gov.tw/list.asp?orcaid={850945D1-5D12-4D84-AE32-8C8B0E26D923}'),
                 ('台中榮總嘉義分院', 'https://www.vhcy.gov.tw/PageView/RowView?WebMenuID=25cadfcc-5a2d-4b5b-a1b5-eb11cbb21f7b')],
        '台南市':[('台南醫院', 'https://www.tnhosp.mohw.gov.tw/list.asp?orcaid={850945D1-5D12-4D84-AE32-8C8B0E26D923}'),
                 ('奇美醫院', 'http://sub.chimei.org.tw/57340/index.php/members/')],
        '高雄市':[('高雄醫學大學附設醫院', 'https://www.kmuh.org.tw/KMUHInterWeb/InterWeb/InnerPage/1001124056'),
                 ('高雄榮總', 'https://org.vghks.gov.tw/neph/')],
        '屏東縣':[('屏東醫院', 'https://www.pntn.mohw.gov.tw/?aid=51&pid=90'),
                 ('屏東榮總', 'https://org.ptvgh.gov.tw/nephro/')],
        '南投縣':[('竹山秀傳醫院', 'https://www.csshow.org.tw/new_cssummary/cssummary_04_01_08.asp'),
                 ('南投醫院', 'https://www.nant.mohw.gov.tw/?aid=51&pid=63')],
        '宜蘭縣':[('陽明交通大學附設醫院', 'https://www.hosp.nycu.edu.tw/departments/health-care/internal/kidney/member.html'),
                 ('羅東博愛醫院', 'https://www.pohai.org.tw/doctor.php?Class1=7&Class2=17&Sort=2#sidebar_2')],
        
        '花蓮縣':[('花蓮醫院', 'https://webreg.hwln.mohw.gov.tw/OINetReg.WebRwd/Reg/Dept'),
                 ('花蓮慈濟醫院', 'https://hlm.tzuchi.com.tw/neph/')],
        '台東縣':[('台東醫院', 'https://www.tait.mohw.gov.tw/?aid=51&pid=41&page_name=detail&iid=659'),
                 ('台東馬偕', 'https://ttw3.mmh.org.tw/departmain.php?id=4')],
        '金門縣':[('金門醫院', 'https://netreg.kmhp.mohw.gov.tw/OINetReg.WebRwd/')],
        '澎湖縣':[('三軍總醫院澎湖分院', 'https://wwwv.tsgh.ndmctsgh.edu.tw/Docdetaillist/195/40123/25218'),
                 ('澎湖醫院', 'https://www.pngh.mohw.gov.tw/?aid=51&pid=41')],
        '連江縣':[('連江縣立醫院', 'https://ljc.matsuh.gov.tw/OINetReg/OINetReg.Reg/Reg_NetReg.aspx')]}

    data = lookup_table[region]
    st.write('以下是在您地區的醫院')
    for i, (name, ref) in enumerate(data,1):
        st.markdown(f"{i}.[{name}]({ref})")


# app section
st.title('問卷快篩')
region = st.selectbox('您目前居住在哪裡',
                      ['基隆市','台北市','新北市','桃園市','新竹縣','新竹市','苗栗縣','台中市',
                       '彰化縣','雲林縣','嘉義縣','嘉義市','台南市','高雄市','屏東縣','南投縣'
                       '宜蘭縣','花蓮縣','台東縣','金門縣','澎湖縣','連江縣'])
age = st.number_input('您目前的年齡',
                      min_value=1,max_value=100,value=20)


high_blood_pressure = setup_quesion('您是否有高血壓')
high_blood_sugar = setup_quesion('您是否有糖尿病')
high_blood_oil = setup_quesion('您是否有高血脂')
bone_lack = setup_quesion('您是否有骨質疏鬆')
liver_problem = setup_quesion('您是否有肝臟疾病')
womon_proble = setup_quesion('您是否有子宮卵巢疾病(男性填無)')
joint_pain = setup_quesion('您是否關節疼痛')
back_pain = setup_quesion('您是否有下背部疼痛或是腰痛')
sit_pain = setup_quesion('您是否有坐骨神經痛')
head_pain = setup_quesion('您是否有是否頭痛或偏頭痛')
gout = setup_quesion('您是否有痛風')
longterm_drug = setup_quesion('您是否有使用慢性處方籤')
smoke = setup_quesion('您是否有吸菸')



if st.button('Predict'):
    result = predict()

