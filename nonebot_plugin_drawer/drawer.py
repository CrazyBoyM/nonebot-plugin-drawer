import asyncio
import httpx
from .config import wenxin_config

# 获取access_token
async def get_token():
  url = "https://wenxin.baidu.com/younger/portal/api/oauth/token?from=baicai"
  async with httpx.AsyncClient(verify=False, timeout=None) as client:
    resp = await client.post(
      url,
      data={
        'grant_type': 'client_credentials',
        'client_id': wenxin_config.wenxin_ak,
        'client_secret': wenxin_config.wenxin_sk
      },
      headers={
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    )
    access_token = resp.json()['data']
    return access_token

# 获取绘画的任务id
async def get_taskId(access_token, text, style):
  url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernievilg/v1/txt2img?from=baicai"
  payload = {
    'access_token': access_token,
    'text': text,
    'style': style,
  } # 请求参数
  async with httpx.AsyncClient(verify=False, timeout=None) as client:
    resp = await client.post(url, data=payload)
    data = resp.json()
    print(data)
    if data['code'] == 0: # 请求成功
      return data['data']['taskId']
    
    print(f'绘画任务失败,返回msg: {data["msg"]}') # 请求失败的消息提示
    return None
    

# 获取绘画的结果
async def get_img(access_token, taskId):
  url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernievilg/v1/getImg?from=baicai"
  payload={
    'access_token': access_token,
    'taskId': taskId
  } # 请求参数，taskId是绘画的任务id
  async with httpx.AsyncClient(verify=False, timeout=None) as client:
    resp = await client.post(url, data=payload)
    data = resp.json()
    print(data)
    if data['code'] == 0: # 请求成功
      if data['data']['status'] == 1: # status为1，表明绘画完成
        return data['data']['imgUrls']
      else:
        # 5s后再次请求
        await asyncio.sleep(5)
        return await get_img(access_token, taskId)
    
    print(f'绘画任务失败,返回msg: {data["msg"]}') # 请求失败的消息提示    
    return None