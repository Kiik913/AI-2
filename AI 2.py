import webbrowser
from datetime import datetime, date
import os
import math
import urllib.parse
import subprocess

# ==============================
# CONFIGURATION
# ==============================

PERCHANCE_URL = "https://perchance.org/stable-diffusion-ai"
STABLE_DIFFUSION_WEB_URL = "https://stablediffusionweb.com"
WIKIPEDIA_URL = "https://www.wikipedia.org/"
WIKIPEDIA_SEARCH_BASE = "https://en.wikipedia.org/wiki/"

PROMPT_HISTORY_FILE = "prompts_history.txt"
FAVORITES_FILE = "favorites_prompts.txt"

# Fixed history folder on your Windows user account
HISTORY_DIR = r"C:\Users\HP\AI 2 History"
os.makedirs(HISTORY_DIR, exist_ok=True)
APP_HISTORY_FILE = os.path.join(HISTORY_DIR, "AI 2 history.txt")

# ==============================
# HISTORY LOGGER
# ==============================

def log_history(message: str) -> None:
    """Append a line to AI 2 history.txt with timestamp in fixed folder."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {message}\n"
    with open(APP_HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(line)

# ==============================
# SIMPLE CLIPBOARD (Windows)
# ==============================

def copy_to_clipboard(text: str) -> None:
    """
    Copy text to clipboard on Windows using 'clip' command.
    If it fails, just log the error and continue normally.
    """
    try:
        subprocess.run("clip", universal_newlines=True, input=text)
        log_history("Copied prompt to clipboard using clip command")
    except Exception as e:
        log_history(f"Clipboard copy failed: {e}")

# ==============================
# FESTIVALS (India 2026 + World Fixed-Date)
# ==============================

INDIA_FESTIVALS_2026 = {
    # January
    "01-01": ["New Year's Day"],
    "01-05": ["Guru Gobind Singh Jayanti"],
    "01-13": ["Lohri"],
    "01-14": ["Makar Sankranti", "Pongal Begins", "Magh Bihu"],
    "01-23": ["Vasant Panchami / Saraswati Puja"],
    "01-26": ["Republic Day"],

    # February
    "02-14": ["Valentine's Day"],
    "02-15": ["Maha Shivratri"],
    "02-19": ["Phulera Dooj"],
    "02-26": ["Holashtak Begins"],

    # March
    "03-03": ["Holika Dahan"],
    "03-04": ["Holi"],
    "03-06": ["Chapchar Kut (Mizoram)"],
    "03-17": ["St. Patrick's Day"],
    "03-19": ["Ugadi", "Gudi Padwa", "Chaitra Navratri Begins"],
    "03-20": ["Nowruz (Iran & Central Asia)", "Cheti Chand"],
    "03-21": ["Eid-ul-Fitr*"],
    "03-26": ["Ram Navami"],
    "03-31": ["Mahavir Jayanti"],

    # April
    "04-02": ["Hanuman Jayanti"],
    "04-03": ["Good Friday"],
    "04-05": ["Easter"],
    "04-14": ["Baisakhi", "Vishu", "Tamil New Year", "Ambedkar Jayanti"],
    "04-15": ["Pohela Boishakh", "Bohag Bihu"],
    "04-19": ["Akshaya Tritiya"],
    "04-26": ["Thrissur Pooram (Kerala)"],

    # May
    "05-01": ["Buddha Purnima", "International Workers' Day"],
    "05-02": ["Narada Jayanti"],
    "05-05": ["Cinco de Mayo (Mexico)"],
    "05-13": ["Apara Ekadashi"],
    "05-16": ["Vat Savitri Vrat"],
    "05-25": ["Ganga Dussehra"],
    "05-27": ["Eid-ul-Adha (some calendars place it in June)*"],
    "05-31": ["Jyeshtha Purnima"],

    # June
    "06-05": ["World Environment Day"],
    "06-11": ["Parama Ekadashi"],
    "06-17": ["Bakrid / Eid-ul-Adha*"],
    "06-21": ["International Day of Yoga"],
    "06-24": ["Inti Raymi (Peru)"],
    "06-26": ["Rath Yatra"],
    "06-29": ["Hemis Festival (Ladakh)"],
    "06-30": ["Hemis Festival (Ladakh)"],

    # July
    "07-01": ["Canada Day"],
    "07-04": ["Independence Day (USA)"],
    "07-14": ["Bastille Day (France)"],
    "07-16": ["Muharram / Ashura*"],
    "07-21": ["Guru Purnima"],
    "07-24": ["Nag Panchami"],

    # August
    "08-09": ["National Day (Singapore)"],
    "08-15": ["Independence Day (India)", "Hariyali Teej (Rajasthan, Haryana, UP)"],
    "08-16": ["Onam Festival (start, Kerala)"],
    "08-19": ["Raksha Bandhan"],
    "08-22": ["Kajari Teej (approx)"],
    "08-27": ["Janmashtami"],

    # September
    "09-04": ["Karam Festival (Jharkhand, Odisha, Chhattisgarh)"],
    "09-05": ["Eid-e-Milad / Milad-un-Nabi*"],
    "09-14": ["Ganesh Chaturthi"],
    "09-17": ["Rishi Panchami"],
    "09-18": ["Nuakhai (Odisha)"],
    "09-23": ["Anant Chaturdashi"],

    # October
    "10-02": ["Gandhi Jayanti"],
    "10-10": ["Bathukamma Begins (Telangana)"],
    "10-11": ["Sharad Navratri Begins"],
    "10-18": ["Saddula Bathukamma (Final Day, Telangana)"],
    "10-20": ["Dussehra / Vijayadashami"],
    "10-29": ["Karva Chauth"],

    # November
    "11-01": ["All Saints' Day"],
    "11-02": ["Day of the Dead"],
    "11-06": ["Dhanteras"],
    "11-08": ["Diwali"],
    "11-09": ["Govardhan Puja"],
    "11-10": ["Bhai Dooj"],
    "11-11": ["Veterans Day (USA)", "Singles' Day (China)"],
    "11-12": ["Chhath Puja"],
    "11-24": ["Guru Nanak Jayanti"],

    # December
    "12-06": ["Saint Nicholas Day"],
    "12-13": ["Saint Lucia Day (Sweden)"],
    "12-24": ["Christmas Eve"],
    "12-25": ["Christmas"],
    "12-26": ["Boxing Day"],
    "12-31": ["New Year's Eve"],
}

WORLD_FESTIVALS_FIXED = {
    "01-01": ["New Year's Day"],
    "02-14": ["Valentine's Day"],
    "03-17": ["St. Patrick's Day"],
    "03-21": ["Nowruz (Iran & Central Asia)"],
    "05-01": ["International Workers' Day"],
    "05-05": ["Cinco de Mayo (Mexico)"],
    "06-21": ["International Day of Yoga"],
    "06-24": ["Inti Raymi (Peru)"],
    "07-01": ["Canada Day"],
    "07-04": ["Independence Day (USA)"],
    "07-14": ["Bastille Day (France)"],
    "08-09": ["National Day (Singapore)"],
    "08-15": ["Independence Day (India)"],
    "08-31": ["Merdeka Day (Malaysia)"],
    "09-16": ["Malaysia Day"],
    "10-03": ["German Unity Day"],
    "10-31": ["Halloween"],
    "11-01": ["All Saints' Day"],
    "11-02": ["Day of the Dead"],
    "11-05": ["Guy Fawkes Night (UK)"],
    "11-11": ["Veterans Day (USA)"],
    "12-25": ["Christmas"],
    "12-26": ["Boxing Day"],
    "12-31": ["New Year's Eve"],
}

MOVABLE_FESTIVALS_NOTE = """
Movable / Variable Festivals (dates change each year):

