one = [["Van Cortlandt Park - 242 St", "40.889248", "-73.898583", ["1"]],
       ["238 St", "40.884667", "-73.90087", ["1"]],
       ["231 St", "40.878856","-73.904834", ["1"]],
       ["Marble Hill - 225 St", "40.874561", "-73.909831", ["1"]],
       ["215 St", "40.869444", "-73.915279", ["1"]],
       ["207 St", "40.864621",  "-73.918822", ["1"]],
       ["Dyckman St", "40.860531",  "-73.925536", ["1"]],
       ["191 St", "40.855225", "-73.929412", ["1"]],
       ["181 St", "40.849505", "-73.933596", ["1"]],
       ["168 St - Washington Hts", "40.840556",  "-73.940133", ["1"]],
       ["157 St", "40.834041", "-73.94489", ["1"]],
       ["145 St", "40.826551", "-73.95036", ["1"]],
       ["137 St - City College", "40.822008", "-73.953676", ["1"]],
       ["125 St", "40.815581", "-73.958372", ["1"]],
       ["116 St - Columbia University", "40.807722", "-73.96411", ["1"]],
       ["Cathedral Pkwy", "40.803967", "-73.966847", ["1"]],
       ["103 St", "40.799446", "-73.968379", ["1"]],
       ["96 St", "40.793919", "-73.972323", ["1","2","3"]],
       ["86 St", "40.788644", "-73.976218", ["1"]],
       ["79 St", "40.783934", "-73.979917", ["1"]],
       ["72 St", "40.778453", "-73.98197", ["1","2","3"]],
       ["66 St - Lincoln Center", "40.77344", "-73.982209", ["1"]],
       ["59 St - Columbus Circle", "40.768247", "-73.981929", ["1"]],#,"2"]],
       ["50 St", "40.761728", "-73.983849", ["1"]],
       ["Times Sq - 42 St", "40.75529", "-73.987495", ["1","2","3"]],
       ["34 St - Penn Station", "40.750373", "-73.991057", ["1","2","3"]],
       ["28 St", "40.747215", "-73.993365", ["1"]],
       ["23 St", "40.744081", "-73.995657", ["1"]],
       ["18 St", "40.74104", "-73.997871", ["1"]],
       ["14 St", "40.737826", "-74.000201", ["1","2","3"]],
       ["Christopher St - Sheridan Sq", "40.733422", "-74.002906", ["1"]],
       ["Houston St", "40.728251", "-74.005367", ["1"]],
       ["Canal St", "40.722854", "-74.006277", ["1"]],
       ["Franklin St", "40.719318", "-74.006886", ["1"]],
       ["Chambers St", "40.715478", "-74.009266", ["1","2","3"]],
       ["Cortlandt St", "40.711835", "-74.012188", ["1"]],
       ["Rector St", "40.707513", "-74.013783", ["1"]],
       ["South Ferry Loop", "40.701411",  "-74.013205", ["1"]]
]

def get_one():
    return one

two = [["Wakefield - 241 St","40.903125", "-73.85062", ["2"]],
       ["Nereid Av", "40.898379", "-73.854376", ["2"]],
       ["233 St", "40.893193", "-73.857473", ["2"]],
       ["225 St", "40.888022", "-73.860341", ["2"]],
       ["219 St", "40.883895", "-73.862633", ["2"]],
       ["Gun Hill Rd", "40.87785", "-73.866256", ["2"]],
       ["Burke Av", "40.871356", "-73.867164", ["2"]],
       ["Allerton Av", "40.865462", "-73.867352", ["2"]],
       ["Pelham Pkwy", "40.857192", "-73.867615", ["2"]],
       ["Bronx Park East", "40.848828", "-73.868457", ["2"]],
       ["E 180 St", "40.841894", "-73.873488", ["2","5"]],
       ["West Farms Sq - E Tremont Av", "40.840295", "-73.880049", ["2", "5"]],
       ["174 St", "40.837288", "-73.887734", ["2", "5"]],
       ["Freeman St", "40.829993", "-73.891865", ["2"]],
       ["Simpson St", "40.824073", "-73.893064", ["2"]],
       ["Intervale Av", "40.822181", "-73.896736", ["2"]],
       ["Prospect Av", "40.819585", "-73.90177", ["2"]],
       ["Jackson Av", "40.81649", "-73.907807", ["2"]],
       ["3 Av - 149 St", "40.816109", "-73.917757", ["2","5"]],
       ["149 St - Grand Concourse", "40.81841", "-73.926718", ["2","4","5"]],
       ["135 St", "40.814229", "-73.94077", ["2","3"]],
       ["125 St", "40.807754", "-73.945495", ["2"]],
       ["116 St", "40.802098", "-73.949625", ["2"]],
       ["Central Park North (110 St)", "40.799075", "-73.951822", ["2"]],
       ["96 St", "40.793919", "-73.972323", ["1","2","3"]],
       ["72 St", "40.778453", "-73.98197", ["1","2","3"]],
       ["Times Sq - 42 St",  "40.75529", "-73.987495", ["1","2","3"]],
       ["34 St - Penn Station",  "40.750373", "-73.991057", ["1","2","3"]],
       ["14 St", "40.737826", "-74.000201", ["1","2","3"]],
       ["Chambers St", "40.715478", "-74.009266", ["1","2","3"]],
       ["Park Pl", "40.713051", "-74.008811", ["2","3"]],
       ["Fulton St", "40.709416", "-74.006571", ["2","3","4","5"]],
       ["Wall St", "40.706821", "-74.0091", ["2","3"]],
       ["Clark St", "40.697466", "-73.993086", ["2","3"]],
       ["Borough Hall", "40.693219", "-73.989998", ["2","3","4","5"]],
       ["Hoyt St", "40.690545", "-73.985065", ["2","3"]],
       ["Nevins St", "40.688246", "-73.980492", ["2","3","4","5"]],
       ["Atlantic Av - Barclays Ctr", "40.684359", "-73.977666", ["2","3","4","5"]],
       ["Bergen St", "40.680829", "-73.975098", ["2","3"]],
       ["Grand Army Plaza", "40.675235", "-73.971046", ["2","3"]],
       ["Eastern Pkwy - Brooklyn Museum", "40.671987", "-73.964375", ["2","3"]],
       ["Franklin Av", "40.670682", "-73.958131", ["2","3","4","5"]],
       ["President St", "40.667883", "-73.950683", ["2"]],
       ["Sterling St", "40.662742", "-73.95085", ["2"]],
       ["Winthrop St", "40.656652", "-73.9502", ["2"]],
       ["Church Av", "40.650843", "-73.949575", ["2"]],
       ["Beverly Rd", "40.645098", "-73.948959", ["2"]],
       ["Newkirk Av", "40.639967", "-73.948411", ["2"]],
       ["Flatbush Av - Brooklyn College", "40.632836", "-73.947642", ["2","5"]]
]

