# length unit conversion functions

def kilometer_to_meter(km):
    return km * 1000

def kilometer_to_centimeter(km):
    return km * 100000

def kilometer_to_mile(km):
    return km / 1.609

def kilometer_to_yard(km):
    return km * 1094

def kilometer_to_foot(km):
    return km * 3281

def kilometer_to_inch(km):
    return km * 39370

def meter_to_kilometer(m):
    return m / 1000

def meter_to_centimeter(m):
    return m * 100

def meter_to_milimeter(m):
    return m * 1000

def meter_to_mile(m):
    return m / 1609

def meter_to_yard(m):
    return m * 1.094

def meter_to_foot(m):
    return m * 3.281

def meter_to_inch(m):
    return m * 39.37

def centimeter_to_kilometer(cm):
    return cm / 100000

def centimeter_to_meter(cm):
    return cm / 100

def centimeter_to_milimeter(cm):
    return cm * 10

def centimeter_to_micrometer(cm):
    return cm * 10000

def centimeter_to_mile(cm):
    return cm / 160900

def centimeter_to_yard(cm):
    return cm / 91.44

def centimeter_to_foot(cm):
    return cm / 30.48

def centimeter_to_inch(cm):
    return cm / 2.54

def milimeter_to_meter(mim):
    return mim / 1000

def milimeter_to_centimeter(mim):
    return mim / 10

def milimeter_to_micrometer(mim):
    return mim * 1000

def milimeter_to_yard(mim):
    return mim / 914.4

def milimeter_to_foot(mim):
    return mim / 304.8

def milimeter_to_inch(mim):
    return mim / 25.4

def micrometer_to_centimeter(mcm):
    return mcm / 10000

def micrometer_to_milimeter(mcm):
    return mcm / 1000

def micrometer_to_yard(mcm):
    return mcm * 914400  

def micrometer_to_foot(mcm):
    return mcm * 304800

def micrometer_to_inch(mcm):
    return mcm * 25400

def mile_to_kilometer(mile):
    return mile * 1.609

def mile_to_meter(mile):
    return mile * 1609

def mile_to_centimeter(mile):
    return mile * 160900

def mile_to_yard(mile):
    return mile * 1760

def mile_to_foot(mile):
    return mile * 5280

def mile_to_inch(mile):
    return mile * 63360

def yard_to_kilometer(yard):
    return yard / 1094

def yard_to_meter(yard):
    return yard / 1.904

def yard_to_centimeter(yard):
    return yard * 91.44

def yard_to_milimeter(yard):
    return yard * 914.4

def yard_to_micrometer(yard):
    return yard * 914400

def yard_to_mile(yard):
    return yard / 1760

def yard_to_foot(yard):
    return yard * 3

def yard_to_inch(yard):
    return yard * 36

def foot_to_kilometer(foot):
    return foot / 3181

def foot_to_meter(foot):
    return foot / 3.281

def foot_to_centimeter(foot):
    return foot * 30.48

def foot_to_milimeter(foot):
    return foot * 304.8

def foot_to_micrometer(foot):
    return foot * 304800

def foot_to_mile(foot):
    return foot / 5280

def foot_to_yard(foot):
    return foot / 3

def foot_to_inch(foot):
    return foot * 12

def inch_to_kilometer(inch):
    return inch / 39370

def inch_to_meter(inch):
    return inch / 39.37

def inch_to_centimeter(inch):
    return inch * 2.54

def inch_to_milimeter(inch):
    return inch * 25.4

def inch_to_micrometer(inch):
    return inch ^ 25400

def inch_to_mile(inch):
    return inch / 63360

def inch_to_yard(inch):
    return inch / 36

def inch_to_foot(inch):
    return inch / 12

# mass unit conversion functions

def kilogram_to_gram(kg):
    return kg * 1000

def kilogram_to_decigram(kg):
    return kg * 10000

def kilogram_to_centigram(kg):
    return kg * 100000

def kilogram_to_miligram(kg):
    return kg * 1000000

def gram_to_kilogram(g):
    return g / 1000

def gram_to_decigram(g):
    return g * 10

def gram_to_centigram(g):
    return g * 100

def gram_to_miligram(g):
    return g * 1000

def gram_to_microgram(g):
    return g * 1000000

def miligram_to_kilogram(milig):
    return milig / 1e+6

def miligram_to_gram(milig):
    return milig / 1000
    
def miligram_to_microgram(milig):
    return milig * 1000

def microgram_to_kilogram(microg):
    return microg / 1e+9

def microgram_to_gram(microg):
    return microg / 1e+6

def microgram_to_miligram(microg):
    return microg / 1000
# time unit conversion functions

def hour_to_minute(hr):
    return hr * 60

def hour_to_second(hr):
    return hr * 3600

def minute_to_hour(min):
    return min / 60

def minute_to_second(min):
    return min * 60

def second_to_minute(sec):
    return sec / 60

def second_to_hour(sec):
    return sec / 3600

# temperature unit conversion functions

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return ( ( f - 32 ) * 5) / 9

def fahrenheit_to_kelvin(f):
    return ( f + 459.67) * 5 / 9

def kelvin_to_celsius(kl):
    return kl - 273.15

def kelvin_to_fahrenheit(kl):
    return (9/5 * (kl - 273.15) + 32)

# volume unit converison functions

def cubicmeter_to_liter(cubicm):
    return cubicm * 1000

def cubicmeter_to_mililiter(cubicm):
    return cubicm * 1e+6

def liter_cubicmeter(ltr):
    return ltr / 1000

def liter_to_mililiter(ltr):
    return ltr * 1000

def mililiter_to_cubicmeter(milil):
    return milil / 1e+6

def mililiter_to_liter(milil):
    return milil / 1000