- Ramadan, Eid al-Fitr, Eid al-Adha, Muharram, Mawlid (Islamic Lunar Calendar)
- Chinese New Year, Lantern Festival, Dragon Boat Festival, Mid-Autumn Festival
- Easter, Good Friday, Palm Sunday, Ascension Day, Pentecost
- Diwali, Holi, Maha Shivratri, Navratri, Dussehra, Ganesh Chaturthi, Janmashtami
- Vesak, Losar, Hanukkah, Yom Kippur, Rosh Hashanah, Passover

Only approximate months are fixed; exact Gregorian dates move each year.
"""

# ==============================
# GOOGLE PRODUCTS
# ==============================

GOOGLE_PRODUCTS = {
    "Main Google Apps": [
        ("Google Account", "https://myaccount.google.com"),
        ("Google Search", "https://www.google.com"),
        ("Gmail", "https://mail.google.com"),
        ("Google Maps", "https://maps.google.com"),
        ("YouTube", "https://www.youtube.com"),
        ("Google Play Store", "https://play.google.com"),
        ("Google News", "https://news.google.com"),
        ("Google Contacts", "https://contacts.google.com"),
        ("Google Drive", "https://drive.google.com"),
        ("Google Calendar", "https://calendar.google.com"),
        ("Google Translate", "https://translate.google.com"),
        ("Google Photos", "https://photos.google.com"),
        ("Google Meet", "https://meet.google.com"),
        ("Google Chat", "https://chat.google.com"),
        ("Google Shopping", "https://shopping.google.com"),
        ("Google Finance", "https://www.google.com/finance"),
        ("Google Docs", "https://docs.google.com/document"),
        ("Google Sheets", "https://docs.google.com/spreadsheets"),
        ("Google Slides", "https://docs.google.com/presentation"),
        ("Google Books", "https://books.google.com"),
        ("Google Keep", "https://keep.google.com"),
        ("Google Forms", "https://forms.google.com"),
        ("Google Sites", "https://sites.google.com"),
        ("Google Earth", "https://earth.google.com"),
        ("Google Flights", "https://flights.google.com"),
        ("Google Arts & Culture", "https://artsandculture.google.com"),
    ],
    "Workspace (India URLs)": [
        ("Gmail (Workspace)", "https://workspace.google.com/intl/en_in/products/gmail"),
        ("Drive (Workspace)", "https://workspace.google.com/intl/en_in/products/drive"),
        ("Meet (Workspace)", "https://workspace.google.com/intl/en_in/products/meet"),
        ("Calendar (Workspace)", "https://workspace.google.com/intl/en_in/products/calendar"),
        ("Chat (Workspace)", "https://workspace.google.com/intl/en_in/products/chat"),
        ("Gemini (Workspace AI)", "https://workspace.google.com/intl/en_in/solutions/ai/"),
        ("Docs (Workspace)", "https://workspace.google.com/intl/en_in/products/docs"),
        ("Sheets (Workspace)", "https://workspace.google.com/intl/en_in/products/sheets"),
        ("Slides (Workspace)", "https://workspace.google.com/intl/en_in/products/slides"),
        ("Vids (Workspace)", "https://workspace.google.com/intl/en_in/products/vids"),
        ("Keep (Workspace)", "https://workspace.google.com/intl/en_in/products/keep"),
        ("Sites (Workspace)", "https://workspace.google.com/intl/en_in/products/sites"),
        ("Forms (Workspace)", "https://workspace.google.com/intl/en_in/products/forms"),
        ("Tasks (Workspace)", "https://workspace.google.com/intl/en_in/products/tasks/"),
        ("NotebookLM (Workspace)", "https://workspace.google.com/intl/en_in/products/notebooklm"),
        ("AppSheet (Workspace)", "https://about.appsheet.com/home/"),
        ("Workspace Marketplace", "https://workspace.google.com/marketplace?pann=ogb"),
    ],
    "AI & Labs": [
        ("Google Gemini", "https://gemini.google.com"),
        ("Google AI Studio", "https://ai.google.dev/"),
        ("NotebookLM", "https://notebooklm.google"),
        ("Google Labs", "https://labs.google/"),
    ],
    "Hidden & Fun": [
        ("Google Fonts", "https://fonts.google.com"),
        ("Material Design", "https://m3.material.io"),
        ("Google Open Source", "https://opensource.google"),
        ("Google Search Console", "https://search.google.com/search-console"),
        ("Blogger", "https://www.blogger.com/features"),
        ("elgooG (Google Easter Eggs)", "https://elgoog.im/"),
    ],
    "Official Directories": [
        ("All Google Products Directory", "https://about.google/products/"),
        ("Developer Products Directory", "https://developers.google.com/products"),
    ],
}

def run_google_products_menu():
    print("==============================================")
    print("  Google Products")
    print("==============================================\n")
    print("Select a category, then choose a product to open in your browser.\n")

    categories = list(GOOGLE_PRODUCTS.keys())
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    print("0. Back to main menu\n")

    cat_choice = input("Choose a category number: ").strip()
    if cat_choice == "0":
        log_history("Back from Google Products menu")
        return
    try:
        idx = int(cat_choice) - 1
        if idx < 0 or idx >= len(categories):
            print("Invalid category.\n")
            return
    except ValueError:
        print("Invalid number.\n")
        return

    category_name = categories[idx]
    products = GOOGLE_PRODUCTS[category_name]
    log_history(f"Opened Google Products category: {category_name}")

    print(f"\nProducts in: {category_name}\n")
    for i, (name, url) in enumerate(products, 1):
        print(f"{i}. {name}")
    print("0. Back\n")

    prod_choice = input("Choose a product number: ").strip()
    if prod_choice == "0":
        log_history(f"Back from category: {category_name}")
        return
    try:
        pidx = int(prod_choice) - 1
        if pidx < 0 or pidx >= len(products):
            print("Invalid product.\n")
            return
    except ValueError:
        print("Invalid number.\n")
        return

    product_name, product_url = products[pidx]
    print(f"\nOpening {product_name} in your browser...\n")
    webbrowser.open(product_url)
    log_history(f"Opened Google product: {product_name} ({product_url})")
    input("Press Enter to return to the main menu...")

# ==============================
# DATE / TIME / FESTIVALS
# ==============================

def show_datetime_and_festival():
    print("==============================================")
    print("  Date / Time / Festivals (India + World)")
    print("==============================================\n")

    now = datetime.now()
    today = now.date()

    date_str = now.strftime("%d-%m-%Y")
    day_name = now.strftime("%A")
    month_name = now.strftime("%B")
    year = now.strftime("%Y")

    time_24 = now.strftime("%H:%M:%S")
    time_12 = now.strftime("%I:%M:%S %p")

    print(f"Today is: {day_name}, {date_str}")
    print(f"Month: {month_name}, Year: {year}")
    print(f"Time (24-hour): {time_24}")
    print(f"Time (12-hour): {time_12}\n")

    key = today.strftime("%m-%d")
    festivals = []

    if key in INDIA_FESTIVALS_2026:
        festivals.extend(INDIA_FESTIVALS_2026[key])
    if key in WORLD_FESTIVALS_FIXED:
        for f in WORLD_FESTIVALS_FIXED[key]:
            if f not in festivals:
                festivals.append(f)

    if festivals:
        print("Festivals on this date:")
        for f in festivals:
            print(" -", f)
        log_history(f"Checked festivals for {date_str}: {', '.join(festivals)}")
        print()
    else:
        print("No major festival from the 2026 India + world fixed list on this date.\n")
        log_history(f"Checked festivals for {date_str}: none in list")

    print(MOVABLE_FESTIVALS_NOTE)
    input("Press Enter to go back to the main menu...")

# ==============================
# PROMPT GENERATOR (with styles, clipboard, favorites, auto-Perchance)
# ==============================

def generate_prompt(short_idea: str, style: str = "default") -> str:
    base_common = (
        "high quality, ultra detailed, 4k, masterpiece, beautiful composition, "
        "sharp focus, crisp details, "
    )

    if style == "anime":
        style_txt = "anime style, vibrant colors, clean lines, sharp anime shading, "
    elif style == "photo":
        style_txt = "photorealistic, DSLR, shallow depth of field, natural lighting, "
    elif style == "pixel":
        style_txt = "pixel art, 16-bit game style, crisp pixels, limited color palette, "
    elif style == "cinematic":
        style_txt = "cinematic lighting, movie poster, dramatic shadows, high contrast, "
    else:
        style_txt = ""

    return base_common + style_txt + short_idea.strip()

def save_prompt(short_idea: str, prompt: str, style: str) -> None:
    is_new_file = not os.path.exists(PROMPT_HISTORY_FILE)
    with open(PROMPT_HISTORY_FILE, "a", encoding="utf-8") as f:
        if is_new_file:
            f.write("Prompt Generator History\n")
            f.write("========================\n\n")
        f.write(f"Time: {datetime.now().isoformat(timespec='seconds')}\n")
        f.write(f"Style: {style}\n")
        f.write(f"Short idea: {short_idea}\n")
        f.write(f"Generated prompt: {prompt}\n")
        f.write("-" * 40 + "\n\n")

def save_favorite(short_idea: str, prompt: str, style: str) -> None:
    is_new_file = not os.path.exists(FAVORITES_FILE)
    with open(FAVORITES_FILE, "a", encoding="utf-8") as f:
        if is_new_file:
            f.write("Favorite Prompts\n")
            f.write("================\n\n")
        f.write(f"Time: {datetime.now().isoformat(timespec='seconds')}\n")
        f.write(f"Style: {style}\n")
        f.write(f"Short idea: {short_idea}\n")
        f.write(f"Prompt: {prompt}\n")
        f.write("-" * 40 + "\n\n")
    log_history(f"Saved favorite prompt (style={style}, idea={short_idea})")

def view_favorites():
    print("==============================================")
    print("  Favorite Prompts")
    print("==============================================\n")

    if not os.path.exists(FAVORITES_FILE):
        print("No favorite prompts saved yet.\n")
        log_history("Viewed favorites: none yet")
        input("Press Enter to return to the main menu...")
        return

    with open(FAVORITES_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    print(content)
    log_history("Viewed favorites prompts file")
    input("Press Enter to return to the main menu...")

def run_prompt_helper():
    print("==============================================")
    print("  Prompt + Image Helper (Auto Perchance)")
    print("==============================================\n")
    print("Flow:")
    print("  1) Choose a style")
    print("  2) Enter a short idea")
    print("  3) AI 2 generates a long prompt")
    print("  4) Prompt is copied to clipboard (Windows)")
    print("  5) Perchance (Stable Diffusion) opens automatically\n")

    style_map = {
        "1": "default",
        "2": "photo",
        "3": "anime",
        "4": "pixel",
        "5": "cinematic",
    }

    while True:
        print("Choose style:")
        print("  1) Default")
        print("  2) Realistic Photo")
        print("  3) Anime")
        print("  4) Pixel Art")
        print("  5) Cinematic")
        print("  0) Back\n")

        style_choice = input("Style number: ").strip()
        if style_choice == "0":
            log_history("Exited Prompt + Image Helper")
            break

        style = style_map.get(style_choice, "default")

        idea = input("Enter a short idea (or 'back' to return): ").strip()
        if idea.lower() == "back":
            log_history("Exited Prompt + Image Helper")
            break
        if not idea:
            print("Please type something.\n")
            continue

        log_history(f"Prompt idea entered: {idea} (style={style})")
        prompt = generate_prompt(idea, style)
        print("\nGenerated prompt:\n")
        print(prompt)
        print()

        # Save to history file
        save_prompt(idea, prompt, style)
        log_history("Generated prompt and saved to prompt history file")
        print("Saved to history file.\n")

        # Copy to clipboard (Windows)
        copy_to_clipboard(prompt)
        print("Prompt copied to clipboard. Press Ctrl+V in Perchance.\n")

        # Ask to save as favorite
        fav_choice = input("Save this prompt as a favorite? (y/n): ").strip().lower()
        if fav_choice == "y":
            save_favorite(idea, prompt, style)
            print("Saved as favorite.\n")
        else:
            print("Not saved as favorite.\n")

        # Auto-open Perchance
        print("Opening Perchance (Stable Diffusion) in your browser...")
        webbrowser.open(PERCHANCE_URL)
        log_history("Opened Perchance automatically after generating prompt")
        print("Paste the prompt into the prompt/description box and click Generate.\n")

# ==============================
# MATH SOLVER
# ==============================

def safe_eval_math(expr: str) -> float:
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    code = compile(expr, "<string>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"Use of '{name}' is not allowed.")
    return eval(code, {"__builtins__": {}}, allowed_names)

def run_math_solver():
    print("==============================================")
    print("  Math Solver (Simple Calculator)")
    print("==============================================\n")
    print("Type a math expression, for example:")
    print("  2+3*4")
    print("  (5**2 + 3)/4")
    print("  sqrt(16) + sin(0.5)")
    print("Type 'back' to return to the main menu.\n")

    while True:
        expr = input("Enter math expression: ").strip()
        if expr.lower() == "back":
            log_history("Exited Math Solver")
            break
        if not expr:
            print("Please type something.\n")
            continue
        try:
            result = safe_eval_math(expr)
            print("Result:", result, "\n")
            log_history(f"Math expression: {expr} = {result}")
        except Exception as e:
            print("Error:", e, "\n")
            log_history(f"Math expression error: {expr} -> {e}")

# ==============================
# EXTRA MATH TOOLS
# ==============================

def quadratic_solver():
    print("==============================================")
    print("  Quadratic Equation Solver")
    print("  Solve: ax^2 + bx + c = 0")
    print("==============================================\n")

    a = input("Enter a: ").strip()
    b = input("Enter b: ").strip()
    c = input("Enter c: ").strip()

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print("Invalid numbers.\n")
        log_history("Quadratic solver: invalid input")
        return

    if a == 0:
        print("'a' cannot be 0 for a quadratic equation.\n")
        log_history("Quadratic solver: a=0 invalid")
        return

    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print("Two real roots:")
        print("  x1 =", x1)
        print("  x2 =", x2)
        log_history(f"Quadratic roots (two real): a={a}, b={b}, c={c}, x1={x1}, x2={x2}")
    elif D == 0:
        x = -b / (2*a)
        print("One real root:")
        print("  x =", x)
        log_history(f"Quadratic root (one real): a={a}, b={b}, c={c}, x={x}")
    else:
        real = -b / (2*a)
        imag = abs(D**0.5) / (2*a)
        print("Two complex roots:")
        print(f"  x1 = {real} + {imag}i")
        print(f"  x2 = {real} - {imag}i")
        log_history(f"Quadratic roots (complex): a={a}, b={b}, c={c}, x1={real}+{imag}i, x2={real}-{imag}i")
    print()

def area_perimeter():
    print("==============================================")
    print("  Area & Perimeter Helper")
    print("==============================================\n")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle (base, height, sides)")
    print("0. Back\n")

    choice = input("Choose shape number: ").strip()
    if choice == "0":
        log_history("Exited Area & Perimeter Helper")
        return

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid number.\n")
        log_history("Area & Perimeter: invalid menu choice")
        return

    if choice == 1:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        area = l * b
        peri = 2 * (l + b)
        print("Rectangle:")
        print("  Area =", area)
        print("  Perimeter =", peri)
        log_history(f"Rectangle area/perimeter: length={l}, breadth={b}, area={area}, peri={peri}")
    elif choice == 2:
        r = float(input("Enter radius: "))
        area = math.pi * r**2
        circ = 2 * math.pi * r
        print("Circle:")
        print("  Area =", area)
        print("  Circumference =", circ)
        log_history(f"Circle area/circ: radius={r}, area={area}, circ={circ}")
    elif choice == 3:
        base = float(input("Enter base: "))
        h = float(input("Enter height: "))
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        area = 0.5 * base * h
        peri = a + b + base
        print("Triangle:")
        print("  Area =", area)
        print("  Perimeter =", peri)
        log_history(f"Triangle area/peri: base={base}, height={h}, a={a}, b={b}, area={area}, peri={peri}")
    else:
        print("Invalid choice.\n")
        log_history("Area & Perimeter: invalid shape choice")
    print()

def run_extra_math_tools():
    print("==============================================")
    print("  Extra Math Tools")
    print("==============================================\n")
    print("1. Quadratic Equation Solver")
    print("2. Area & Perimeter Helper")
    print("0. Back to main menu\n")

    choice = input("Choose number: ").strip()
    if choice == "0":
        log_history("Back from Extra Math Tools")
        return
    if choice == "1":
        log_history("Opened Quadratic Equation Solver")
        quadratic_solver()
    elif choice == "2":
        log_history("Opened Area & Perimeter Helper")
        area_perimeter()
    else:
        print("Invalid choice.\n")
        log_history("Extra Math Tools: invalid menu choice")

# ==============================
# MATH & PHYSICS FORMULAS
# ==============================

def show_basic_formulas():
    print("==============================================")
    print("  Math Formula Sheet (Basic to Class 12)")
    print("==============================================\n")

    print("1) Arithmetic:")
    print("   - Addition: a + b")
    print("   - Subtraction: a - b")
    print("   - Multiplication: a × b")
    print("   - Division: a ÷ b")
    print("   - Percentage: (part / whole) × 100\n")

    print("2) Algebra:")
    print("   - (a + b)^2 = a^2 + 2ab + b^2")
    print("   - (a - b)^2 = a^2 - 2ab + b^2")
    print("   - a^2 - b^2 = (a - b)(a + b)")
    print("   - Quadratic: ax^2 + bx + c = 0 →")
    print("     x = [-b ± √(b^2 - 4ac)] / (2a)\n")

    print("3) Geometry:")
    print("   - Perimeter of rectangle = 2 × (length + breadth)")
    print("   - Area of rectangle = length × breadth")
    print("   - Area of triangle = (1/2) × base × height")
    print("   - Circumference of circle = 2πr")
    print("   - Area of circle = πr^2\n")

    print("4) Trigonometry:")
    print("   - sin(θ) = opposite / hypotenuse")
    print("   - cos(θ) = adjacent / hypotenuse")
    print("   - tan(θ) = opposite / adjacent")
    print("   - a^2 + b^2 = c^2 (Pythagoras)\n")

    print("5) Coordinate Geometry:")
    print("   - Distance: d = √[(x2 - x1)^2 + (y2 - y1)^2]")
    print("   - Midpoint: M = ((x1 + x2)/2, (x1 + y2)/2)")
    print("   - Slope: m = (y2 - y1) / (x2 - x1)\n")

    print("6) Calculus (basic):")
    print("   Derivatives:")
    print("     - d/dx (x^n) = n x^(n - 1)")
    print("     - d/dx (sin x) = cos x")
    print("     - d/dx (cos x) = -sin x")
    print("     - d/dx (e^x) = e^x")
    print("   Integrals:")
    print("     - ∫ x^n dx = x^(n + 1) / (n + 1) + C")
    print("     - ∫ 1/x dx = ln|x| + C")
    print("     - ∫ e^x dx = e^x + C\n")

    log_history("Viewed Math Formula Sheet")
    input("Press Enter to go back...")

def show_physics_formulas():
    print("==============================================")
    print("  Basic Physics Formulas")
    print("==============================================\n")

    print("1) Motion:")
    print("   - Speed = distance / time")
    print("   - v = u + at")
    print("   - s = ut + (1/2)at^2")
    print("   - v^2 = u^2 + 2as\n")

    print("2) Force & Energy:")
    print("   - Force = mass × acceleration (F = ma)")
    print("   - Work = force × distance")
    print("   - Kinetic Energy = (1/2)mv^2")
    print("   - Potential Energy = mgh\n")

    print("3) Electricity:")
    print("   - V = I × R (Ohm's law)")
    print("   - Power = V × I")
    print("   - Power = I^2 × R\n")

    log_history("Viewed Physics Formula Sheet")
    input("Press Enter to go back...")

# ==============================
# WIKIPEDIA
# ==============================

def run_wikipedia_home():
    print("==============================================")
    print("  Wikipedia Home")
    print("==============================================\n")
    print("Opening Wikipedia home page...\n")
    webbrowser.open(WIKIPEDIA_URL)
    log_history("Opened Wikipedia Home")
    input("Press Enter to return...")

def run_wikipedia_search():
    print("==============================================")
    print("  Wikipedia Search")
    print("==============================================\n")
    print("Type a topic (e.g., Python, India, Black hole).")
    print("I will open the Wikipedia page.\n")
    print("'back' to return.\n")

    while True:
        topic = input("Enter topic: ").strip()
        if topic.lower() == "back":
            log_history("Exited Wikipedia Search")
            break
        if not topic:
            print("Please type something.\n")
            continue
        slug = topic.replace(" ", "_")
        slug = urllib.parse.quote(slug)
        url = WIKIPEDIA_SEARCH_BASE + slug
        print("Opening:", url)
        webbrowser.open(url)
        log_history(f"Wikipedia search/open: {topic} -> {url}")
        print()

# ==============================
# COMMUNITY / AURA LAB LINKS
# ==============================

AURA_LINKS = [
    ("Aura Lab: Cares & Laughs 2 (CodePen)", "https://codepen.io/Kavyant-Kumar/pen/dPOXwmY"),
    ("Aura Lab: Cares & Laughs 1 (CodePen)", "https://codepen.io/Kavyant-Kumar/pen/dPGJPKj"),
    ("Instagram @kavyanthub", "https://www.instagram.com/kavyanthub/"),
    ("Facebook Profile", "https://www.facebook.com/profile.php?id=61586003535719"),
    ("GitHub @Kiik913", "https://github.com/Kiik913"),
    ("Aura Lab Discord Server", "https://discord.com/channels/1505857480503197696/1505857672597999736"),
    ("Care Lab Studio YouTube Channel", "https://www.youtube.com/@CareLabStudio"),
    ("Sekai app (search in your app store)", None),
]

def run_aura_links():
    print("==============================================")
    print("  Aura Lab / Social Links")
    print("==============================================\n")
    print("Select a link to open in your browser.\n")

    for i, (name, url) in enumerate(AURA_LINKS, 1):
        if url:
            print(f"{i}. {name}  ->  {url}")
        else:
            print(f"{i}. {name}  (no direct URL, open manually in app store)")
    print("0. Back\n")

    choice = input("Choose number: ").strip()
    if choice == "0":
        log_history("Back from Aura Lab / Social Links")
        return

    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(AURA_LINKS):
            print("Invalid choice.\n")
            return
    except ValueError:
        print("Invalid number.\n")
        return

    name, url = AURA_LINKS[idx]
    if url:
        print(f"\nOpening {name}...\n")
        webbrowser.open(url)
        log_history(f"Opened Aura/Social link: {name} ({url})")
    else:
        print("\nThis entry does not have a direct link (Sekai app).")
        print("Open your app store and search for 'Sekai' to install / open it.\n")
        log_history("Viewed Sekai app info (no direct URL)")
    input("Press Enter to return to the main menu...")

# ==============================
# HELP / TUTORIAL
# ==============================

def show_help():
    print("==============================================")
    print("  Help – How to use AI 2")
    print("==============================================\n")

    print("1) Prompt + Image Helper (auto Perchance)")
    print("   - From main menu, choose option 1.")
    print("   - Choose a style: Default, Photo, Anime, Pixel, Cinematic.")
    print("   - Type a short idea (example: 'cute anime cat in neon city').")
    print("   - AI 2 generates a long, detailed prompt for Stable Diffusion.")
    print("   - The prompt is automatically copied to your clipboard (Windows).")
    print("   - Perchance (Stable Diffusion, free, no login) opens in your browser.")
    print("   - Press Ctrl+V in the Perchance prompt box and click Generate.\n")

    print("2) Favorite Prompts")
    print("   - After a prompt is generated, you can choose to save it as a favorite.")
    print("   - All favorites are stored in the file:")
    print("       favorites_prompts.txt")
    print("   - From main menu, option 2: 'View Favorite Prompts' shows all saved prompts.\n")

    print("3) History & Logs")
    print("   - Every action (menu choices, prompts, math, links) is logged to:")
    print("       C:\\Users\\HP\\AI 2 History\\AI 2 history.txt")
    print("   - Prompt history (every generated prompt) is stored in:")
    print("       prompts_history.txt")
    print("   - You can open these files in Notepad to review everything AI 2 did.\n")

    print("4) Festivals & Date/Time")
    print("   - Main menu option 7: 'Date / Time / Festivals (India + World)'.")
    print("   - Shows today’s date, time, and any fixed-date festivals for 2026.")
    print("   - Includes separate lists for India festivals and world fixed-date days.")
    print("   - Also shows a note explaining movable festivals (like Diwali, Eid, etc.).\n")

    print("5) Study Tools (Math & Physics)")
    print("   - Math Solver (option 3): quick calculator with safe math expressions.")
    print("   - Extra Math Tools (option 4): quadratic solver and area/perimeter helper.")
    print("   - Math Formulas (option 5): basic to Class 12 style formulas.")
    print("   - Physics Formulas (option 6): school-level motion, energy, electricity.\n")

    print("6) Quick Web Shortcuts")
    print("   - Wikipedia Home & Search (options 8 and 9) open Wikipedia in your browser.")
    print("   - Google Products (option 10) opens many Google / Workspace apps.")
    print("   - Aura Lab / Social Links (option 11) open your CodePen, Instagram, GitHub, etc.\n")

    print("7) Aura Lab Hub")
    print("   - AI 2 is your offline hub for:")
    print("       * Image prompts for Perchance / Stable Diffusion")
    print("       * Study help (math, physics, formulas)")
    print("       * Quick launchers for Google, Wiki, and your Aura Lab links")
    print("       * History of what you did, saved on your own PC")
    print("   - Think of it as the command center for Aura Lab / Care Lab Studio.\n")

    input("Press Enter to return to the main menu...")
    log_history("Viewed Help / Tutorial")

# ==============================
# CREDITS
# ==============================

def show_credits():
    print("==============================================")
    print("  Credits")
    print("==============================================\n")
    print("AI 2: Prompts + Math + Google + Wiki + Festivals + History")
    print("Created by: Kavyant (Aura Lab / Care Lab Studio)")
    print("Assistant / ideas: Perplexity AI\n")
    print("Main Features:")
    print(" - Prompt generator for AI images (Perchance, Stable Diffusion Web)")
    print(" - Prompt styles (default, photo, anime, pixel, cinematic)")
    print(" - Auto-copy prompt to clipboard (Windows) + auto-open Perchance")
    print(" - Favorite prompts list and viewer")
    print(" - Math tools and formulas (basic to class 12 style)")
    print(" - Physics formulas (school level)")
    print(" - Quick launchers for Google & Workspace apps")
    print(" - Date/Time with India + world festivals list")
    print(" - Full history logging to 'C:\\Users\\HP\\AI 2 History\\AI 2 history.txt'")
    print(" - Local folder for saving screenshots from any device:\n")
    print("     C:\\Users\\HP\\AI 2 History\n")
    print("Aura Lab / Care Lab Studio Links:")
    print(" - Cares & Laughs 2 (CodePen): https://codepen.io/Kavyant-Kumar/pen/dPOXwmY")
    print(" - Cares & Laughs 1 (CodePen): https://codepen.io/Kavyant-Kumar/pen/dPGJPKj")
    print(" - Instagram: https://www.instagram.com/kavyanthub/")
    print(" - Facebook:  https://www.facebook.com/profile.php?id=61586003535719")
    print(" - GitHub:    https://github.com/Kiik913")
    print(" - Aura Lab Discord server (channel link)")
    print(" - YouTube:   https://www.youtube.com/@CareLabStudio")
    print(" - Many cool projects and ideas also live in the Sekai app.\n")
    print("Use the 'Aura Lab / Social Links' menu to open these directly.\n")
    log_history("Viewed Credits")
    input("Press Enter to return to the main menu...")

# ==============================
# MAIN MENU
# ==============================

def main():
    log_history("=== AI 2 app started ===")
    while True:
        print("==============================================")
        print("  AI 2: Prompts + Math + Google + Wiki + Festivals")
        print("==============================================")
        print("1. Prompt + Image Helper (auto Perchance)")
        print("2. View Favorite Prompts")
        print("3. Math Solver (Calculator)")
        print("4. Extra Math Tools")
        print("5. Math Formulas")
        print("6. Physics Formulas")
        print("7. Date / Time / Festivals (India + World)")
        print("8. Wikipedia Home")
        print("9. Wikipedia Search")
        print("10. Google Products")
        print("11. Aura Lab / Social Links")
        print("12. Help – How to use AI 2")
        print("13. Credits")
        print("14. Exit")
        choice = input("Choose 1-14: ").strip()
        log_history(f"Main menu choice: {choice}")

        if choice == "1":
            run_prompt_helper()
        elif choice == "2":
            view_favorites()
        elif choice == "3":
            run_math_solver()
        elif choice == "4":
            run_extra_math_tools()
        elif choice == "5":
            show_basic_formulas()
        elif choice == "6":
            show_physics_formulas()
        elif choice == "7":
            show_datetime_and_festival()
        elif choice == "8":
            run_wikipedia_home()
        elif choice == "9":
            run_wikipedia_search()
        elif choice == "10":
            run_google_products_menu()
        elif choice == "11":
            run_aura_links()
        elif choice == "12":
            show_help()
        elif choice == "13":
            show_credits()
        elif choice == "14":
            print("Goodbye!")
            log_history("=== AI 2 app exited by user ===")
            break
        else:
            print("Invalid choice. Enter 1-14.\n")
            log_history(f"Invalid main menu choice: {choice}")

if __name__ == "__main__":
    main()