def get_two():
    return two

three = [["Harlem - 148 St","40.82388", "-73.93647", ["3"]],
         ["145 St","40.820421", "-73.936245", ["3"]],
         ["135 St","40.817894","-73.947649", ["2","3"]],
         ["125 St","40.811109", "-73.952343", ["3"]],
         ["116 St","40.805085", "-73.954882", ["3"]],
         ["Central Park North (110 St)","40.799075", "-73.951822", ["3"]],
         ["96 St","40.793919", "-73.972323", ["1","2","3"]],
         ["72 St","40.778453", "-73.98197", ["1","2","3"]],
         ["Times Sq - 42 St","40.75529", "-73.987495", ["1","2","3"]],
         ["34 St - Penn Station","40.750373", "-73.991057", ["1","2","3"]],
         ["14 St","40.737826", "-74.000201", ["1","2","3"]],
         ["Chambers St","40.715478", "-74.009266", ["1","2","3"]],
         ["Park Pl","40.713051", "-74.008811", ["2","3"]],
         ["Fulton St","40.709416", "-74.006571", ["2","3","4","5"]],
         ["Wall St","40.706821", "-74.0091", ["2","3"]],
         ["Clark St","40.697466", "-73.993086", ["2","3"]],
         ["Borough Hall","40.693219", "-73.989998", ["2","3","4","5"]],
         ["Hoyt St","40.690545", "-73.985065", ["2","3"]],
         ["Nevins St","40.688246", "-73.980492", ["2","3","4","5"]],
         ["Atlantic Av - Barclays Ctr","40.684359", "-73.977666", ["2","3","4","5"]],
         ["Bergen St","40.680829", "-73.975098", ["2","3"]],
         ["Grand Army Plaza","40.675235", "-73.971046", ["2","3"]],
         ["Eastern Pkwy - Brooklyn Museum","40.671987", "-73.964375", ["2","3"]],
         ["Franklin Av","40.670682", "-73.958131", ["2","3","4","5"]],
         ["Nostrand Av","40.669847", "-73.950466", ["3"]],
         ["Kingston Av","40.669399", "-73.942161", ["3"]],
         ["Crown Hts - Utica Av","40.668897", "-73.932942", ["3","4"]],
         ["Sutter Av - Rutland Rd","40.664717", "-73.92261", ["3"]],
         ["Saratoga Av","40.661453", "-73.916327", ["3"]],
         ["Rockaway Av","40.662549", "-73.908946", ["3"]],
         ["Junius St","40.663515", "-73.902447", ["3"]],
         ["Pennsylvania Av","40.664635", "-73.894895", ["3"]],
         ["Van Siclen Av","40.665449", "-73.889395", ["3"]],
         ["New Lots Av","40.666235", "-73.884079", ["3"]]
]

def get_three():
    return three

four = [["Woodlawn", "40.886037", "-73.878751", ["4"]],
        ["Mosholu Pkwy", "40.87975", "-73.884655", ["4"]],
        ["Bedford Park Blvd - Lehman College", "40.873412", "-73.890064", ["4"]],
        ["Kingsbridge Rd", "40.86776", "-73.897174", ["4"]],
        ["Fordham Rd", "40.862803", "-73.901034", ["4"]],
        ["183 St", "40.858407", "-73.903879", ["4"]],
        ["Burnside Av", "40.853453", "-73.907684", ["4"]],
        ["176 St", "40.84848", "-73.911794", ["4"]],
        ["Mt Eden Av", "40.844434", "-73.914685", ["4"]],
        ["170 St", "40.840075", "-73.917791", ["4"]],
        ["167 St", "40.835537", "-73.9214", ["4"]],
        ["161 St - Yankee Stadium", "40.827994", "-73.925831", ["4"]],
        ["149 St - Grand Concourse", "40.818375","-73.927351", ["2","4","5"]],
        ["138 St - Grand Concourse", "40.813224","-73.929849", ["4","5"]],
        ["125 St", "40.804138", "-73.937594", ["4","5","6"]],
        ["86 St", "40.779492", "-73.955589", ["4","5","6"]],
        ["59 St", "40.762526", "-73.967967", ["4","5","6"]],
        ["Grand Central - 42 St", "40.751776", "-73.976848", ["4","5","6"]],
        ["14 St - Union Sq", "40.734673", "-73.989951", ["4","5","6"]],
        ["Broadway-Lafayette St", "40.725297", "-73.996204", ["4","6"]],
        ["Canal St", "40.718803", "-74.000193", ["4","6"]],
        ["Brooklyn Bridge - City Hall", "40.713065", "-74.004131", ["4","5","6"]],
        ["Fulton St", "40.710368", "-74.009509", ["2","3","4","5"]],
        ["Wall St", "40.707557", "-74.011862", ["4","5"]],
        ["Bowling Green", "40.704817", "-74.014065", ["4","5"]],
        ["Borough Hall", "40.692404", "-73.990151", ["2","3","4","5"]],
        ["Nevins St", "40.688246", "-73.980492", ["2","3","4","5"]],
        ["Atlantic Av - Barclays Ctr", "40.684359", "-73.977666", ["2","3","4","5"]],
        ["Franklin Av", "40.670682", "-73.958131", ["2","3","4","5"]],
        ["Crown Hts - Utica Av","40.668897", "-73.932942", ["3","4"]]
]

