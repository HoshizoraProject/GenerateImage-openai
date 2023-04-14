# GenerateImage
透過 OpenAI API 進行自然語言敘述產生圖片

## Python 使用上的基礎範例
### 主要呼叫程序
`gimage.py` 

```python
import subprocess

# 定義輸入內容
input = "要產生圖片的文字敘述"

# 執行子程序
proc = subprocess.run(['python3', 'gimage.py', f'--message="{input}"'],
                          stdout=subprocess.PIPE)
if (proc.returncode != 0):
    print("執行 gimage.py 發生異常!")
    return

image_url = proc.stdout.decode("utf-8")

print(image_url)
```

## Required
[OpenAI](https://pypi.org/project/openai/)

## Reference
[OpenAI API DALL·E](https://platform.openai.com/docs/guides/images)

## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
