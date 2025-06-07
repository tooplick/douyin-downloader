#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from apiproxy.douyin import douyin_headers
from apiproxy.common.utils import Utils
from apiproxy.douyin.urls import Urls

def test_single_video_api():
    """测试单个视频API"""

    # 测试用的aweme_id（从搜索结果中找到的真实ID）
    test_aweme_id = "7065264218437717285"  # 这是搜索结果中提到的真实ID

    urls = Urls()
    utils_instance = Utils()

    print(f"🔍 测试单个视频API")
    print(f"📹 视频ID: {test_aweme_id}")

    # 尝试不同的参数组合
    test_cases = [
        # 基础参数
        f'aweme_id={test_aweme_id}&device_platform=webapp&aid=6383',
        # 添加更多参数
        f'aweme_id={test_aweme_id}&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400',
        # 完整参数
        f'aweme_id={test_aweme_id}&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Mac&os_version=10.15.7&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&update_version_code=170400'
    ]

    for i, detail_params in enumerate(test_cases, 1):
        print(f"\n🧪 测试用例 {i}:")
        print(f"📋 参数: {detail_params[:100]}...")

        # 生成X-Bogus
        jx_url = urls.POST_DETAIL + utils_instance.getXbogus(detail_params)

        test_api_request(jx_url, f"测试用例{i}")

def test_api_request(jx_url, test_name):
    """测试API请求"""

    print(f"🌐 {test_name} 请求URL: {jx_url[:100]}...")

    try:
        # 发送请求
        response = requests.get(url=jx_url, headers=douyin_headers, timeout=10)

        print(f"📊 HTTP状态码: {response.status_code}")
        print(f"📏 响应长度: {len(response.text)}")

        if response.status_code == 200:
            if len(response.text) == 0:
                print(f"❌ 空响应")
                return False

            try:
                datadict = json.loads(response.text)
                print(f"✅ JSON解析成功")
                print(f"📝 响应状态码: {datadict.get('status_code', 'None')}")
                print(f"📝 响应消息: {datadict.get('status_msg', 'None')}")
                print(f"📝 可用字段: {list(datadict.keys())}")

                if datadict.get('status_code') == 0:
                    if 'aweme_detail' in datadict:
                        print(f"🎉 {test_name} 成功获取视频详情!")
                        aweme_detail = datadict['aweme_detail']
                        print(f"📹 视频标题: {aweme_detail.get('desc', 'N/A')}")
                        print(f"👤 作者: {aweme_detail.get('author', {}).get('nickname', 'N/A')}")
                        return True
                    else:
                        print(f"❌ 响应中缺少aweme_detail字段")
                        return False
                else:
                    print(f"❌ API返回错误: {datadict.get('status_msg', '未知错误')}")
                    return False

            except json.JSONDecodeError as e:
                print(f"❌ JSON解析失败: {str(e)}")
                print(f"📄 响应内容前200字符: {response.text[:200]}")
                return False
        else:
            print(f"❌ HTTP请求失败: {response.status_code}")
            print(f"📄 响应内容: {response.text[:200]}")
            return False

    except Exception as e:
        print(f"❌ 请求异常: {str(e)}")
        return False

if __name__ == "__main__":
    test_single_video_api()
