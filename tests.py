from main import get_country_info, get_countries_by_language, get_countries_by_continent

def test_get_country_by_name():
    assert get_country_info("brazil") == '''Name: Brazil
Capital: Brasília
Region: Americas
Population: 212 million'''

    assert get_country_info("mexico") == '''Name: Mexico
Capital: Mexico City
Region: Americas
Population: 128 million'''

assert get_country_info("pakistan") == '''Name: Pakistan
Capital: Islamabad
Region: Asia
Population: 220 million'''

def test_get_countries_by_language():
    assert get_countries_by_language("Spanish") == "The following countries have Spanish as an official language: Argentina, Belize, Bolivia, Chile, Colombia, Costa Rica, Cuba, Dominican Republic, Ecuador, El Salvador, Equatorial Guinea, Guam, Guatemala, Honduras, Mexico, Nicaragua, Panama, Paraguay, Peru, Puerto Rico, Spain, Uruguay, Venezuela, Western Sahara."

    assert get_countries_by_language("French") == "The following countries have French as an official language: Belgium, Benin, Burkina Faso, Burundi, Cameroon, Canada, Central African Republic, Chad, Comoros, DR Congo, Djibouti, Equatorial Guinea, France, French Guiana, French Polynesia, French Southern and Antarctic Lands, Gabon, Guadeloupe, Guernsey, Guinea, Haiti, Ivory Coast, Jersey, Lebanon, Luxembourg, Madagascar, Mali, Martinique, Mauritius, Mayotte, Monaco, New Caledonia, Niger, Republic of the Congo, Rwanda, Réunion, Saint Barthélemy, Saint Martin, Saint Pierre and Miquelon, Senegal, Seychelles, Sint Maarten, Switzerland, Togo, Vanuatu, Wallis and Futuna."

    assert get_countries_by_language("Hindi") == "The following countries have Hindi as an official language: India."

def test_get_countries_by_continent():
    response = get_countries_by_continent("Pangaea")
    assert response == "Unable to retrieve countries in Pangaea."

    assert get_countries_by_continent("Antarctica") == "There are no countries in Antarctica."


