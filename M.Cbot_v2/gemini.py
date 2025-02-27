from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

def aiai(text):
    client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
    response = client.models.generate_content(model="gemini-2.0-flash",contents=text + "; 단, 400자 이내, 말을 시작할 때는 ...을 붙여 그리고 서술형으로 말 끝을 음슴체로 알려줘.")
    answer = response.text
    print(answer)
    return answer

if __name__=="__main__":
    aiai("gpt에 대해 설명해")