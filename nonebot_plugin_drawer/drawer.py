import asyncio
import httpx
from .config import wenxin_config

# 获取access_token
async def get_token():
  url = "https://wenxin.baidu.com/younger/portal/api/oauth/token"
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
    return resp.json()['data']

# 获取绘画的任务id
async def get_taskId(access_token, text, style):
  url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernievilg/v1/txt2img"
  payload = {
    'access_token': access_token,
    'text': text,
    'style': style,
  } # 请求参数
  async with httpx.AsyncClient(verify=False, timeout=None) as client:
    resp = await client.post(url, data=payload)
    data = resp.json()
    print(data)
    if resp.json()['code'] == 0: # 请求成功
      return resp.json()['data']['taskId']
    return resp.json()['msg'] # 请求失败

# 获取绘画的结果
async def get_img(access_token, taskId):
  url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernievilg/v1/getImg"
  payload={
    'access_token': access_token,
    'taskId': taskId
  } # 请求参数，taskId是绘画的任务id
  async with httpx.AsyncClient(verify=False, timeout=None) as client:
    resp = await client.post(url, data=payload)
    data = resp.json()
    print(data)
    data = resp.json()['data']
    if resp.json()['code'] == 0: # 请求成功
      if data['status'] == 1: # 绘画完成
        return data['imgUrls']
      else:
        # 10s后再次请求
        await asyncio.sleep(10)
        return await get_img(access_token, taskId)
      
    return resp.json()['msg'] # 请求失败
  