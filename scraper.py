from bs4 import BeautifulSoup
import requests
import db.controller as dbc


def scrape(_input:str="-1") -> None:
    """"""
    print("----------------")

    if _input == "-1":
        wrd_input = input("Enter Word (JP): ")
    else:
        wrd_input = _input
        print(f"using input {wrd_input}")

    url = "https://jisho.org/search/" + str(wrd_input)

    print(f"Scraping, URL: {url}")

    response = requests.get(url)
    if not response:
        return print("Error: couldn't request URL")

    soup = BeautifulSoup(response.text, "html.parser")
    if not soup:
        return print("Error: couldn't scrape url.")

    print("----------------")

    # Get/Find first jisho entry
    jisho_entry_block = soup.find("div", class_="exact_block")
    if not jisho_entry_block:
        return print("No div with class 'exact_block' found.")

    # Step 2: Get the first concept_light inside it
    first_entry = jisho_entry_block.find("div", class_="concept_light") # type: ignore
    if not first_entry:
        print("No entries found for this word.")
        return print("No div with class 'concept_light' found inside exact_block.")

    # Kanji / Input
    wrd_kanji = first_entry.find("span", class_="text") # type: ignore
    formatted_kanji:str = "-"
    if wrd_kanji:
        formatted_kanji = wrd_kanji.text.strip()
        print(f"Word (Kanji): {formatted_kanji}")
        if formatted_kanji != wrd_input:
            print(f"-> Warning: Found word ({formatted_kanji}) differs from Input ({wrd_input})")
            # @TODO maybe ask to continue ?

    # Furigana
    furigana = first_entry.find_all("span", class_="furigana") # type: ignore
    formatted_furigana:str = "-"
    if furigana[0].text:
        formatted_furigana = furigana[0].text.strip()
        print(f"Furigana: {formatted_furigana}")

    # Meaning
    meaning_wrapper = first_entry.find("div", class_="meaning-definition") # type: ignore
    meanings = meaning_wrapper.find_all("span", class_="meaning-meaning") # type: ignore
    formatted_meanings:str = ""
    for i, f in enumerate(meanings, 1):
        m:str = f"Meaning {i}: {f.text.strip()}"
        print(m)
        formatted_meanings = formatted_meanings + str("||" + m)

    print("----------------")

    b_confirm = input("Save word? [Y/n]")

    t = ["", "y", "Y"]
    for i in t:
        if b_confirm == i:
            b_success:bool = dbc.db_create_vocab(
                wrd_kanji=formatted_kanji,
                wrd_furigana=formatted_furigana,
                meanings=formatted_meanings
            )
            print("Success.") if b_success else print("Failure.")

if __name__ == '__main__':
    dbc.db_init()
    scrape()