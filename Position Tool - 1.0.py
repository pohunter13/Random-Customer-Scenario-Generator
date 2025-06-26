import random

##### Define Variables ###
Random_IT1_Number = 0
Random_IT1 = ""
Random_IT2_Number = 0
Random_IT2 = ""
Random_App1_Number = 0
Random_App1 = ""
Random_App1_str = ""
Random_App2_Number = 0
Random_App2 = ""

########## IT Department Information ##########

print("---------------------- START OF SCENARIO ----------------------")
print("")
print("IT Department Information...")
print("")

    # IT1 is addressing how many people are on thier IT team

IT1 = ['1','2','3','4','5','6','7','8','9','10','13','15']
Random_IT1_Number = random.randint(0, len(IT1) - 1)
Random_IT1 = IT1[Random_IT1_Number]
print("Number of people on IT team:", Random_IT1)

    # IT2 is addressing how much time they spent managing their data center

IT2 = ['Spend a lot of time managing our data center',
        'Spend about half of my time managing our data center',
        'Spend very little to no time managing our data center']
Random_IT2_Number = random.randint(0, len(IT2)-1)
Random_IT2 = IT2[Random_IT2_Number]
print("Time spent managing data:", Random_IT2)

############ Application Information ##########

print("")
print("--------------------------------")
print("Application Information...")
print("")

    # App1 gives info about important applications

App1 = ["ERP", "SCM", "Online customer portal", "Exchange(email)", "Payment/billing", "Salesforce"]
Random_App1 = random.sample(App1, 3)
Random_App1_str = ", ".join(Random_App1)
print("MC Apps:", Random_App1_str)

    # App2 asks if they have any new apps in development

App2 = ["Yes","No"]
Random_App2_Number = random.randint(0,len(App2)-1)
Random_App2 = App2[Random_App2_Number]
print("Any new applications?",Random_App2)

    # App3 tells the timline for the app (if there is a new one)
if Random_App2 == "Yes":
    App3 = ['3 months','6 months','1 year', 'Few years']
    Random_App3_Number = random.randint(0,len(App3)-1)
    Random_App3 = App3[Random_App3_Number]
    print("Timeline to deploy new app:",Random_App3)

    # App4 deals with predicted data growth

App4 = ['%5','%10','%15','%20','%25','%30']
Random_App4_Number = random.randint(0,len(App4)-1)
Random_App4 = App4[Random_App4_Number]
print("Predicted data growth:",Random_App4)

    # App5 deals with how their apps are currently performing

App5 = ["Some latency",
        "Lots of latency",
        "Not much latency",
        "No downtime",
        "Some downtime but rare",
        "Lots of downtime"]
Random_App5_Number = random.randint(0,len(App5)-1)
Random_App5 = App5[Random_App5_Number]
print("Current app performance:",Random_App5)

########## Server Information ##########

print("")
print("--------------------------------")
print("Server Information...")
print("")

    # Serv1 is talking about their experience with their current hardware

Serv1 = ["Experience has been good",
         "Experience has been bad due to latency",
         "Experience has been bad due to storing directly on server"]
Random_Serv1_Number = random.randint(0,len(Serv1)-1)
Random_Serv1 = Serv1[Random_Serv1_Number]
print("Experience with their current server:",Random_Serv1)

    # Serv2 is talking about how many servers they currently have

Serv2 = ["1","2","3","4","5","6","7","8","9","10"]
Random_Serv2_Number = random.randint(0,len(Serv2)-1)
Random_Serv2 = Serv2[Random_Serv2_Number]
print("Total number of servers:",Random_Serv2)

    # Serv3 is how long they have had their current servers

Serv3 = ["1 year","2 years","3 years","4 years","5 years"]
Random_Serv3_Number = random.randint(0,len(Serv3)-1)
Random_Serv3 = Serv3[Random_Serv3_Number]
print("How long they've had their servers:",Random_Serv3)

    # Serv4 is how long they're under maintenance for their servers

Serv4 = ["Few months","6 months","1 year","Several years"]
Random_Serv4_Number = random.randint(0,len(Serv4)-1)
Random_Serv4 = Serv4[Random_Serv4_Number]
print("How much longer under maintenance:",Random_Serv4)

########## Storage Information ##########

print("")
print("--------------------------------")
print("Storage Information...")
print("")

    # Stor1 is how thier experience has been with thier current hardware

Stor1 = ["Experience has been good",
         "Experience has been bad due to capacity issues",
         "Experience has been bad due to complex management"]
Random_Stor1_Number = random.randint(0,len(Stor1)-1)
Random_Stor1 = Stor1[Random_Stor1_Number]
print("Experience with current storage array:",Random_Stor1)

    # Stor2 is talking about how many storage arrays they have

Stor2 = ["1","2","3","4"]
Random_Stor2_Number = random.randint(0,len(Stor2)-1)
Random_Stor2 = Stor2[Random_Stor2_Number]
print("How many arrays they have:",Random_Stor2)

    # Stor3 is how long they've had their storage arrays

Stor3 = ["1 year","2 years","3 years","4 years","5 years"]
Random_Stor3_Number = random.randint(0,len(Stor3)-1)
Random_Stor3 = Stor3[Random_Stor3_Number]
print("How long they've had these arrays:",Random_Stor3)

    # Stor4 is how much longer their servers are under maintenance

Stor4 = ["Few months","6 months","1 year","Several years"]
Random_Stor4_Number = random.randint(0,len(Stor4)-1)
Random_Stor4 = Stor4[Random_Stor4_Number]
print("How much longer arrays under maintenance:",Random_Stor4)

    # Stor 5 is what capacity they're at