def get_four():
    return four

five = [["Eastchester - Dyre Av", "40.8883", "-73.830834", ["5"]],
        ["Baychester Av", "40.878663", "-73.838591", ["5"]],
        ["Gun Hill Rd", "40.869526", "-73.846384", ["2", "5"]],
        ["Pelham Pkwy", "40.858985", "-73.855359", ["5"]],
        ["Morris Park", "40.854364", "-73.860495", ["5"]],
        ["E 180 St", "40.841894", "-73.873488", ["2","5"]],
        ["West Farms Sq - E Tremont Av","40.840295", "-73.880049", ["2", "5"]],
        ["174 St", "40.837288", "-73.887734", ["2", "5"]],
        ["Freeman St", "40.829993", "-73.891865", ["5"]],
        ["Simpson St", "40.824073", "-73.893064", ["5"]],
        ["Intervale Av","40.822181", "-73.896736", ["5"]],
        ["Prospect Av","40.819585", "-73.90177", ["5"]],
        ["Jackson Av", "40.81649", "-73.907807", ["5"]],
        ["3 Av - 149 St", "40.816109", "-73.917757", ["2","5"]],
        ["149 St - Grand Concourse","40.81841", "-73.926718", ["2","4","5"]],
        ["138 St - Grand Concourse", "40.813224","-73.929849", ["4","5"]],
        ["125 St", "40.807754", "-73.945495", ["4","5","6"]],
        ["86 St", "40.779492", "-73.955589", ["4","5","6"]],
        ["59 St", "40.762526", "-73.967967", ["4","5","6"]],
        ["Grand Central - 42 St", "40.751776", "-73.976848", ["4","5","6"]],
        ["14 St - Union Sq", "40.734673", "-73.989951", ["4","5","6"]],
        ["Brooklyn Bridge - City Hall", "40.713065", "-74.004131", ["4","5","6"]],
        ["Fulton St", "40.710368", "-74.009509", ["2","3","4","5"]],
        ["Wall St", "40.707557", "-74.011862", ["4","5"]],
        ["Bowling Green", "40.704817", "-74.014065", ["4","5"]],
        ["Borough Hall", "40.692404", "-73.990151", ["2","3","4","5"]],
        ["Nevins St", "40.688246", "-73.980492", ["2","3","4","5"]],
        ["Atlantic Av - Barclays Ctr", "40.684359", "-73.977666", ["2","3","4","5"]],
        ["Franklin Av", "40.670682", "-73.958131", ["2","3","4","5"]],
        ["President St", "40.667883", "-73.950683", ["5"]],
        ["Sterling St", "40.662742", "-73.95085", ["5"]],
        ["Winthrop St", "40.656652", "-73.9502", ["5"]],
        ["Church Av", "40.650843", "-73.949575", ["5"]],
        ["Beverly Rd", "40.645098", "-73.948959", ["5"]],
        ["Newkirk Av", "40.639967", "-73.948411", ["5"]],
        ["Flatbush Av - Brooklyn College","40.632836", "-73.947642", ["2", "5"]]
]

def get_five():
    return five

