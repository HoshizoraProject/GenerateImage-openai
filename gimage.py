import os, sys, getopt, json
import configparser
import openai

# 定義 OpenAI GPT 請求
def generate_response(prompt: str, size: str):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=size
    )

    # 使用 stderr 顯示回應內容
    print(json.dumps(response), file=sys.stderr)

    return response['data'][0]['url']

def main(argv):
    # 從設定檔讀取資料
    cf = configparser.ConfigParser()
    cf.read("settings.config")

    # 嘗試取得輸入參數
    try:
        opts, args = getopt.getopt(argv,"hps:",["prompt=", "size="])
    except getopt.GetoptError:
        print('gimage.py -p <prompt> -s <size>[256x256|512x512|1024x1024]')
        sys.exit(2)

    size = "256x256"
    for opt, arg in opts:
        if opt == '-h':
            print('gimage.py -p <prompt> -s <size>[256x256|512x512|1024x1024]')
            sys.exit(0)
        elif opt in ("-p", "--prompt"):
            prompt: str = arg
        elif opt in ("-s", "--size"):
            size: str = arg

    # 設定 OpenAI 參數
    openai.api_key = cf.get("openai", "OPENAI_API_KEY")
    openai.organization = cf.get("openai", "OPENAI_ORGANIZATION_ID")

    # 取得請求結果
    response = ""
    try:
        response = generate_response(prompt, size)
    # 發生錯誤直接跳離程序
    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)
    
    # CLI 輸出圖形網址
    print(response, end='')

if __name__ == "__main__":
   main(sys.argv[1:])