Stor5 = ["%20","%30","%40","%50","%60","%70","%80","%90"]
Random_Stor5_Number = random.randint(0,len(Stor5)-1)
Random_Stor5 = Stor5[Random_Stor5_Number]
print("What % capacity filled on array:",Random_Stor5)

########## Backup Information ##########

print("")
print("--------------------------------")
print("Backup Information...")
print("")

    #BU1 is software

BU1 = ["Dell's BU software","Non-Dell BU software"]
Random_BU1_Number = random.randint(0,len(BU1)-1)
Random_BU1 = BU1[Random_BU1_Number]
print("BU software:",Random_BU1)

    #BU2 is hardware

BU2 = ["Tape","HDDs","SSDs","Dedicated backup appliance","Cloud"]
Random_BU2_Number = random.randint(0,len(BU2)-1)
Random_BU2 = BU2[Random_BU2_Number]
print("BU hardware:",Random_BU2)

    #BU3 is backup schedule

BU3 = ["Every night","3 nights a week","Once per week","Once every 2 weeks"]
Random_BU3_Number = random.randint(0,len(BU3)-1)
Random_BU3 = BU3[Random_BU3_Number]
print("BU schedule:",Random_BU3)

    #BU4 is backup window

BU4 = ["2 hours","3 hours","4 hours","5 hours","6 hours","8 hours"]
Random_BU4_Number = random.randint(0,len(BU4)-1)
Random_BU4 = BU4[Random_BU4_Number]
print("BU window:",Random_BU4)

    #BU5 is backup target capacity

BU5 = ["%20","%30","%40","%50","%60","%70","%80","%90"]
Random_BU5_Number = random.randint(0,len(BU5)-1)
Random_BU5 = BU5[Random_BU5_Number]
print("BU target capacity:",Random_BU5)

    #BU6 is retention policies

BU6 = ["No policies requiring specific retention times",
       "Retain data for 3 months",
       "Retain data for 6 months",
       "Retain data for 1 year",
       "Retain data for 3 years"]
Random_BU6_Number = random.randint(0,len(BU6)-1)
Random_BU6 = BU6[Random_BU6_Number]
print("BU retention requirements:",Random_BU6)

    #BU7 is how often they do restores

BU7 = ["Once a week",
       "Once a month",
       "Once a quarter",
       "Only when absolutely necessary"]
Random_BU7_Number = random.randint(0,len(BU7)-1)
Random_BU7 = BU7[Random_BU7_Number]
print("How often they perform restores:",Random_BU7)

    #BU8 is if they have ever had failed restores in the past

BU8 = ["Yes","No"]
Random_BU8_Number = random.randint(0,len(BU8)-1)
Random_BU8 = BU8[Random_BU8_Number]
print("Ever had failed restores?:",Random_BU8)

########## Disaster Recovery Information ##########

print("")
print("--------------------------------")
print("Disaster Recovery Information...")
print("")

    #DR 1 is do they have a disaster recovery plan or not

DR1 = ["Yes","No not really"]
Random_DR1_Number = random.randint(0,len(DR1)-1)
Random_DR1 = DR1[Random_DR1_Number]
print("Do you have a disaster recovery plan?:",Random_DR1)

    ### The rest of these only apply if they DO have a disaster recovery plan ###

    # DR2 is if they have a secondary site
    
if Random_DR1 == "Yes":
    DR2 = ["Yes","No"]
    Random_DR2_Number = random.randint(0,len(DR2)-1)
    Random_DR2 = DR2[Random_DR2_Number]
    print("Do they have a 2nd site?:",Random_DR2)

    # DR3 is if that site is sync or async
    
    if Random_DR2 == "Yes":
        DR3 = ["Synchronous","Asynchronous"]
        Random_DR3_Number = random.randint(0,len(DR3)-1)
        Random_DR3 = DR3[Random_DR3_Number]
        print("Is that site sync or async?:",Random_DR3)

    # DR4 is their RPO/RTO time
    
        if Random_DR3 == "Asynchronous":
            DR4 = ["2 hours",
           "3 hours",
           "4 hours",
           "5 hours",
           "6 hours",
           "8 hours"]
            Random_DR4_Number = random.randint(0,len(DR4)-1)
            Random_DR4 = DR4[Random_DR4_Number]
            print("RPO/RTO time:",Random_DR4)


########## Partner Information ##########

print("")
print("--------------------------------")
print("Partner Information...")
print("")

    #Partner1 is if they have a preferred partner that you've worked with in the past

Partner1 = ["Yes","No"]
Random_Partner1_Number = random.randint(0,len(Partner1)-1)
Random_Partner1 = Partner1[Random_Partner1_Number]
print("Preferred partner?:",Random_Partner1)

########## Budget Information ##########

print("")
print("--------------------------------")
print("Budget Information...")
print("")

Budget1 = ["Do not want to share budget",
           "5 figures",
           "6 figures",
           "Willing to spend whatever it takes to get the job done"]
Random_Budget1_Number = random.randint(0,len(Budget1)-1)
Random_Budget1 = Budget1[Random_Budget1_Number]
print("Budget:",Random_Budget1)

########## Authority Information ##########

print("")
print("--------------------------------")
print("Authority Information...")
print("")

Auth1 = ["I make the budget decisions",
         "I need approval from higher ups on budgeting decisions"]
Random_Auth1_Number = random.randint(0,len(Auth1)-1)
Random_Auth1 = Auth1[Random_Auth1_Number]
print("Authority:",Random_Auth1)

########## Timeline Information ##########
print("")
print("--------------------------------")
print("Timeline Information...")
print("")
print("Infer timeline from app/capacity demands, if no clear demands then assume no dedicated timeline")
print("")
print("")
print("---------------------- END OF SCENARIO ----------------------")











    



    




