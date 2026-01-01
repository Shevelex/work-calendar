from datetime import datetime, timedelta

def generate_calendar(path: str):
    events = [
        (
            datetime(2026, 1, 10, 8, 20),
            datetime(2026, 1, 10, 15, 10),
            "ШЕРЕМЕТ-B / КАЗАНЬ / ШЕРЕМЕТ-B [пас]"
        )
    ]

    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Work Calendar//RU",
        "CALSCALE:GREGORIAN",
        "X-WR-CALNAME:Работа",
    ]

    for i, (start, end, title) in enumerate(events):
        start_utc = (start - timedelta(hours=3)).strftime("%Y%m%dT%H%M%SZ")
        end_utc = (end - timedelta(hours=3)).strftime("%Y%m%dT%H%M%SZ")

        lines += [
            "BEGIN:VEVENT",
            f"UID:work-{i}@calendar",
            f"DTSTAMP:{start_utc}",
            f"DTSTART:{start_utc}",
            f"DTEND:{end_utc}",
            f"SUMMARY:{title}",
            "END:VEVENT",
        ]

    lines.append("END:VCALENDAR")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
