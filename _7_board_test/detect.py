# detect_save.py  — 결과를 파일에 저장
alerts = [
    {"level": 12, "ip": "1.1.1.1"},
    {"level": 9,  "ip": "2.2.2.2"},
    {"level": 5,  "ip": "3.3.3.3"},
]

def severity(level):
    if level >= 10: return "High"
    if level >= 7:  return "Medium"
    return "Low"

with open("result.txt", "w", encoding="utf-8") as f:
    for a in alerts:
        line = f'{a["ip"]} → {severity(a["level"])}'
        print(line)          # 화면에도 출력
        f.write(line + "\n") # 파일에도 저장

print("result.txt 저장 완료")