six = [["Pelham Bay Park", "40.852462", "-73.828121", ["6"]],
       ["Buhre Av", "40.84681", "-73.832569", ["6"]],
       ["Middletown Rd", "40.843863","-73.836322", ["6"]],
       ["Westchester Sq - E Tremont Av", "40.839892", "-73.842952", ["6"]],
       ["Zerega Av", "40.836488", "-73.847036", ["6"]],
       ["Castle Hill Av", "40.834255", "-73.851222", ["6"]],
       ["Parkchester", "40.833226", "-73.860816", ["6"]],
       ["St Lawrence Av", "40.831509", "-73.867618", ["6"]],
       ["Morrison Av- Sound View", "40.829521", "-73.874516", ["6"]],
       ["Elder Av", "40.828584", "-73.879159", ["6"]],
       ["Whitlock Av", "40.826525", "-73.886283", ["6"]],
       ["Hunts Point Av", "40.820948", "-73.890549", ["6"]],
       ["Longwood Av","40.816104", "-73.896435", ["6"]],
       ["E 149 St", "40.812118", "-73.904098", ["6"]],
       ["E 143 St - St Mary's St", "40.808719", "-73.907657", ["6"]],
       ["Cypress Av", "40.805368", "-73.914042", ["6"]],
       ["Brook Av", "40.807566", "-73.91924", ["6"]],
       ["3 Av - 138 St", "40.810476", "-73.926138", ["6"]],
       ["125 St", "40.804138", "-73.937594", ["4","5","6"]],
       ["116 St", "40.798629", "-73.941617", ["6"]],
       ["110 St", "40.79502", "-73.94425", ["6"]],
       ["103 St", "40.7906", "-73.947478", ["6"]],
       ["96 St", "40.785672", "-73.95107", ["6"]],
       ["86 St", "40.779492", "-73.955589", ["4","5","6"]],
       ["77 St", "40.77362", "-73.959874", ["6"]],
       ["68 St - Hunter College", "40.768141", "-73.96387", ["6"]],
       ["59 St", "40.762526", "-73.967967", ["4","5","6"]],
       ["51 St", "40.757107", "-73.97192", ["6"]],
       ["Grand Central - 42 St", "40.751776", "-73.976848", ["4","5","6"]],
       ["33 St", "40.746081", "-73.982076", ["6"]],
       ["28 St", "40.74307", "-73.984264", ["6"]],
       ["23 St", "40.739864", "-73.986599", ["6"]],
       ["14 St - Union Sq", "40.734673", "-73.989951", ["4","5","6"]],
       ["Astor Pl", "40.730054", "-73.99107", ["6"]],
       ["Broadway-Lafayette St", "40.725297", "-73.996204", ["4","6"]],
       ["Spring St", "40.722301", "-73.997141", ["6"]],
       ["Canal St", "40.718803", "-74.000193", ["4","6"]],
       ["Brooklyn Bridge - City Hall","40.713065", "-74.004131", ["4","5","6"]]
]

def get_six():
    return six


