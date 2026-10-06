import csv
import re

import requests
from bs4 import BeautifulSoup, NavigableString


URL = "https://en.wikipedia.org/wiki/2026_in_technology_and_computing"
OUTPUT_FILE = "technology_events_2026.csv"

MONTHS = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]


def clean_text(text):
    # Remove Wikipedia citation numbers such as [1], [2], etc.
    text = re.sub(r"\[\d+\]", "", text)

    # Remove unnecessary spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def get_parent_text(li):
    """
    Gets the text of a list item before a nested list begins.

    Example:

    January 7 –
        • Event A
        • Event B

    Returns:
    January 7 –
    """

    parts = []

    for child in li.children:

        # Stop when we reach a nested list
        if getattr(child, "name", None) in ["ul", "ol"]:
            break

        if isinstance(child, NavigableString):
            parts.append(str(child))

        else:
            parts.append(child.get_text(" ", strip=True))

    return clean_text(" ".join(parts))


def scrape_events():

    headers = {
        "User-Agent": "Student-NER-Web-Scraping-Project/1.0"
    }

    print("Connecting to Wikipedia...")

    response = requests.get(
        URL,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    print("Page downloaded successfully.")

    soup = BeautifulSoup(response.text, "html.parser")

    records = []

    # Go through each month
    for month in MONTHS:

        heading = soup.find("h2", id=month)

        if heading is None:
            continue

        print(f"Collecting {month}...")

        # Look at everything after this heading
        # until the next H2 heading appears
        for element in heading.find_all_next(["h2", "li"]):

            # Reached the next section
            if element.name == "h2":
                break

            li = element

            # Ignore nested list items here.
            # They are handled through their parent.
            if li.find_parent("li") is not None:
                continue

            nested_list = li.find(
                ["ul", "ol"],
                recursive=False
            )

            # Example:
            #
            # January 7 –
            #     Event A
            #     Event B
            #
            if nested_list:

                parent_text = get_parent_text(li)

                # Get date before the dash
                if "–" in parent_text:
                    date = parent_text.split("–", 1)[0].strip()
                elif "-" in parent_text:
                    date = parent_text.split("-", 1)[0].strip()
                else:
                    date = parent_text

                for child_li in nested_list.find_all(
                    "li",
                    recursive=False
                ):

                    child_text = clean_text(
                        child_li.get_text(
                            " ",
                            strip=True
                        )
                    )

                    if child_text:

                        event_text = (
                            f"{date} – {child_text}"
                        )

                        records.append({
                            "Month": month,
                            "Event Text": event_text
                        })

            # Normal event with no nested list
            else:

                event_text = clean_text(
                    li.get_text(
                        " ",
                        strip=True
                    )
                )

                if event_text:

                    records.append({
                        "Month": month,
                        "Event Text": event_text
                    })

    return records


def remove_duplicates(records):

    cleaned_records = []
    seen = set()

    for record in records:

        key = (
            record["Month"],
            record["Event Text"]
        )

        if key not in seen:

            seen.add(key)
            cleaned_records.append(record)

    return cleaned_records


def save_csv(records):

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Month",
            "Event Text"
        ])

        for index, record in enumerate(
            records,
            start=1
        ):

            writer.writerow([
                index,
                record["Month"],
                record["Event Text"]
            ])


def main():

    events = scrape_events()

    events = remove_duplicates(events)

    save_csv(events)

    print()
    print("Web scraping complete.")
    print(f"Total events collected: {len(events)}")
    print(f"Dataset saved as: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()