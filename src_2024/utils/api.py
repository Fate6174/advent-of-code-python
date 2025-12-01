import requests
from os.path import exists
from bs4 import BeautifulSoup, Tag

def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()


def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"

def get_name_url(year, day):
    return f'https://adventofcode.com/{year}/day/{day}'

YEAR = 2024
SESSION_ID_FILE = "session.cookie"
SESSION = get_session_id(SESSION_ID_FILE)
HEADERS = {
    "User-Agent": "github.com/tomfran/advent-of-code-setup reddit:u/fran-sch, discord:@tomfran#5786"
}
COOKIES = {"session": SESSION}


def get_input(day):
    path = f"inputs/{day:02d}"

    if not exists(path):
        url = get_url(YEAR, day)
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(path, "w") as f:
            f.write(response.text[:-1])

    with open(path, "r") as f:
        return f.read()

def get_name(day):
    path = f'names/{day:02d}'
    
    if not exists(path):
        url = get_name_url(YEAR, day)
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        
        puzzle_page = BeautifulSoup(response.text, 'html.parser')
        puzzle_title_h2 = puzzle_page.find('h2')
        if puzzle_title_h2 is None or not isinstance(puzzle_title_h2, Tag):
            raise RuntimeError(
                f"Could not parse given webpage - Puzzle title not found."
            )
        puzzle_title_h2.get_text()
        
        with open(path, "w") as f:
            f.write(puzzle_title_h2.get_text()[4:-4])
    
    with open(path, "r") as f:
        return f.read()