d1=[[u'0.4 mi', u'4 mins'], [u'0.5 mi', u'1 min'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'5 mins'], [u'0.6 mi', u'4 mins'], [u'0.4 mi', u'2 mins'], [u'0.7 mi', u'3 mins'], [u'0.6 mi', u'3 mins'], [u'0.6 mi', u'3 mins'], [u'0.5 mi', u'4 mins'], [u'0.5 mi', u'3 mins'], [u'0.7 mi', u'5 mins'], [u'0.5 mi', u'4 mins'], [u'0.5 mi', u'3 mins'], [u'0.5 mi', u'5 mins'], [u'0.5 mi', u'5 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'3 mins'], [u'0.6 mi', u'4 mins'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'4 mins'], [u'0.3 mi', u'3 mins'], [u'0.3 mi', u'2 mins'], [u'0.2 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.2 mi', u'1 min'], [u'0.3 mi', u'2 mins'], [u'0.3 mi', u'6 mins'], [u'0.5 mi', u'7 mins'], [u'0.5 mi', u'3 mins']]

def get_d1():
    return d1

u1=[[u'0.4 mi', u'2 mins'], [u'0.3 mi', u'7 mins'], [u'0.3 mi', u'6 mins'], [u'0.3 mi', u'2 mins'], [u'0.2 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'3 mins'], [u'0.3 mi', u'2 mins'], [u'0.2 mi', u'1 min'], [u'0.3 mi', u'2 mins'], [u'0.3 mi', u'2 mins'], [u'0.5 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.6 mi', u'5 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'3 mins'], [u'0.5 mi', u'5 mins'], [u'0.5 mi', u'5 mins'], [u'0.5 mi', u'3 mins'], [u'0.5 mi', u'4 mins'], [u'0.7 mi', u'5 mins'], [u'0.5 mi', u'4 mins'], [u'0.5 mi', u'4 mins'], [u'0.6 mi', u'3 mins'], [u'0.6 mi', u'3 mins'], [u'0.7 mi', u'3 mins'], [u'0.4 mi', u'2 mins'], [u'0.6 mi', u'4 mins'], [u'0.5 mi', u'4 mins'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'3 mins']]

def get_u1():
    return u1

d2=[[u'0.4 mi', u'1 min'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.5 mi', u'1 min'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.6 mi', u'2 mins'], [u'0.6 mi', u'1 min'], [u'0.6 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.9 mi', u'3 mins'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'3 mins'], [u'0.4 mi', u'2 mins'], [u'1.4 mi', u'7 mins'], [u'1.2 mi', u'4 mins'], [u'1.7 mi', u'4 mins'], [u'0.4 mi', u'4 mins'], [u'1.0 mi', u'3 mins'], [u'1.8 mi', u'4 mins'], [u'0.4 mi', u'4 mins'], [u'0.4 mi', u'5 mins'], [u'0.3 mi', u'2 mins'], [u'1.3 mi', u'6 mins'], [u'0.4 mi', u'3 mins'], [u'0.3 mi', u'7 mins'], [u'0.3 mi', u'1 min'], [u'0.6 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'3 mins'], [u'0.5 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.6 mi', u'5 mins'], [u'0.5 mi', u'4 mins'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'2 mins']]

def get_d2():
    return d2

u2=[[u'0.5 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'3 mins'], [u'0.6 mi', u'5 mins'], [u'0.4 mi', u'3 mins'], [u'0.6 mi', u'4 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'3 mins'], [u'0.6 mi', u'4 mins'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'4 mins'], [u'0.4 mi', u'4 mins'], [u'1.3 mi', u'4 mins'], [u'0.3 mi', u'2 mins'], [u'0.4 mi', u'5 mins'], [u'0.4 mi', u'4 mins'], [u'1.8 mi', u'8 mins'], [u'1.1 mi', u'6 mins'], [u'0.5 mi', u'3 mins'], [u'1.7 mi', u'3 mins'], [u'1.2 mi', u'5 mins'], [u'1.4 mi', u'7 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'3 mins'], [u'0.9 mi', u'3 mins'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.6 mi', u'2 mins'], [u'0.6 mi', u'2 mins'], [u'0.6 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'2 mins']]


def get_u2():
    return u2

d3=[[u'0.6 mi', u'8 mins'], [u'1.0 mi', u'13 mins'], [u'0.7 mi', u'4 mins'], [u'0.6 mi', u'5 mins'], [u'0.8 mi', u'10 mins'], [u'1.4 mi', u'7 mins'], [u'1.2 mi', u'4 mins'], [u'1.7 mi', u'4 mins'], [u'0.4 mi', u'4 mins'], [u'1.0 mi', u'3 mins'], [u'1.8 mi', u'4 mins'], [u'0.4 mi', u'4 mins'], [u'0.4 mi', u'5 mins'], [u'0.3 mi', u'2 mins'], [u'1.3 mi', u'6 mins'], [u'0.4 mi', u'3 mins'], [u'0.3 mi', u'7 mins'], [u'0.3 mi', u'1 min'], [u'0.6 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'4 mins'], [u'0.7 mi', u'6 mins'], [u'0.7 mi', u'6 mins'], [u'0.6 mi', u'5 mins'], [u'0.5 mi', u'3 mins'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'5 mins']]

def get_d3():
    return d3

u3=[[u'0.4 mi', u'6 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.5 mi', u'4 mins'], [u'0.6 mi', u'5 mins'], [u'0.7 mi', u'6 mins'], [u'0.7 mi', u'6 mins'], [u'0.5 mi', u'4 mins'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'3 mins'], [u'0.6 mi', u'4 mins'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'4 mins'], [u'0.4 mi', u'4 mins'], [u'1.3 mi', u'4 mins'], [u'0.3 mi', u'2 mins'], [u'0.4 mi', u'5 mins'], [u'0.4 mi', u'4 mins'], [u'1.8 mi', u'8 mins'], [u'1.1 mi', u'6 mins'], [u'0.5 mi', u'3 mins'], [u'1.7 mi', u'3 mins'], [u'1.2 mi', u'5 mins'], [u'1.4 mi', u'7 mins'], [u'0.8 mi', u'10 mins'], [u'0.6 mi', u'4 mins'], [u'0.7 mi', u'5 mins'], [u'1.0 mi', u'13 mins'], [u'0.3 mi', u'6 mins']]

def get_u3():
    return u3

d4=[[u'0.5 mi', u'2 mins'], [u'0.5 mi', u'1 min'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'2 mins'], [u'0.3 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'2 mins'], [u'0.9 mi', u'7 mins'], [u'0.7 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.7 mi', u'2 mins'], [u'2.0 mi', u'9 mins'], [u'1.4 mi', u'6 mins'], [u'1.0 mi', u'4 mins'], [u'1.5 mi', u'5 mins'], [u'2.1 mi', u'11 mins'], [u'0.8 mi', u'6 mins'], [u'0.3 mi', u'2 mins'], [u'0.3 mi', u'2 mins'], [u'1.8 mi', u'6 mins'], [u'0.6 mi', u'2 mins'], [u'0.6 mi', u'3 mins'], [u'1.6 mi', u'7 mins'], [u'1.3931142 mi', u'9 mins'], [u'1.32600612 mi', u'5 mins'], [u'1.4 mi', u'8 mins']]

def get_d4():
    return d4

u4=[[u'1.4 mi', u'8 mins'], [u'1.32600612 mi', u'8 mins'], [u'1.3931142 mi', u'7 mins'], [u'1.6 mi', u'6 mins'], [u'0.6 mi', u'4 mins'], [u'0.6 mi', u'1 min'], [u'1.7 mi', u'6 mins'], [u'0.3 mi', u'2 mins'], [u'0.2 mi', u'5 mins'], [u'0.8 mi', u'6 mins'], [u'2.1 mi', u'11 mins'], [u'1.5 mi', u'4 mins'], [u'1.0 mi', u'4 mins'], [u'1.4 mi', u'6 mins'], [u'2.0 mi', u'8 mins'], [u'0.7 mi', u'3 mins'], [u'0.4 mi', u'1 min'], [u'0.7 mi', u'2 mins'], [u'0.6 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.3 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'1 min'], [u'0.5 mi', u'1 min'], [u'0.5 mi', u'10 mins']]

def get_u4():
    return u4

d5=[[u'1.0 mi', u'10 mins'], [u'1.2 mi', u'13 mins'], [u'1.0 mi', u'6 mins'], [u'0.4 mi', u'1 min'], [u'1.1 mi', u'3 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.9 mi', u'3 mins'], [u'0.5 mi', u'2 mins'], [u'2.5 mi', u'19 mins'], [u'1.4 mi', u'6 mins'], [u'1.0 mi', u'4 mins'], [u'1.5 mi', u'5 mins'], [u'2.1 mi', u'11 mins'], [u'0.8 mi', u'6 mins'], [u'0.3 mi', u'2 mins'], [u'0.3 mi', u'2 mins'], [u'1.8 mi', u'6 mins'], [u'0.6 mi', u'2 mins'], [u'0.6 mi', u'3 mins'], [u'1.6 mi', u'8 mins'], [u'0.5 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.6 mi', u'5 mins'], [u'0.5 mi', u'4 mins'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'2 mins']]

def get_d5():
    return d5

u5=[[u'0.5 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'3 mins'], [u'0.6 mi', u'5 mins'], [u'0.4 mi', u'3 mins'], [u'0.6 mi', u'4 mins'], [u'1.6 mi', u'6 mins'], [u'0.6 mi', u'3 mins'], [u'0.6 mi', u'1 min'], [u'1.7 mi', u'6 mins'], [u'0.3 mi', u'2 mins'], [u'0.2 mi', u'5 mins'], [u'0.8 mi', u'6 mins'], [u'2.1 mi', u'11 mins'], [u'1.5 mi', u'4 mins'], [u'1.0 mi', u'4 mins'], [u'1.4 mi', u'6 mins'], [u'2.5 mi', u'18 mins'], [u'0.5 mi', u'2 mins'], [u'0.9 mi', u'3 mins'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'1 min'], [u'1.1 mi', u'3 mins'], [u'0.4 mi', u'1 min'], [u'1.0 mi', u'6 mins'], [u'1.2 mi', u'13 mins'], [u'1.0 mi', u'11 mins']]

def get_u5():
    return u5

d6=[[u'0.6 mi', u'5 mins'], [u'0.3 mi', u'1 min'], [u'0.5 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'3 mins'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'2 mins'], [u'0.3 mi', u'1 min'], [u'0.5 mi', u'4 mins'], [u'0.6 mi', u'5 mins'], [u'0.5 mi', u'2 mins'], [u'0.6 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.5 mi', u'4 mins'], [u'0.3 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.9 mi', u'3 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.5 mi', u'3 mins'], [u'0.5 mi', u'2 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'3 mins'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'4 mins'], [u'0.4 mi', u'4 mins'], [u'0.4 mi', u'4 mins'], [u'0.6 mi', u'4 mins'], [u'0.5 mi', u'2 mins'], [u'0.5 mi', u'5 mins'], [u'0.5 mi', u'4 mins'], [u'0.4 mi', u'3 mins'], [u'0.7 mi', u'6 mins']]

def get_d6():
    return d6

u6=[[u'0.7 mi', u'6 mins'], [u'0.7 mi', u'6 mins'], [u'0.5 mi', u'4 mins'], [u'0.8 mi', u'6 mins'], [u'0.5 mi', u'3 mins'], [u'0.6 mi', u'5 mins'], [u'0.4 mi', u'4 mins'], [u'0.4 mi', u'4 mins'], [u'0.5 mi', u'4 mins'], [u'0.5 mi', u'1 min'], [u'0.5 mi', u'3 mins'], [u'0.5 mi', u'3 mins'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'3 mins'], [u'0.5 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.4 mi', u'2 mins'], [u'0.5 mi', u'2 mins'], [u'0.9 mi', u'3 mins'], [u'0.4 mi', u'3 mins'], [u'0.3 mi', u'2 mins'], [u'0.5 mi', u'4 mins'], [u'0.4 mi', u'3 mins'], [u'0.6 mi', u'3 mins'], [u'0.5 mi', u'2 mins'], [u'0.6 mi', u'4 mins'], [u'0.5 mi', u'5 mins'], [u'0.3 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.4 mi', u'1 min'], [u'0.5 mi', u'3 mins'], [u'0.4 mi', u'2 mins'], [u'0.4 mi', u'3 mins'], [u'0.5 mi', u'3 mins'], [u'0.3 mi', u'1 min'], [u'0.6 mi', u'6 mins']]

def get_u6():
    return u6

def get_possible_trains(station_name, l):
    trains = []
    for station in l:
        if station[0] == station_name:
            if len(station[3]) > len(trains):
                trains = station[3]
    return trains

def find_remove(s, list):
    for i in range(len(list)):
        if list[i][0] == s:
            return i
    return -1

all_trains = [['Van Cortlandt Park - 242 St', '40.889248', '-73.898583', ['1']], ['238 St', '40.884667', '-73.90087', ['1']], ['231 St', '40.878856', '-73.904834', ['1']], ['Marble Hill - 225 St', '40.874561', '-73.909831', ['1']], ['215 St', '40.869444', '-73.915279', ['1']], ['207 St', '40.864621', '-73.918822', ['1']], ['Dyckman St', '40.860531', '-73.925536', ['1']], ['191 St', '40.855225', '-73.929412', ['1']], ['181 St', '40.849505', '-73.933596', ['1']], ['168 St - Washington Hts', '40.840556', '-73.940133', ['1']], ['157 St', '40.834041', '-73.94489', ['1']], ['145 St', '40.826551', '-73.95036', ['1']], ['137 St - City College', '40.822008', '-73.953676', ['1']], ['125 St', '40.815581', '-73.958372', ['1']], ['116 St - Columbia University', '40.807722', '-73.96411', ['1']], ['Cathedral Pkwy', '40.803967', '-73.966847', ['1']], ['103 St', '40.799446', '-73.968379', ['1']], ['96 St', '40.793919', '-73.972323', ['1', '2', '3']], ['86 St', '40.788644', '-73.976218', ['1']], ['79 St', '40.783934', '-73.979917', ['1']], ['72 St', '40.778453', '-73.98197', ['1', '2', '3']], ['66 St - Lincoln Center', '40.77344', '-73.982209', ['1']], ['59 St - Columbus Circle', '40.768247', '-73.981929', ['1']], ['50 St', '40.761728', '-73.983849', ['1']], ['Times Sq - 42 St', '40.75529', '-73.987495', ['1', '2', '3']], ['34 St - Penn Station', '40.750373', '-73.991057', ['1', '2', '3']], ['28 St', '40.747215', '-73.993365', ['1']], ['23 St', '40.744081', '-73.995657', ['1']], ['18 St', '40.74104', '-73.997871', ['1']], ['14 St', '40.737826', '-74.000201', ['1', '2', '3']], ['Christopher St - Sheridan Sq', '40.733422', '-74.002906', ['1']], ['Houston St', '40.728251', '-74.005367', ['1']], ['Canal St', '40.722854', '-74.006277', ['1']], ['Franklin St', '40.719318', '-74.006886', ['1']], ['Chambers St', '40.715478', '-74.009266', ['1', '2', '3']], ['Cortlandt St', '40.711835', '-74.012188', ['1']], ['Rector St', '40.707513', '-74.013783', ['1']], ['South Ferry Loop', '40.701411', '-74.013205', ['1']], ['Wakefield - 241 St', '40.903125', '-73.85062', ['2']], ['Nereid Av', '40.898379', '-73.854376', ['2']], ['233 St', '40.893193', '-73.857473', ['2']], ['225 St', '40.888022', '-73.860341', ['2']], ['219 St', '40.883895', '-73.862633', ['2']], ['Gun Hill Rd', '40.87785', '-73.866256', ['2', '5']], ['Burke Av', '40.871356', '-73.867164', ['2']], ['Allerton Av', '40.865462', '-73.867352', ['2']], ['Pelham Pkwy', '40.857192', '-73.867615', ['2']], ['Bronx Park East', '40.848828', '-73.868457', ['2']], ['E 180 St', '40.841894', '-73.873488', ['2', '5']], ['West Farms Sq - E Tremont Av', '40.840295', '-73.880049', ['2', '5']], ['174 St', '40.837288', '-73.887734', ['2', '5']], ['Freeman St', '40.829993', '-73.891865', ['2']], ['Simpson St', '40.824073', '-73.893064', ['2']], ['Intervale Av', '40.822181', '-73.896736', ['2']], ['Prospect Av', '40.819585', '-73.90177', ['2']], ['Jackson Av', '40.81649', '-73.907807', ['2']], ['3 Av - 149 St', '40.816109', '-73.917757', ['2', '5']], ['149 St - Grand Concourse', '40.81841', '-73.926718', ['2', '4', '5']], ['135 St', '40.814229', '-73.94077', ['2', '3']], ['125 St', '40.807754', '-73.945495', ['2']], ['116 St', '40.802098', '-73.949625', ['2']], ['Central Park North (110 St)', '40.799075', '-73.951822', ['2']], ['Park Pl', '40.713051', '-74.008811', ['2', '3']], ['Fulton St', '40.709416', '-74.006571', ['2', '3', '4', '5']], ['Wall St', '40.706821', '-74.0091', ['2', '3']], ['Clark St', '40.697466', '-73.993086', ['2', '3']], ['Borough Hall', '40.693219', '-73.989998', ['2', '3', '4', '5']], ['Hoyt St', '40.690545', '-73.985065', ['2', '3']], ['Nevins St', '40.688246', '-73.980492', ['2', '3', '4', '5']], ['Atlantic Av - Barclays Ctr', '40.684359', '-73.977666', ['2', '3', '4', '5']], ['Bergen St', '40.680829', '-73.975098', ['2', '3']], ['Grand Army Plaza', '40.675235', '-73.971046', ['2', '3']], ['Eastern Pkwy - Brooklyn Museum', '40.671987', '-73.964375', ['2', '3']], ['Franklin Av', '40.670682', '-73.958131', ['2', '3', '4', '5']], ['President St', '40.667883', '-73.950683', ['2']], ['Sterling St', '40.662742', '-73.95085', ['2']], ['Winthrop St', '40.656652', '-73.9502', ['2']], ['Church Av', '40.650843', '-73.949575', ['2']], ['Beverly Rd', '40.645098', '-73.948959', ['2']], ['Newkirk Av', '40.639967', '-73.948411', ['2']], ['Flatbush Av - Brooklyn College', '40.632836', '-73.947642', ['2', '5']], ['Harlem - 148 St', '40.82388', '-73.93647', ['3']], ['145 St', '40.820421', '-73.936245', ['3']], ['125 St', '40.811109', '-73.952343', ['3']], ['116 St', '40.805085', '-73.954882', ['3']], ['Central Park North (110 St)', '40.799075', '-73.951822', ['3']], ['Nostrand Av', '40.669847', '-73.950466', ['3']], ['Kingston Av', '40.669399', '-73.942161', ['3']], ['Crown Hts - Utica Av', '40.668897', '-73.932942', ['3', '4']], ['Sutter Av - Rutland Rd', '40.664717', '-73.92261', ['3']], ['Saratoga Av', '40.661453', '-73.916327', ['3']], ['Rockaway Av', '40.662549', '-73.908946', ['3']], ['Junius St', '40.663515', '-73.902447', ['3']], ['Pennsylvania Av', '40.664635', '-73.894895', ['3']], ['Van Siclen Av', '40.665449', '-73.889395', ['3']], ['New Lots Av', '40.666235', '-73.884079', ['3']], ['Woodlawn', '40.886037', '-73.878751', ['4']], ['Mosholu Pkwy', '40.87975', '-73.884655', ['4']], ['Bedford Park Blvd - Lehman College', '40.873412', '-73.890064', ['4']], ['Kingsbridge Rd', '40.86776', '-73.897174', ['4']], ['Fordham Rd', '40.862803', '-73.901034', ['4']], ['183 St', '40.858407', '-73.903879', ['4']], ['Burnside Av', '40.853453', '-73.907684', ['4']], ['176 St', '40.84848', '-73.911794', ['4']], ['Mt Eden Av', '40.844434', '-73.914685', ['4']], ['170 St', '40.840075', '-73.917791', ['4']], ['167 St', '40.835537', '-73.9214', ['4']], ['161 St - Yankee Stadium', '40.827994', '-73.925831', ['4']], ['138 St - Grand Concourse', '40.813224', '-73.929849', ['4', '5']], ['125 St', '40.804138', '-73.937594', ['4', '5', '6']], ['86 St', '40.779492', '-73.955589', ['4', '5', '6']], ['59 St', '40.762526', '-73.967967', ['4', '5', '6']], ['Grand Central - 42 St', '40.751776', '-73.976848', ['4', '5', '6']], ['14 St - Union Sq', '40.734673', '-73.989951', ['4', '5', '6']], ['Brooklyn Bridge - City Hall', '40.713065', '-74.004131', ['4', '5', '6']], ['Wall St', '40.707557', '-74.011862', ['4', '5']], ['Bowling Green', '40.704817', '-74.014065', ['4', '5']], ['Eastchester - Dyre Av', '40.8883', '-73.830834', ['5']], ['Baychester Av', '40.878663', '-73.838591', ['5']], ['Pelham Pkwy', '40.858985', '-73.855359', ['5']], ['Morris Park', '40.854364', '-73.860495', ['5']], ['Freeman St', '40.829993', '-73.891865', ['5']], ['Simpson St', '40.824073', '-73.893064', ['5']], ['Intervale Av', '40.822181', '-73.896736', ['5']], ['Prospect Av', '40.819585', '-73.90177', ['5']], ['Jackson Av', '40.81649', '-73.907807', ['5']], ['President St', '40.667883', '-73.950683', ['5']], ['Sterling St', '40.662742', '-73.95085', ['5']], ['Winthrop St', '40.656652', '-73.9502', ['5']], ['Church Av', '40.650843', '-73.949575', ['5']], ['Beverly Rd', '40.645098', '-73.948959', ['5']], ['Newkirk Av', '40.639967', '-73.948411', ['5']], ['Pelham Bay Park', '40.852462', '-73.828121', ['6']], ['Buhre Av', '40.84681', '-73.832569', ['6']], ['Middletown Rd', '40.843863', '-73.836322', ['6']], ['Westchester Sq - E Tremont Av', '40.839892', '-73.842952', ['6']], ['Zerega Av', '40.836488', '-73.847036', ['6']], ['Castle Hill Av', '40.834255', '-73.851222', ['6']], ['Parkchester', '40.833226', '-73.860816', ['6']], ['St Lawrence Av', '40.831509', '-73.867618', ['6']], ['Morrison Av- Sound View', '40.829521', '-73.874516', ['6']], ['Elder Av', '40.828584', '-73.879159', ['6']], ['Whitlock Av', '40.826525', '-73.886283', ['6']], ['Hunts Point Av', '40.820948', '-73.890549', ['6']], ['Longwood Av', '40.816104', '-73.896435', ['6']], ['E 149 St', '40.812118', '-73.904098', ['6']], ["E 143 St - St Mary's St", '40.808719', '-73.907657', ['6']], ['Cypress Av', '40.805368', '-73.914042', ['6']], ['Brook Av', '40.807566', '-73.91924', ['6']], ['3 Av - 138 St', '40.810476', '-73.926138', ['6']], ['116 St', '40.798629', '-73.941617', ['6']], ['110 St', '40.79502', '-73.94425', ['6']], ['103 St', '40.7906', '-73.947478', ['6']], ['96 St', '40.785672', '-73.95107', ['6']], ['77 St', '40.77362', '-73.959874', ['6']], ['68 St - Hunter College', '40.768141', '-73.96387', ['6']], ['51 St', '40.757107', '-73.97192', ['6']], ['33 St', '40.746081', '-73.982076', ['6']], ['28 St', '40.74307', '-73.984264', ['6']], ['23 St', '40.739864', '-73.986599', ['6']], ['Astor Pl', '40.730054', '-73.99107', ['6']], ['Broadway-Lafayette St', '40.725297', '-73.996204', ['4', '6']], ['Spring St', '40.722301', '-73.997141', ['6']], ['Canal St', '40.718803', '-74.000193', ['4', '6']]]

def give_all():
    return all_trains
    # all_trains = [ get_one(), get_two(), get_three(), get_four(), get_five(), get_six() ]
    # short = []
    # l = 0
    # while (len(all_trains[0]) > 0 or len(all_trains[1]) > 0 or len(all_trains[2]) > 0 or len(all_trains[3]) > 0 or len(all_trains[4]) > 0 or len(all_trains[5]) > 0):
    #     while len(all_trains[l]) > 0:
    #         # print all_trains[l]
    #         s = all_trains[l][0][0]
    #         for num in all_trains[l][0][3]:
    #             x = find_remove(s, all_trains[int(num)-1])
    #             if x > -1:
    #                 if int(num) - 1 == l:
    #                     short.append(all_trains[int(num)-1].pop(x))
    #                 else:
    #                     all_trains[int(num)-1].pop(x)
    #         # print short
    #     l += 1
    # return short

# print give_all()
#print get_possible_trains("Chambers St")
#print get_possible_trains("Atlantic Av - Barclays Ctr")
