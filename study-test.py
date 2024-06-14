questions1 = [' נהנה לשרבט תמיד, במחברות שלי יש הרבה תמונות, חיצים עיגולים קווים',
              "זוכר דברים טוב יותר אם אני כותב אותם, גם אם אך אני לא חוזר לעיין בהם.",
              "מנסה לזכור מספר טלפון , על ידי כך שאני מדמיין אותו בראשי.",
              "במהלך בחינה כאשר אני נזכר במידע, אני יכול לראות בדמיון את המחברת עם המידע כתוב בתוכה.",
              "אם אני לא כותב הוראות הגעה למקום מסוים, אני תועה בדרך או מגיע באיחור."]

questions2 = [" לא אוהב להקשיב להוראות או לקרא אותן , אני מעדיף פשוט להתחיל",
              "לומד באופן הטוב ביותר כאשר מראים לי איך לעשות משהו.",
              "זוכר בעיקר דברים שהתנסיתי בהם באופן מעשי.",
              " מעדיף ללמוד מתוך התנסות.",
              "נהנה ללמוד על ידי יצירה ובנייה של דברים"]

questions3 = [" מעדיף לקורא בקול,", " כשאני צריך לזכור מידע, אני משנן זאת שוב ושוב בקול רם וזה עוזר לי לזכור",
              "מבין טוב יותר, אם אני מסביר את החומר לאדם אחר.", " זוכר טוב יותר מה אנשים אומרים ופחות איך הם נראים או מה הם לובשים.",
              "מעדיף לשמוע חדשות ברדיו מאשר לקרא אותם בעיתון."]

answers1 = []
answers2 = []
answers3 = []

for i in range(len(questions1)):
    print(questions1[i])
    value = int(input("1-10-כמה אתה מסכים"))
    answers1.append(value)


for i in range(len(questions2)):
    print(questions2[i])
    value = int(input("1-10-כמה אתה מסכים"))
    answers2.append(value)

for i in range(len(questions3)):
    print(questions3[i])
    value = int(input("1-10-כמה אתה מסכים"))
    answers3.append(value)


print(sum(answers1), sum(answers2), sum(answers3))

sums = [sum(answers1), sum(answers2), sum(answers3)]
print(sorted(sums)[-1])
top = sorted(sums)[-1]
ltype = ""
if top == sum(answers1):
    ltype = "חזותי"
elif top == sum(answers2):
    ltype = "תנועתי"
else:
    ltype = 'שמיעתי'

print(ltype)



