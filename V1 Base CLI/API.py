import requests
import json
import difflib


def search_city(country_name):
    ISO_CTR = {
      "AF": "Afghanistan",
      "AX": "Aland Islands",
      "AL": "Albania",
      "DZ": "Algeria",
      "AS": "American Samoa",
      "AD": "Andorra",
      "AO": "Angola",
      "AI": "Anguilla",
      "AQ": "Antarctica",
      "AG": "Antigua And Barbuda",
      "AR": "Argentina",
      "AM": "Armenia",
      "AW": "Aruba",
      "AU": "Australia",
      "AT": "Austria",
      "AZ": "Azerbaijan",
      "BS": "Bahamas",
      "BH": "Bahrain",
      "BD": "Bangladesh",
      "BB": "Barbados",
      "BY": "Belarus",
      "BE": "Belgium",
      "BZ": "Belize",
      "BJ": "Benin",
      "BM": "Bermuda",
      "BT": "Bhutan",
      "BO": "Bolivia",
      "BA": "Bosnia And Herzegovina",
      "BW": "Botswana",
      "BV": "Bouvet Island",
      "BR": "Brazil",
      "IO": "British Indian Ocean Territory",
      "BN": "Brunei Darussalam",
      "BG": "Bulgaria",
      "BF": "Burkina Faso",
      "BI": "Burundi",
      "KH": "Cambodia",
      "CM": "Cameroon",
      "CA": "Canada",
      "CV": "Cape Verde",
      "KY": "Cayman Islands",
      "CF": "Central African Republic",
      "TD": "Chad",
      "CL": "Chile",
      "CN": "China",
      "CX": "Christmas Island",
      "CC": "Cocos (Keeling) Islands",
      "CO": "Colombia",
      "KM": "Comoros",
      "CG": "Congo",
      "CD": "Congo, Democratic Republic",
      "CK": "Cook Islands",
      "CR": "Costa Rica",
      "CI": "Cote D\"Ivoire",
      "HR": "Croatia",
      "CU": "Cuba",
      "CY": "Cyprus",
      "CZ": "Czech Republic",
      "DK": "Denmark",
      "DJ": "Djibouti",
      "DM": "Dominica",
      "DO": "Dominican Republic",
      "EC": "Ecuador",
      "EG": "Egypt",
      "SV": "El Salvador",
      "GQ": "Equatorial Guinea",
      "ER": "Eritrea",
      "EE": "Estonia",
      "ET": "Ethiopia",
      "FK": "Falkland Islands (Malvinas)",
      "FO": "Faroe Islands",
      "FJ": "Fiji",
      "FI": "Finland",
      "FR": "France",
      "GF": "French Guiana",
      "PF": "French Polynesia",
      "TF": "French Southern Territories",
      "GA": "Gabon",
      "GM": "Gambia",
      "GE": "Georgia",
      "DE": "Germany",
      "GH": "Ghana",
      "GI": "Gibraltar",
      "GR": "Greece",
      "GL": "Greenland",
      "GD": "Grenada",
      "GP": "Guadeloupe",
      "GU": "Guam",
      "GT": "Guatemala",
      "GG": "Guernsey",
      "GN": "Guinea",
      "GW": "Guinea-Bissau",
      "GY": "Guyana",
      "HT": "Haiti",
      "HM": "Heard Island & Mcdonald Islands",
      "VA": "Holy See (Vatican City State)",
      "HN": "Honduras",
      "HK": "Hong Kong",
      "HU": "Hungary",
      "IS": "Iceland",
      "IN": "India",
      "ID": "Indonesia",
      "IR": "Iran, Islamic Republic Of",
      "IQ": "Iraq",
      "IE": "Ireland",
      "IM": "Isle Of Man",
      "IL": "Israel",
      "IT": "Italy",
      "JM": "Jamaica",
      "JP": "Japan",
      "JE": "Jersey",
      "JO": "Jordan",
      "KZ": "Kazakhstan",
      "KE": "Kenya",
      "KI": "Kiribati",
      "KR": "Korea",
      "KP": "North Korea",
      "KW": "Kuwait",
      "KG": "Kyrgyzstan",
      "LA": "Lao People\"s Democratic Republic",
      "LV": "Latvia",
      "LB": "Lebanon",
      "LS": "Lesotho",
      "LR": "Liberia",
      "LY": "Libyan Arab Jamahiriya",
      "LI": "Liechtenstein",
      "LT": "Lithuania",
      "LU": "Luxembourg",
      "MO": "Macao",
      "MK": "Macedonia",
      "MG": "Madagascar",
      "MW": "Malawi",
      "MY": "Malaysia",
      "MV": "Maldives",
      "ML": "Mali",
      "MT": "Malta",
      "MH": "Marshall Islands",
      "MQ": "Martinique",
      "MR": "Mauritania",
      "MU": "Mauritius",
      "YT": "Mayotte",
      "MX": "Mexico",
      "FM": "Micronesia, Federated States Of",
      "MD": "Moldova",
      "MC": "Monaco",
      "MN": "Mongolia",
      "ME": "Montenegro",
      "MS": "Montserrat",
      "MA": "Morocco",
      "MZ": "Mozambique",
      "MM": "Myanmar",
      "NA": "Namibia",
      "NR": "Nauru",
      "NP": "Nepal",
      "NL": "Netherlands",
      "AN": "Netherlands Antilles",
      "NC": "New Caledonia",
      "NZ": "New Zealand",
      "NI": "Nicaragua",
      "NE": "Niger",
      "NG": "Nigeria",
      "NU": "Niue",
      "NF": "Norfolk Island",
      "MP": "Northern Mariana Islands",
      "NO": "Norway",
      "OM": "Oman",
      "PK": "Pakistan",
      "PW": "Palau",
      "PS": "Palestinian Territory, Occupied",
      "PA": "Panama",
      "PG": "Papua New Guinea",
      "PY": "Paraguay",
      "PE": "Peru",
      "PH": "Philippines",
      "PN": "Pitcairn",
      "PL": "Poland",
      "PT": "Portugal",
      "PR": "Puerto Rico",
      "QA": "Qatar",
      "RE": "Reunion",
      "RO": "Romania",
      "RU": "Russian Federation",
      "RW": "Rwanda",
      "BL": "Saint Barthelemy",
      "SH": "Saint Helena",
      "KN": "Saint Kitts And Nevis",
      "LC": "Saint Lucia",
      "MF": "Saint Martin",
      "PM": "Saint Pierre And Miquelon",
      "VC": "Saint Vincent And Grenadines",
      "WS": "Samoa",
      "SM": "San Marino",
      "ST": "Sao Tome And Principe",
      "SA": "Saudi Arabia",
      "SN": "Senegal",
      "RS": "Serbia",
      "SC": "Seychelles",
      "SL": "Sierra Leone",
      "SG": "Singapore",
      "SK": "Slovakia",
      "SI": "Slovenia",
      "SB": "Solomon Islands",
      "SO": "Somalia",
      "ZA": "South Africa",
      "GS": "South Georgia And Sandwich Isl.",
      "ES": "Spain",
      "LK": "Sri Lanka",
      "SD": "Sudan",
      "SR": "Suriname",
      "SJ": "Svalbard And Jan Mayen",
      "SZ": "Swaziland",
      "SE": "Sweden",
      "CH": "Switzerland",
      "SY": "Syrian Arab Republic",
      "TW": "Taiwan",
      "TJ": "Tajikistan",
      "TZ": "Tanzania",
      "TH": "Thailand",
      "TL": "Timor-Leste",
      "TG": "Togo",
      "TK": "Tokelau",
      "TO": "Tonga",
      "TT": "Trinidad And Tobago",
      "TN": "Tunisia",
      "TR": "Turkey",
      "TM": "Turkmenistan",
      "TC": "Turks And Caicos Islands",
      "TV": "Tuvalu",
      "UG": "Uganda",
      "UA": "Ukraine",
      "AE": "United Arab Emirates",
      "GB": "United Kingdom",
      "US": "United States",
      "UM": "United States Outlying Islands",
      "UY": "Uruguay",
      "UZ": "Uzbekistan",
      "VU": "Vanuatu",
      "VE": "Venezuela",
      "VN": "Vietnam",
      "VG": "Virgin Islands, British",
      "VI": "Virgin Islands, U.S.",
      "WF": "Wallis And Futuna",
      "EH": "Western Sahara",
      "YE": "Yemen",
      "ZM": "Zambia",
      "ZW": "Zimbabwe"
    }
    country_name = ISO_CTR[country_name]

    url = "https://countriesnow.space/api/v0.1/countries/cities"
    payload = {"country": country_name}
    headers = {'Content-Type': 'application/json'}

    print(f"Récupération des villes pour {country_name.capitalize()}...")
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        data = response.json()

        if data.get('error') or not data.get('data'):
            print(f"Impossible de récupérer la liste des villes pour '{country_name}'.")
            print(f"Message de l'API : {data.get('msg')}")
            return "Recherche abandonnée."
        
        cities_list = data['data']

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion à l'API : {e}")
        return "Recherche abandonnée."


    recherche_actuelle = input(f"\nEntrez le nom de la ville en {country_name.capitalize()} : ")

    while True:
        correspondances = difflib.get_close_matches(recherche_actuelle, cities_list, n=5, cutoff=0.5)

        if not correspondances:
            print(f"Aucun résultat pour '{recherche_actuelle}'.")
            choix = input("Appuyez sur 'x' pour refaire une recherche ou Entrée pour quitter : ")
            if choix.lower() == 'x':
                recherche_actuelle = input("\nEntrez le nom de la ville : ")
                continue 
            else:
                return "Recherche abandonnée."


        print(f"\nRésultats pour '{recherche_actuelle}' :")
        for index, nom_ville in enumerate(correspondances):
            print(f" {index + 1} -> {nom_ville}")
        
        print(" x -> Faire une nouvelle recherche") 

        choix = input("\nVotre choix (numéro ou x) : ")

        if choix.lower() == 'x':
            recherche_actuelle = input("Entrez le nom de la ville : ")
            continue 

        try:
            index_choisi = int(choix) - 1
            
            if 0 <= index_choisi < len(correspondances):
                ville_selectionnee = correspondances[index_choisi]
                print(f"Sélectionné : {ville_selectionnee}")
                return ville_selectionnee
            else:
                print("Numéro invalide, réessayez.")
                
        except ValueError:
            print("Erreur : Veuillez entrer un numéro valide ou 'x'.")


if __name__ == '__main__':

    pays_selectionne = "France"
    
    ville_choisie = search_city(pays_selectionne)

    if ville_choisie != "Recherche abandonnée.":
        print(f"\n--- Processus de test terminé ---")
        print(f"Pays : {pays_selectionne}")
        print(f"Ville : {ville_choisie}")
        print(f"Vous pouvez maintenant utiliser '{ville_choisie}' pour appeler une API météo.")
