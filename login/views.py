from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from .forms import UserForm, RegisterForm
import hashlib
import requests
import json
import os
import random
import time

import http.client
import urllib
import random



def index(request):
    '''
    if not request.session.get('is_login', None):
        # 如果本来就未登录， 也就没有登出一说
        return redirect('/login/login')
    '''
    return render(request, 'login/index_bq.html')

def to_picture(request):
    nums = ['https://img-1259017984.cos.ap-nanjing.myqcloud.com/image/'+str(i)+'.jpg' for i in range(20,131)]
    return render(request,'login/pic.html', {'nums': nums})

def to_pubg(request):
    return render(request,'toPage/pubg.html')

def query_pubg(request):
    if request.method == 'POST':
        username = request.POST['username']
        f = open(os.path.dirname(__file__) + '/pubg_api_key.txt','r')
        api_key = f.read()
        f.close()
        url = 'https://api.pubg.com/shards/steam/'
        header = {"Authorization": 'Bearer '+api_key,
                  "Accept": "application/vnd.api+json"
                }
        player_url = url + 'players?filter[playerNames]=' + username
        #player_url = url + 'players/fanc_c/seasons/lifetime'
        r = requests.get(player_url, headers=header)
        if r.status_code == 200:
            res = 'Successfully Connected!'
        else:
            res = '用户名不存在！\nFailed to Connect!'
            return render(request, 'toPage/pubg.html', {'data': res})
        player_stat = json.loads(r.text)
        #print(json.dumps(player_stat,sort_keys=False,indent=4))
        accountID = player_stat['data'][0]['id']
        account_url = url + 'players/%s/seasons/lifetime' % accountID
        r = requests.get(account_url, headers=header)
        if r.status_code == 200:
            res = 'Successfully Connected!(acountID)'
            res = json.loads(r.text)
            attributes =  res['data']['attributes']
            bestRankPoint = attributes['bestRankPoint']
            gameModeStats = attributes['gameModeStats']
            #双排
            duo = gameModeStats['duo']
            duo_fpp = gameModeStats['duo-fpp']
            #单排
            solo = gameModeStats['solo']
            solo_fpp = gameModeStats['solo-fpp']
            #四排
            squad = gameModeStats['squad']
            squad_fpp = gameModeStats['squad-fpp']

        else:
            res = '查询失败！\nFailed to Connect!(acountID)'
    return render(request, 'toPage/pubginfo.html', {'data': duo})

def to_video(request):
    return render(request,'toPage/video.html')

def to_BallPool(request):
    return render(request,'toPage/BallPool.html')

def to_dnf(request):
    #equ = get_equ()
    with open(os.path.dirname(__file__) + '/equ.json','r',encoding='gbk')as f:
        equ = eval(f.read())
    for i in equ:
        imgurl = []
        j = []
        for i in range(1,21):
            j.append('https://img-1259017984.cos.ap-nanjing.myqcloud.com/dnf/装备/%d.gif' %i)
            if i % 5 == 0:
                imgurl.append(j)
                j = []
    return render(request,'toPage/dnf.html',{'imgurl':imgurl, 'equ':equ})

def to_draw(request):
    return render(request, 'toPage/live.txt')

def draw(request):
    if request.method == 'POST':
        #获取请求参数
        pic = request.FILES.get('upPic','')
        import os
        print(os.getcwd())
        if not os.path.exists('pic'):
            os.mkdir('pic')
        #拼接路径
        with open(os.path.join(os.getcwd(),'pic',pic.name),'wb') as fw:
            im = pic.read() #一次性读取文件到内存
            fw.write(im)
        #分块读取，性能高
        
            # for ck in pic.chunks():
            #     fw.write(ck)
        import paddlehub as hub
        import cv2
        model = hub.Module(name="animegan_v2_hayao_99")
        image = cv2.imread(os.path.join(os.getcwd(),'pic',pic.name))
        image = image.transpose((2, 0, 1))
        result = model.style_transfer(images=[image],visualization=True)
        return render(request,'toPage/draw.html',{'upURL':os.path.join(os.getcwd(),'pic',pic.name), 'downURL':result[0]['path']})
        
        #return HttpResponse('It is post request,上传成功')
    else:
        return HttpResponse('It is not post and get request!')

