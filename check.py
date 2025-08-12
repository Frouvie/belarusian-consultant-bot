from g4f.client import Client


FORMAT = '''
На вход поступает строка, содержащая только название ВУЗа.
1. Если ВУЗ белорусский, верни строго by.
2. Если ВУЗ иностранный, верни строго en.
3. Если строка не содержит названия ВУЗа, верни строго error.
4. Не добавляй никаких других символов, текста или пояснений.
'''

client = Client()


def check(name: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": FORMAT
            },
            {
                "role": "user",
                "content": name
            }
        ],
        web_search=False
    )

    return response.choices[0].message.content