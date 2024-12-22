
print("რადგან ჩემამდე მოხვედით, ალბათ, ჩემი შემქმნელივით, ვექტორებზე ოპერაციებმა თქვენც გაგაწამათ. არაუშავს, მე გაგიმარტივებთ ცხოვრებას.")

while True:
    op = input("\nრა ოპერაციის განხორციელება გსურთ ვექტორებზე: შეკრება თუ გამრავლება?")
    if op.strip() !="შეკრება" and op.strip() != "გამრავლება":
        print("გთხოვთ აირჩიოთ 'შეკრება' ან 'გამრავლება': ")
        continue
    else:
        user_operation = op.strip()
        break

def get_vect_cords(message, operation):
    while True:
        cords = input(message)
        try:
            vect_cords = []
            cords_list = cords.split(",")

            for i in cords_list:
                vect_cords. append(float(i))

            if len(vect_cords) > 3:
                print("გთხოვთ შეიტანოთ მაქსიმუმ სამი კორდინატი!")
                continue

            if operation == "შეკრება" :
                while len(vect_cords) < 3:
                    vect_cords.append(0.0) # თუ მომხმარებელი შეკრების ოპერაციას ირჩევს და სამივე კორდინატი არ შეჰყავს პროგრამა ავტომატურად ნულებით ანაცვლებს გამოტოვებულ კორდინატს
                    return vect_cords
           
            return vect_cords
            
        except ValueError:
            print("გთხოვთ შეიტანოთ კორდინატები რიცხვითი ფორმატით!")

if user_operation == "შეკრება":
    v1_cords = get_vect_cords("გთოვთ შეიტანოთ პირველი ვექტორის კორდინატები რიცხვითი ფორმატით. მაგ. 1,2,3.5 (თუ რომელიმე კორდინატს არ შეიტანთ პროგრამა ავტომატურად ნულოვან მნიშვნელობას მიანიჭებს): ", user_operation)
    v2_cords = get_vect_cords("გთოვთ შეიტანოთ მეორე ვექტორის კორდინატები რიცხვითი ფორმატით. მაგ. 1,2,3.5 (თუ რომელიმე კორდინატს არ შეიტანთ პროგრამა ავტომატურად ნულოვან მნიშვნელობას მიანიჭებს): ", user_operation)
else:
    v1_cords = get_vect_cords("გთოვთ შეიტანოთ პირველი ვექტორის კორდინატები რიცხვითი ფორმატით. მაგ. 1,2,3.5: ", user_operation)
    v2_cords = get_vect_cords("გთოვთ შეიტანოთ მეორე ვექტორის კორდინატები რიცხვითი ფორმატით. მაგ. 1,2,3.5: ", user_operation)



class VectorClass:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
       
       if isinstance(other,(float)):
           return VectorClass(self.x * other,
                              self.y * other,
                              self.z *other)
       
       elif isinstance(other, VectorClass):
           return VectorClass( self.x * other.x,
                                self.y * other.y,
                                self.z * other.z)
       
    def __add__(self, other):
        return VectorClass(self.x + other.x,
                            self.y + other.y,
                            self.z + other.z)
    def __str__(self):
        return f"{self.x} : {self.y} : {self.z}"
    
if len(v1_cords) == 1:      # იმ შემთხვევისთვის თუ მომხმარებელს სურს ვექტორის რიცხვზე გამრავლება
    v1 = v1_cords[0]
else:
    v1 = VectorClass(*v1_cords)  # "*"" სიმბოლო გვეხმარება სიის ელემენტების ცალკეულ არგუმენტებად გარდაქმნაში

if len(v2_cords) == 1:    # იმ შემთხვევისთვის თუ მომხმარებელს სურს ვექტორის რიცხვზე გამრავლება
    v2 = v2_cords[0]    
else:
    v2 = VectorClass(*v2_cords)

if user_operation == "შეკრება":
    v3 = v1 + v2
else:
    v3 = v1 * v2

print("V1 ->", v1)
print("V2 ->", v2)
print("V3 ->", v3)