def poetry(request):
    if request.method == 'GET':
        return render(request, 'toPage/poetry.html',{'text':'', 'res':['']})
    elif request.method == 'POST':
        text = request.POST['text']
        import requests
        import json
        # 发送HTTP请求
        
        data = {'texts':[text],
                'use_gpu':False, 'beam_width':5}
        headers = {"Content-type": "application/json"}
        url = "http://127.0.0.1:8866/predict/ernie_gen_poetry"
        r = requests.post(url=url, headers=headers, data=json.dumps(data))
        # 保存结果
        results = r.json()["results"]
        if results:
            res = results
        else:
            res = r.json()
        return render(request,'toPage/poetry.html',{'text':text, 'res':res})
        
def submit1(request):
    if request.POST:
        zyx = request.POST.get("zyx")
    return render(request,'toPage/dnf.html',{'careers':zyx})

def show_video(request):
    if request.POST:
        url = request.POST['url']
        video_url = '/video/12.mp4'
    return render(request, 'login/index.html', {'video_url': video_url})

#翻译转换
def translate_(fromLang, toLang, q):
    if q:
        appid = '20201230000659637'  # 填写你的appid
        secretKey = 'jc2uIslzscbLoQtTNY4z'  # 填写你的密钥
        
        httpClient = None
        myurl = '/api/trans/vip/translate'
        
        #fromLang = 'auto'   #原文语种
        #toLang = 'zh'   #译文语种
        #salt = random.randint(32768, 65536)
        salt = time.time()
        #q = '苹果皮'
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
        
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            print (result['trans_result'][0]['dst'])
            res = result['trans_result'][0]['dst']
        
        except Exception as e:
            print (e)
            res = None
        finally:
            if httpClient:
                httpClient.close()
            return res

def main(q):
    language = {'zh' : '中文',
                'en' : '英语',
                'yue' : '粤语',
                'wyw' : '文言文',
                'jp' : '日语',
                'kor' : '韩语',
                'fra' : '法语',
                'spa' : '西班牙语',
                'th' : '泰语',
                'ara' : '阿拉伯语',
                'ru' : '俄语',
                'pt' : '葡萄牙语',
                'de' : '德语',
                'it' : '意大利语',
                'el' : '希腊语',
                'nl' : '荷兰语',
                'pl' : '波兰语',
                'bul' : '保加利亚语',
                'est' : '爱沙尼亚语',
                'dan' : '丹麦语',
                'fin' : '芬兰语',
                'cs' : '捷克语',
                'rom' : '罗马尼亚语',
                'slo' : '斯洛文尼亚语',
                'swe' : '瑞典语',
                'hu' : '匈牙利语',
                'cht' : '繁体中文',
                'vie' : '越南语',
                }
    use_lang_lis = [0] + [random.randint(1, len(language)-1) for i in range(5)] + [0]
    keys = list(language.keys())
    values = list(language.values())

    #q = '在气候变暖和城市化进程加快的背景下,城市暴雨洪涝灾害变得日益剧烈和频繁,给全世界尤其是中国造成了巨大的经济损失。随着第三届世界减灾大会的召开以及联合国减灾署《2015-2030年仙台减轻灾害风险框架》的制定,各国政府已充分意识到降低灾害风险与制定科学防灾减灾规划的重要性。全面了解城市暴雨洪涝灾害的经济影响是开展灾害应急管理和制定有效防灾减灾策略的重要组成部分,现已成为气象灾害研究领域的热点和难点。在经济一体化深入发展的背景下,产业部门之间的关联性日益加深。'
    for i in range(len(use_lang_lis)-1):
        result = q
        if result:
            print(values[use_lang_lis[i+1]])
            q = translate_(keys[use_lang_lis[i]], keys[use_lang_lis[i+1]], result)
            time.sleep(1)
    
    return q
        
def to_translate(request):
    return render(request,'toPage/translate.html')

def translate(request):
    if request.method == 'POST':
        i = request.POST['usertext']
        res = main(i)
    return render(request, 'toPage/translate.html', {'data': res, 'text':i})

def login(request):
    request.session['is_login'] = True
    return redirect('/login/')
    '''
    if request.session.get('is_login', None):   # 不允许重复登录
        return redirect('/login/')  # 之前登录过，直接登录
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():  # 确保用户名和密码都不为空
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多其他验证
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = User.objects.get(name=username)
            except Exception:
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/login/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())
    '''

def register(request):
    if request.session.get('is_login', None):
        return redirect('/login/')

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = '请检查填写的内容! '
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:
                    message = '用户已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return  render(request, 'login/register.html', locals())

                new_user = User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录， 也就没有登出一说
        return redirect('/login/login')
    request.session.flush()  # 删除当前session
    return HttpResponseRedirect('/login/login')

def hash_code(s, salt='mysit'): # 加盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())   # update方法只接收bytes类型
    return h.hexdigest()