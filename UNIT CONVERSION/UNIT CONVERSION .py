import conversion

inp = -1

while(inp!=0):
    print("\n1. Lenght")
    print("2. Temperature")
    print("3. Mass")
    print("4. Time")
    print("5. Volume")

    inp = int(input("\nENTER CHOICE : "))
    
    if(inp==1):
        print("\nEXAMPLE  From - meter | To - centimeter")
        
        print("\nENTER INPUT :-\n")
        
        frm = input("From : ")
        to = input("To : ")
        
        if(frm.upper()=="KILOMETER"):
            
            if(to.upper()=="METER"):
                
                km = float(input("\nENTER LENGTH : "))
                print(km,"KILOMETER = ",conversion.kilometer_to_meter(km),"METER")
                
            elif(to.upper()=="CENTIMETER"):
                
                km = float(input("ENTER LENGTH : "))
                print(km,"KILOMETER = ",conversion.kilometer_to_centimeter(km),"CENTIMETER")
                
            else:
                
                print("\nNO MATCH FOUND OR INVALID INPUT - ")
        
        elif(frm.upper()=="METER"):
            
            if(to.upper()=="KILOMETER"):
                
                m = float(input("\nENTER LENGTH : "))
                print(m,"METER = ",conversion.meter_to_kilometer(m),"KILOMETER")
                
            elif(to.upper()=="CENTIMETER"):
                
                m = float(input("ENTER LENGTH : "))
                print(m,"METER = ",conversion.meter_to_centimeter(m),"CENTIMETER")
                
            elif(to.upper()=="MILIMETER"):
                
                m = float(input("ENTER LENGTH : "))
                print(m,"METER = ",conversion.meter_to_milimeter(m),"MILIMETER")
                
            elif(to.upper()=="MILE"):
                
                m = float(input("ENTER LENGTH : "))
                print(m,"METER = ",conversion.meter_to_mile(m),"MILE")
                
            elif(to.upper()=="YARD"):
                
                m = float(input("ENTER LENGTH : "))
                print(m,"METER = ",conversion.meter_to_yard(m),"YARD")
                
            elif(to.upper()=="FOOT"):
                
                m = float(input("ENTER LENGTH : "))
                print(m,"METER = ",conversion.meter_to_foot(m),"FOOT")
            
            elif(to.upper()=="INCH"):
                
                m = float(input("ENTER LENGTH : "))
                print(m,"METER = ",conversion.meter_to_inch(m),"INCH")
                
            else:
                
                print("\nNO MATCH FOUND - ")
            
        elif(frm.upper()=="CENTIMETER"):
            
            if(to.upper()=="KILOMETER"):
                
                cm = float(input("ENTER LENGTH : "))
                print(cm,"CENTIMETER = ",conversion.centimeter_to_kilometer(cm),"KILOMETER")
                
            elif(to.upper()=="METER"):
                
                cm = float(input("ENTER LENGTH : "))
                print(cm,"CENTIMETER = ",conversion.centimeter_to_meter(cm),"METER")
                
            elif(to.upper()=="MILIMETER"):
                
                cm = float(input("ENTER LENGTH : "))
                print(cm,"CENTIMETER = ",conversion.centimeter_to_milimeter(cm),"MILIMETER")
                
            elif(to.upper()=="MICROMETER"):
                
                cm = float(input("ENTER LENGTH : "))
                print(cm,"CENTIMETER = ",conversion.centimeter_to_micrometer(cm),"MICROMETER") 
                
            elif(to.upper()=="MILE"):
                
                cm = float(input("ENTER LENGTH : "))
                print(cm,"CENTIMETER = ",conversion.centimeter_to_mile(cm),"MILE")
                
            elif(to.upper()=="YARD"):
                
                cm = float(input("ENTER LENGTH : "))
                print(cm,"CENTIMETER = ",conversion.centimeter_to_yard(cm),"YARD")
                
            elif(to.upper()=="FOOT"):
                
                cm = float(input("ENTER LENGTH : "))
                print(cm,"CENTIMETER = ",conversion.centimeter_to_foot(cm),"FOOT")
                
            elif(to.upper()=="INCH"):
                
                cm = float(input("ENTER LENGTH : "))
                print(cm,"CENTIMETER = ",conversion.centimeter_to_inch(cm),"INCH")
                
            else:
                
                print("\nNO MATCH FOUND OR INVALID INPUT - ")
                
        elif(frm.upper()=="MILIMETER"):
            
            if(to.upper()=="METER"):
                milim = float(input("ENTER LENGTH : "))
                print(milim,"MILIMETER = ",conversion.milimeter_to_meter(milim),"METER")
            
            elif(to.upper()=="CENTIMETER"):
                milim = float(input("ENTER LENGTH : "))
                print(milim,"MILIMETER = ",conversion.milimeter_to_centimeter(milim),"CENTIMETER")

            elif(to.upper()=="MICROMETER"):
                milim = float(input("ENTER LENGTH : "))
                print(milim,"MILIMETER = ",conversion.milimeter_to_micrometer(milim),"MICROMETER")

            elif(to.upper()=="YARD"):
                milim = float(input("ENTER LENGTH : "))
                print(milim,"MILIMETER = ",conversion.milimeter_to_yard(milim),"YARD")
                
            elif(to.upper()=="FOOT"):
                milim = float(input("ENTER LENGTH : "))
                print(milim,"MILIMETER = ",conversion.milimeter_to_foot(milim),"FOOT")
        
            elif(to.upper()=="INCH"):
                milim = float(input("ENTER LENGTH : "))
                print(milim,"MILIMETER = ",conversion.milimeter_to_inch(milim),"INCH")
        
        elif(frm.upper()=="MICROMETER"):
            
            if(to.upper()=="CENTIMETER"):
                microm = float(input("ENTER LENGTH : "))
                print(microm,"MICROMETER = ",conversion.micrometer_to_centimeter(microm),"CENTIMETER")
                
            elif(to.upper()=="MILIMETER"):
                microm = float(input("ENTER LENGTH : "))
                print(microm,"MICROMETER = ",conversion.micrometer_to_centimeter(microm),"CENTIMETER")
            
            elif(to.upper()=="FOOT"):
                microm = float(input("ENTER LENGTH : "))
                print(microm,"MICROMETER = ",conversion.micrometer_to_foot(microm),"FOOT")
            
            elif(to.upper()=="INCH"):
                microm = float(input("ENTER LENGTH : "))
                print(microm,"MICROMETER = ",conversion.micrometer_to_inch(microm),"INCH")
                
            elif(to.upper()=="YARD"):
                microm = float(input("ENTER LENGTH : "))
                print(microm,"MICROMETER = ",conversion.micrometer_to_yard(microm),"YARD")
            else:
                print("\nNO MATCH FOUND - ")
        
        elif(frm.upper()=="MILE"):
            
            if(to.upper()=="KILOMETER"):
                mile = float(input("ENTER LENGTH IN MILE : "))
                print(mile,"MILES = ",conversion.mile_to_kilometer(mile),"KILOMETER")
                
            elif(to.upper()=="METER"):
                mile = float(input("ENTER LENGTH IN MILE : "))
                print(mile,"MILES = ",conversion.mile_to_meter(mile),"METER")
                
            elif(to.upper()=="CENTIMETER"):
                mile = float(input("ENTER LENGTH IN MILE : "))
                print(mile,"MILES = ",conversion.mile_to_centimeter(mile),"CENTIMETER")
                
            elif(to.upper()=="YARD"):
                mile = float(input("ENTER LENGTH IN MILE : "))
                print(mile,"MILES = ",conversion.mile_to_yard(mile),"YARD")
                
            elif(to.upper()=="FOOT"):
                mile = float(input("ENTER LENGTH IN MILE : "))
                print(mile,"MILES = ",conversion.mile_to_foot(mile),"FOOT")
                
            elif(to.upper()=="INCH"):
                mile = float(input("ENTER LENGTH IN MILE : "))
                print(mile,"MILES = ",conversion.mile_to_inch(mile),"INCH")
                                
        elif(frm.upper()=="YARD"):

            if(to.upper()=="KILOMETER"):
                yard = float(input("ENTER LENGTH IN YARD : "))
                print(yard,"YARD = ",conversion.yard_to_kilometer(yard),"KILOMETER")
                
            elif(to.upper=="METER"):
                yard = float(input("ENTER LENGTH IN YARD : "))
                print(yard,"YARD = ",conversion.yard_to_meter(yard),"METER")
                
            elif(to.upper=="CENTIMETER"):
                yard = float(input("ENTER LENGTH IN YARD : "))
                print(yard,"YARD = ",conversion.yard_to_centimeter(yard),"CENTIMETER")
                
            elif(to.upper=="MILIMETER"):
                yard = float(input("ENTER LENGTH IN YARD : "))
                print(yard,"YARD = ",conversion.yard_to_milimeter(yard),"MILIMETER")
                
            elif(to.upper=="MICROMETER"):
                yard = float(input("ENTER LENGTH IN YARD : "))
                print(yard,"YARD = ",conversion.yard_to_micrometer(yard),"MICROMETER")
            
            elif(to.upper=="MILE"):
                yard = float(input("ENTER LENGTH IN YARD : "))
                print(yard,"YARD = ",conversion.yard_to_mile(yard),"MILE")
                        
            elif(to.upper=="FOOT"):
                yard = float(input("ENTER LENGTH IN YARD : "))
                print(yard,"YARD = ",conversion.yard_to_foot(yard),"FOOT")
                
            elif(to.upper=="INCH"):
                yard = float(input("ENTER LENGTH IN YARD : "))
                print(yard,"YARD = ",conversion.yard_to_inch(yard),"INCH")
                 
        elif(frm.upper()=="FOOT"):
            
            if(to.upper()=="KILOMETER"):
                foot = float(input("ENTER LENGTH IN FOOT : "))
                print(foot,"FOOT = ",conversion.foot_to_kilometer(foot),"KILOMETER")
                
            elif(to.upper()=="METER"):
                foot = float(input("ENTER LENGTH IN FOOT : "))
                print(foot,"FOOT",conversion.foot_to_meter(foot),"METER")
                
            elif(to.upper()=="CENTIMETER"):
                foot = float(input("ENTER LENGTH IN FOOT : "))
                print(foot,"FOOT",conversion.foot_to_centimeter(foot),"CENTIMETER")
            
            elif(to.upper()=="MILIMETER"):
                foot = float(input("ENTER LENGTH IN FOOT : "))
                print(foot,"FOOT",conversion.foot_to_milimeter(foot),"MILIMETER")
                
            elif(to.upper()=="MICROMETER"):
                foot = float(input("ENTER LENGTH IN FOOT : "))
                print(foot,"FOOT",conversion.foot_to_micrometer(foot),"MICROMETER")
                      
            elif(to.upper()=="MILE"):
                foot = float(input("ENTER LENGTH IN FOOT : "))
                print(foot,"FOOT",conversion.foot_to_mile(foot),"MILE")
                
            elif(to.upper()=="YARD"):
                foot = float(input("ENTER LENGTH IN FOOT : "))
                print(foot,"FOOT",conversion.foot_to_yard(foot),"YARD")
                
            elif(to.upper()=="INCH"):
                foot = float(input("ENTER LENGTH IN FOOT : "))
                print(foot,"FOOT",conversion.foot_to_inch(foot),"INCH")
                
        elif(frm.upper()=="INCH"):
            
            if(to.upper()=="KILOMETER"):
                inch = float(input("ENTER LENGTH IN INCH : "))
                print(inch,"INCH = ",conversion.inch_to_kilometer(inch),"KILOMETER")
                
            elif(to.upper()=="METER"):
                inch = float(input("ENTER LENGTH IN INCH : "))
                print(inch,"INCH = ",conversion.inch_to_meter(inch),"METER")
                
            elif(to.upper()=="CENTIMETER"):
                inch = float(input("ENTER LENGTH IN INCH : "))
                print(inch,"INCH = ",conversion.inch_to_centimeter(inch),"CENTIMETER") 
                
            elif(to.upper()=="MILIMETER"):
                inch = float(input("ENTER LENGTH IN INCH : "))
                print(inch,"INCH = ",conversion.inch_to_milimeter(inch),"MILIMETER")
               
            elif(to.upper()=="MICROMETER"):
                inch = float(input("ENTER LENGTH IN INCH : "))
                print(inch,"INCH = ",conversion.inch_to_micrometer(inch),"MICROMETER")
            
            elif(to.upper()=="MILE"):
                inch = float(input("ENTER LENGTH IN INCH : "))
                print(inch,"INCH = ",conversion.inch_to_mile(inch),"MILE")
                
            elif(to.upper()=="YARD"):
                inch = float(input("ENTER LENGTH IN INCH : "))
                print(inch,"INCH = ",conversion.inch_to_yard(inch),"YARD")
                
            elif(to.upper()=="FOOT"):
                inch = float(input("ENTER LENGTH IN INCH : "))
                print(inch,"INCH = ",conversion.inch_to_foot(inch),"FOOT")
                
        else:    
            print("\nINVALID INPUT - ")
            
    elif(inp==2):
        print("\nEXAMPLE  From - celsius | To - kelvin")
        
        print("\nENTER INPUT :-\n")
        
        frm = input("From : ")
        to = input("To : ")
        
        if(frm.upper()=="CELSIUS"):
            
            if(to.upper()=="FAHRENHEIT"):
                c = float(input("ENTER TEMPERATURE : "))
                print(c,"CELSIUS = ",conversion.celsius_to_fahrenheit(c),"FAHRENHEIT")
              
            elif(to.upper()=="KELVIN"):
                c = float(input("ENTER TEMPERATURE : "))
                print(c,"CELSIUS = ",conversion.celsius_to_kelvin(c),"KELVIN")
                
        elif(frm.upper()=="FAHRENHEIT"):
            
            if(to.upper()=="CELSIUS"):
                f = float(input("ENTER TEMPERATURE : "))
                print(f,"FAHRENHEIT = ",conversion.fahrenheit_to_celsius(f),"CELSIUS")
                
            elif(to.upper()=="KELVIN"):
                f = float(input("ENTER TEMPERATURE : "))
                print(f,"FAHRENHEIT = ",conversion.fahrenheit_to_kelvin(f),"KELVIN")
                
        elif(frm.upper()=="KELVIN"):
            
            if(to.upper()=="CELSIUS"):
                k = float(input("ENTER TEMPERATURE : "))
                print(k,"KELVIN = ",conversion.kelvin_to_celsius(k),"CELSIUS")
                
            elif(to.upper()=="KELVIN"):
                k = float(input("ENTER TEMPERATURE : "))
                print(k,"KELVIN = ",conversion.kelvin_to_fahrenheit(k),"FAHRENHEIT")        
                
        else:
            
            print("\nINVALID INPUT - ")
            
    elif(inp==3):
        print("\nEXAMPLE  From - kilogram | To - gram")
        
        print("\nENTER INPUT :-\n")
        
        frm = input("From : ")
        to = input("To : ")
        
        if(frm.upper()=="KILOGRAM"):
            
            if(to.upper()=="GRAM"):
                kg = float(input("\nENTER MASS : "))
                print(kg,"KILOGRAM = ",conversion.kilogram_to_gram(kg),"GRAM")
    
            elif(to.upper()=="CENTIGRAM"):
                kg = float(input("\nENTER MASS : "))
                print(kg,"KILOGRAM = ",conversion.kilogram_to_centigram(kg),"CENTIGRAM")
                
            elif(to.upper()=="MILIGRAM"):
                kg = float(input("\nENTER MASS : "))
                print(kg,"KILOGRAM = ",conversion.kilogram_to_miligram(kg),"MILIGRAM")
                
            else:
                print("\nNO MATCH FOUND - ")
                
        elif(frm.upper()=="GRAM"):
            
            if(to.upper()=="KILOGRAM"):
                g = float(input("\nENTER MASS : "))
                print(g,"GRAM = ",conversion.gram_to_kilogram(g),"KILOGRAM")
                
            elif(to.upper()=="CENTIGRAM"):
                g = float(input("\nENTER MASS : "))
                print(g,"GRAM = ",conversion.gram_to_centigram(g),"CENTIGRAM")
                
            elif(to.upper()=="MILIGRAM"):
                g = float(input("\nENTER MASS : "))
                print(g,"GRAM = ",conversion.gram_to_miligram(g),"MILIGRAM")
                
            elif(to.upper()=="MICROGRAM"):
                g = float(input("\nENTER MASS : "))
                print(g,"GRAM = ",conversion.gram_to_microgram(g),"MICROGRAM")
                
        elif(frm.upper()=="MILIGRAM"):
            
            if(to.upper()=="KILOGRAM"):
                milig = float(input("\nENTER MASS : "))
                print(milig,"MILIGRAM = ",conversion.miligram_to_kilogram(milig),"KILOGRAM")
            
            elif(to.upper()=="GRAM"):
                milig = float(input("\nENTER MASS : "))
                print(milig,"MILIGRAM = ",conversion.miligram_to_gram(milig),"GRAM")
            
            elif(to.upper()=="MIRCOGRAM"):
                milig = float(input("\nENTER MASS : "))
                print(milig,"MILIGRAM = ",conversion.miligram_to_microgram(milig),"MICROGRAM")
            
            else:
                print("\nINVALID INPUT OR NO MATCH FOUND IN 'TO' - ")
                
        elif(frm.upper()=="MICROGRAM"):
            
            if(to.upper()=="KILOGRAM"):
                microg = float(input("\nENTER MASS : "))
                print(microg,"MICROGRAM = ",conversion.microgram_to_kilogram(microg),"KILOGRAM")
                
            elif(to.upper()=="GRAM"):
                microg = float(input("\nENTER MASS : "))
                print(microg,"MICROGRAM = ",conversion.microgram_to_gram(microg),"GRAM")
               
            elif(to.upper()=="MILIGRAM"):
                microg = float(input("\nENTER MASS : "))
                print(microg,"MICROGRAM = ",conversion.microgram_to_miligram(microg),"MILIGRAM")
            
            else:
                print("\nINVALID INPUT OR NO MATCH FOUND IN 'TO' - ")

        else:
            print("\nINVALID INPUT OR NO MATCH FOUND IN 'FROM' - ")   
                
    elif(inp==4):
        print("\nEXAMPLE  From - Minute | To - Hour")
        
        print("\nENTER INPUT :-\n")
        
        frm = input("From : ")
        to = input("To : ")
        
        if(frm.upper()=="HOUR"):
            
            if(to.upper()=="MINUTE"):    
                hr = float(input("\nENTER TIME : "))
                print(hr,"HOUR = ",conversion.hour_to_minute(hr),"MINUTES")
                
            elif(to.upper()=="SECOND"):
                hr = float(input("\nENTER TIME : "))
                print(hr,"HOUR = ",conversion.hour_to_second(hr),"SECONDS")
            
            else:
                print("\nINVALID INPUT OR NO MATCH FOUND IN 'TO' - ")
            
        elif(frm.upper()=="MINUTE"):
            
            if(to.upper()=="HOUR"):
                
                min = float(input("\nENTER TIME : "))
                print(min,"MINUTES = ",conversion.minute_to_hour(min),"HOURS")
            
            elif(to.upper()=="SECOND"):
                
                min = float(input("\nENTER TIME : "))
                print(min,"MINUTES = ",conversion.minute_to_second(min),"SECONDS")
            
            else:
                print("\nINVALID INPUT OR NO MATCH FOUND IN 'TO' - ")
                
        elif(frm.upper()=="SECOND"):
            
            if(to.upper()=="HOUR"):
                sec = float(input("\nENTER TIME : "))
                print(sec,"SECONDS = ",conversion.second_to_hour(sec),"HOUR")
                
            elif(to.upper()=="MINUTE"):
                sec = float(input("\nENTER TIME : "))
                print(sec,"SECONDS = ",conversion.second_to_minute(sec),"MINUTES")
        
            else:
                print("\nINVALID INPUT OR NO MATCH FOUND IN 'TO' - ")
        
        else:
            print("\nINVALID INPUT OR NO MATCH FOUND IN 'FROM' - ")   
              
        
    elif(inp==5):
        print("\nEXAMPLE  From - liter | To - cubicmeter")
        
        print("\nENTER INPUT :-\n")
        
        frm = input("From : ")
        to = input("To : ")
        
        if(frm.upper()=="LITER"):

            if(to.upper()=="CUBICMETER"):
                ltr = float(input("\nENTER VOLUME : "))
                print(ltr,"LITER = ",conversion.liter_to_cubicmeter(ltr),"CUBIC MTER")
            
            elif(to.upper()=="MILILITER"):
                
                ltr = float(input("\nENTER VOLUME : "))
                print(ltr,"LITER = ",conversion.liter_to_mililiter(ltr),"MILILITER")
            
            else:
                print("\nINVALID INPUT OR NO MATCH FOUND IN 'TO' - ")
            
        elif(frm.upper()=="CUBICMETER"):
        
            if(to.upper=="LITER"):
                cubicm = float(input("\nENTER VOLUME : "))
                print(cubicm,"CUMIC METER = ",conversion.cubicmeter_to_liter(cubicm),"LITER")
    
            elif(to.upper()=="MILILITER"):
                
                cubicm = float(input("\nENTER VOLUME : "))
                print(cubicm,"LITER = ",conversion.cubicmeter_to_mililiter(cubicm),"MILILITER")
            
            else:
                print("\nINVALID INPUT OR NO MATCH FOUND IN 'TO' - ")
                
        elif(frm.upper()=="MILILITER"):
            
            if(to.upper()=="CUBICMETER"):
                milil = float(input("\nENTER VOLUME : "))
                print(cubicm,"MILILITER = ",conversion.mililiter_to_cubicmeter(milil),"CUBIC METER")
                
            elif(to.upper()=="LITER"):
                milil = float(input("\nENTER VOLUME : "))
                print(milil,"MILILITER = ",conversion.mililiter_to_liter(milil),"LITER")
                
            else:
                print("\nINVALID INPUT OR NO MATCH FOUND IN 'TO' - ")
        
        else:
            print("\nINVALID INPUT OR NO MATCH FOUND IN 'FROM' - ")   
                         
    else:
        print("\nINVALID CHOICE INPUT - ")