import webbrowser




def takers():
    import phonenumbers
    from phonenumbers import geocoder
    from phonenumbers import carrier
    from phonenumbers import timezone

    numbers=input("enter your number:")

    country_name=phonenumbers.parse(numbers)
    print(geocoder.country_name_for_number(country_name,"en"))

    sim=phonenumbers.parse(numbers)
    print(carrier.name_for_number(sim,"en"))

    aria=phonenumbers.parse(numbers)
    print(timezone.time_zones_for_number(aria))

def namta():
    numbers=int(input("number:"))
    count=1
    while count<=10:
        print(numbers,"X",count,"=",numbers*count)
        count+=1
def word_print():
    ss=input("ki print korta caw:")
    nn=int(input("koto bar:"))
    n=1

    while n<=nn:
        print(ss)
        n+=1


def MSAA():
    while True:
        user_input = input()
        if user_input in ["hi" and "hello"]:
            print("hello,how are you?\n...........how can i help you?")
        elif user_input in ["what is your name?"]:
            print("my name is alif")
        elif user_input in ["namta"]:
            print(namta())
        elif user_input in ["song"]:
            print("1.Bangla\n2.hindi")
            select=input("select:")
            if select in "1":
                print("1.রঙে রঙে রঙিন হব\n2. আমার গরুর গাড়ীতে\n3.তোমাকে চাই\n4.গা চুয়ে বোলো")
                select=input("1/2/3/4...?")
                if select in "1":
                    webbrowser.open("https://www.youtube.com/watch?v=Un2xfFZPsio&list=RDRjgFMccglsA&index=14")
                elif select in "2":
                    webbrowser.open("https://www.youtube.com/watch?v=61l74K5ZRdA&list=RDRjgFMccglsA&index=13")
                elif select in "3":
                    webbrowser.open("https://www.youtube.com/watch?v=JAP_Acr8jUM&list=RDRjgFMccglsA&index=12")
                elif select in "4":
                    webbrowser.open("https://www.youtube.com/watch?v=3-sTFakVb1g&list=RDRjgFMccglsA&index=11")

                else:
                    print("error")


            elif select in "2":
                print("1.Kahani Suno\n2.Ye Dil Kyu Toda\n3.Raataan Lambiyan\n4.Galti")
                select=input("1/2/3/4...?")
                if select in "1":
                    webbrowser.open("https://www.youtube.com/watch?v=0Wt6C_EzLls&list=RD0Wt6C_EzLls&index=1")
                elif select in "2":
                    webbrowser.open("https://www.youtube.com/watch?v=lsLQb4t_t9o&list=RD0Wt6C_EzLls&index=2")
                elif select in "3":
                    webbrowser.open("https://www.youtube.com/watch?v=orYf6VDtj_k&list=RD0Wt6C_EzLls&index=6")
                elif select in "4":
                    webbrowser.open("https://www.youtube.com/watch?v=1MSEYp-hSv4&list=RD0Wt6C_EzLls&index=7")

                else:
                    print("error")

        elif user_input in ["weather"]:
            webbrowser.open("https://www.msn.com/en-xl/weather/forecast/in-Chattogram,Bangladesh?loc=eyJyIjoiQ2hhdHRvZ3JhbSIsImMiOiJCYW5nbGFkZXNoIiwiaSI6IkJEIiwiZyI6ImVuLXhsIiwieCI6IjkxLjg4MTA5NTg4NjIzMDQ3IiwieSI6IjI0Ljg2OTQ0MDA3ODczNTM1In0%3D&weadegreetype=C")
        elif user_input in ["date"]:
            webbrowser.open("https://www.bing.com/search?q=date&form=STWESB&refig=48587c7b63e04747bc3da4b7af349e3e&mkt=en-xl&ocid=&pq=date&pqlth=4&assgl=4&sgcn=date&qs=PRES&smvpcn=0&swbcn=10&sctcn=0&sc=10-4&sp=1&ghc=0&cvid=48587c7b63e04747bc3da4b7af349e3e&clckatsg=1&hsmssg=0")
        elif user_input in ["birthday"]:
            print("17-06-2005")
        elif user_input in ["phone tak"]:
            print(takers())
        elif user_input in ["my ssc result"]:
            print("4.61")
        elif user_input in ["word print"]:
            word_print()


        else:
            print('error')



MSAA()


