questions=[
    ["Q(1). What is the Capital of Bihar ?","Gaya","Buxur","Patna","Muzaffarpur",3],
    ["Q(2). Who is the Chief minister of Bihar ?","Lalu Yadav ","Nitish kumar","sushil modi","Pawan singh",2],
    ["Q(3). Maximum chance of theift in Bihar is of ?","Money","shop","docs","Bridge",4],
    ["Q(4). What is famous in UttarPradesh ?","burfy","Kaju katli","Samosa","Jalebi",3],
    ["Q(5). What is the medicine of cancer ?","PCM","covishield","khaini","Yoga",3],
    ["Q(6). Which phrase is used with Bhang ?","Dhatura","Bhosda","Vala","Bhola",2],
    ["Q(7). Who can beat world's top two percent scientist ?","Premjeet","Saket","Mayank","Manda",2],
    ["Q(8). Who can destroy the world ?","JCB","kim jong1","Baldev","shyam lal",3],
    ["Q(9). Most lazy JANwAr in india","sloth","Keshav","Atul","Banmali dubey",2],
    ["Q(10). Who is the Director of Nit Patna ?","Johnny sins","Lallan singh","Gyani","Bur-man",2],
]
levels=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
money=0
for i in range(0,len(questions)):
    sawal=questions[i]
    print(f"question for Rs.{levels[i]} :\n")
    prashn=sawal[0]
    print(prashn)
    print(f"1. {sawal[1]}            2.{sawal[2]}")
    print(f"3. {sawal[3]}            4.{sawal[4]}")
    reply=int(input("Enter the correct option in the range of (1,4):"))
    if(reply==sawal[-1]):
        print(f"\nCongratulation !!... You have won Rs.{levels[i]}\n")
        money=levels[i]
    else:
        print(f"Sorry !! Ghar Jaeye \n  Right option is {sawal[-1]}")
        break    
print(f"You bring home {money}")