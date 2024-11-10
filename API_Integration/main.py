import requests
import os

# 環境変数からGitHubトークンを取得
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKENが設定されていません。環境変数を確認してください。")

# APIエンドポイント
url = "https://api.github.com/user"

# ヘッダー情報
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_user_info():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        print("ユーザー名:", user_data.get('login'))
        print("名前:", user_data.get('name'))
        print("公開リポジトリ数:", user_data.get('public_repos'))
        print("フォロワー数:", user_data.get('followers'))
        print("フォロー中数:", user_data.get('following'))
        print("所在地:", user_data.get('location'))
        print("プロフィールURL:", user_data.get('html_url'))
    else:
        print("エラー:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    get_user_info()
