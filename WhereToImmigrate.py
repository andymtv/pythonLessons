visa_free_countries_string = '''
Azerbaijan (up to 90 days)
Albania (up to 90 days)
Antigua and Barbuda from 29 June 2018 of the year (up to 90 days for 180 days)
Argentina (up to 90 days)
Armenia
Belarus
Bosnia and Herzegovina (up to 30 days). You may need tickets back, host invitation or travel voucher.
Brazil (up to 90 days). May need return tickets
Brunei (up to 30 days). Be sure to have tickets in both directions.
Vanuatu (up to 30 days). Citizens of Ukraine entering Vanuatu for a period not exceeding 30 days do not need a visa, a visa stamp is placed directly at the border crossing point. You should have your tickets back, hotel reservations, a document confirming your solvency
Guatemala (up to 90 days). Return tickets are required.
Hong Kong (up to 14 days). Return tickets will be required
Grenada (up to 90 days). Available only with travel vouchers.
Georgia (up to 365 days)
Western Sahara
Israel (up to 90 days)
Indonesia (up to 30 days). You need a passport, valid for at least 6 more months from the date of arrival in the republic, as well as return tickets or tickets to another country.
Kazakhstan (up to 90 days)
Qatar (for a period not exceeding 90 days, for 180 days)
Kyrgyzstan (up to 90 days)
Costa Rica (up to 90 days). Since December 2016, a visa-free regime has been introduced for citizens of Ukraine. A requirement for entry into the country is the presence of a passport document, which must be valid for at least 90 days at the time of the intended departure from Costa Rica. When leaving the state, a US $ 29 fee must be paid, regardless of the type of traveler’s passport document.
Malaysia (up to 30 days). Have return tickets with you
Macedonia (up to 90 days). You will need an insurance policy
Micronesia (only for tourists with vouchers)
Moldova
Mongolia (up to 90 days). Invitation to host is required
Namibia (up to 90 days). Need a migration card filled out in English
Niue (up to 30 days). Looking for return tickets
Nicaragua
United Arab Emirates (31.12.2017 entered into force Memorandum on the mutual abolition of visas.
Visa-free visits to the UAE are available only to citizens with biometric passports that are valid for at least 6 months. Stay without a visa on the territory of the United Arab Emirates possibly up to 30 days
Ck (up to 31 of the day)
Panama (up to 90 days)
Paraguay (up to 90 days). Required return tickets
Peru (up to 90 days). Up to 183 days, subject to availability of documents confirming the tourist purpose of the trip
Pitcairn (on 14 days). In case of arrival and departure on the same vessel
Russia (up to 90 days). Also allowed to enter the territory of Russia on the ID-card
Samoa (up to 60 days)
Swaziland (up to 30 days)
Seychelles (up to 30 days). Return tickets and travel voucher required
Serbia (up to 90 days)
Saint kitts и
Nevis (up to 90 days). Since June 24, the Ukrainian government has adopted a draft agreement on the mutual abolition of the visa regime with Saint Kitts and Nevis
Tajikistan (up to 90 days)
Tunisia (up to 30 days). You should have a travel voucher with you.
Turkey (up to 90 days within 180 days from the date of entry). On request, you may need tickets back and a tourist voucher. Ukrainians can visit Turkey by ID-card
Uzbekistan
Montenegro (up to 90 days)
Chile (up to 90 days)
Spitsbergen
Ecuador (up to 90 days)
Jamaica (up to 30 days). You will need return tickets and proof of solvency.
Yan-Maen (visa-free, but you need to drive through the territory of Norway, visa for Ukrainians).
'''

all_countries_string = '''
Afghanistan
Albania
Algeria
Andorra
Angola
Antigua and Barbuda
Argentina
Armenia
Australia
Austria
Azerbaijan
B
The Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bhutan
Bolivia
Bosnia and Herzegovina
Botswana
Brazil
Brunei
Bulgaria
Burkina Faso
Burundi
C
Cabo Verde
Cambodia
Cameroon
Canada
Central African Republic
Chad
Chile
China
Colombia
Comoros
Congo, Democratic Republic of the
Congo, Republic of the
Costa Rica
Côte d’Ivoire
Croatia
Cuba
Cyprus
Czech Republic
D
Denmark
Djibouti
Dominica
Dominican Republic
E
East Timor (Timor-Leste)
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Eswatini
Ethiopia
F
Fiji
Finland
France
G
Gabon
The Gambia
Georgia
Germany
Ghana
Greece
Grenada
Guatemala
Guinea
Guinea-Bissau
Guyana
H
Haiti
Honduras
Hungary
I
Iceland
India
Indonesia
Iran
Iraq
Ireland
Israel
Italy
J
Jamaica
Japan
Jordan
K
Kazakhstan
Kenya
Kiribati
Korea North
Korea South
Kosovo
Kuwait
Kyrgyzstan
L
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
M
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Mauritania
Mauritius
Mexico
Micronesia
Federated States of
Moldova
Monaco
Mongolia
Montenegro
Morocco
Mozambique
Myanmar (Burma)
N
Namibia
Nauru
Nepal
Netherlands
New Zealand
Nicaragua
Niger
Nigeria
North Macedonia
Norway
O
Oman
P
Pakistan
Palau
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
Q
Qatar
R
Romania
Russia
Rwanda
S
Saint Kitts and Nevis
Saint Lucia
Saint Vincent and the Grenadines
Samoa
San Marino
Sao Tome and Principe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
Spain
Sri Lanka
Sudan
Sudan, South
Suriname
Sweden
Switzerland
Syria
T
Taiwan
Tajikistan
Tanzania
Thailand
Togo
Tonga
Trinidad and Tobago
Tunisia
Turkey
Turkmenistan
Tuvalu
U
Uganda
Ukraine
United Arab Emirates
United Kingdom
United States
Uruguay
Uzbekistan
V
Vanuatu
Vatican City
Venezuela
Vietnam
Y
Yemen
Z
Zambia
Zimbabwe
'''

english_native_countries_string = '''
Antigua and Barbuda
Australia
The Bahamas
Barbados
Belize
Canada
Dominica
Grenada
Guyana
Ireland
Jamaica
New Zealand
Saint Kitts and Nevis
Saint Lucia
Saint Vincent and the Grenadines
Trinidad and Tobago
United Kingdom
United States of America
'''

all_countries_list = list(all_countries_string.split('\n'))


visa_free_countries_list = list(visa_free_countries_string.split('\n'))

english_native_countries_list = list(english_native_countries_string.split('\n'))

for item in all_countries_list:
    if len(item) < 2:
        all_countries_list.remove(item)
    else:
        continue

for item in visa_free_countries_list:
    if len(item) < 2:
        visa_free_countries_list.remove(item)
    else:
        continue

for item in english_native_countries_list:
    if len(item) < 2:
        english_native_countries_list.remove(item)
    else:
        continue

new_list = []
for item in visa_free_countries_list:
    for elem in all_countries_list:
        if elem in item[0: 25]:
            item = elem
            new_list.append(item)

visa_free_countries_list = new_list
for item in visa_free_countries_list:
    print(visa_free_countries_list.index(item), item)

new_list2 = []
for item in visa_free_countries_list:
    for elem in english_native_countries_list:
        if elem in item[0: 25]:
            item = elem
            new_list2.append(item)

english_native_countries_list = new_list2

print(english_native_countries_list)
