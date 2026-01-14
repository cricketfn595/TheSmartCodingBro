#Program to execute virtual titration with inputted values from user
print("Welcome to the virtual titrator. This can help you find the strength or volume of an unknown chemical (acid or alkali) from known strengths and volumes.")
f=input("What do you want to find for the unknown chemical: Strength(S) or Volume(V)?")
if f=="S":
    v2=float(input("What is the volume of the unknown chemical?(in millilitres)"))
    su=input("What is the unit of chemical strength to be calculated- normality (N) or molarity(M)?")
    if su=="N":
             s1=float(input("What is the strength of the known chemical used for neutralizing the unknown chemical?"))
             v1=float(input("What is the volume of the known chemical used for neutralizing the unknown chemical?(in millilitres)"))
             s2=(v1*s1)/v2
             print("The strength of the unknown chemical is", s2, "N")
    elif su=="M":
         s1=float(input("What is the strength of the known chemical used for neutralizing the unknown chemical?"))
         v1=float(input("What is the volume of the known chemical used for neutralizing the unknown chemical?(in millilitres)"))
         s2=(v1*s1)/v2
         print("The strength of the unknown chemical is", s2, "M")
    else:
        print("Invalid")

elif f=="V":
    su=input("What is the unit of chemical strength to be calculated- normality (N) or molarity(M)?")
    if su=="N":
             s2=float(input("What is the strength of the unknown chemical?"))
             s1=float(input("What is the strength of the known chemical used for neutralizing the unknown chemical?"))
             v1=float(input("What is the volume of the known chemical used for neutralizing the unknown chemical?(in millilitres)"))
             v2=(v1*s2)/s1
             print("The volume of the unknown chemical is", v2, "millitres")
    elif su=="M":
             s2=float(input("What is the strength of the unknown chemical?"))
             s1=float(input("What is the strength of the known chemical used for neutralizing the unknown chemical?"))
             v1=float(input("What is the volume of the known chemical used for neutralizing the unknown chemical?(in millilitres)"))
             v2=(v1*s2)/s1
             print("The volume of the unknown chemical is", v2, "millitres")
    else:
        print("Invalid")

else:
    print("Sorry, we are still incapable of doing this.")

print("We hope you had a great time with us. Thank you!")
    
        
        
            
             
