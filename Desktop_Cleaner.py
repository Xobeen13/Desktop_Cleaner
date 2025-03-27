from pathlib import Path

def get_unique_path(path):
    counter = 1
    new_path = path
    while new_path.exists():
        new_path = path.with_name(f"{path.stem}_{counter}")
        counter += 1
    return new_path

#Desktop adress
desktop = Path.home() / "Desktop"

#Folders for Organization and checking for fodler existing
for category in ["University", "CoopResume", "Weeb", "Val", "Projects", "Misc", "Chinese", "Misc"]:
    (desktop / category).mkdir(exist_ok=True)


categories = {
    "University": ["mte", "lecture", "assignment", "notes", "course", "homework", "study", "lab", "syllabus", "slides", "uw", "bio","pd", "241"],
    "CoopResume": ["resume", "cv", "cover", "job", "application", "interview", "position", "company", "portfolio", "linkedin"],
    "Weeb": ["anime", "manga", "naruto", "onepiece", "aot", "bleach", "episode", "scan", "volume", "chapter"],
    "Val": ["valorant", "val", "clip", "gameplay", "frag", "highlight", "ranked", "headshot", "ace", "clutch"],
    "Projects": ["project", "robot", "arduino", "code", "design", "prototype", "firmware", "build", "system", "electronics", "python","programming"],
    "Chinese":["chinese",],
    "Screenshots":["screenshot", ]
}

excluded_folders = {"University", "CoopResume", "Weeb", "Val", "Projects", "Screenshots", "Chinese", "Misc"}

for item in desktop.iterdir():
    if item.is_dir() and item.name in excluded_folders:
        continue

    if item.is_file() or item.is_dir():
        name = item.name.lower()
        matched = False


        for category, keywords in categories.items():
            if any(keyword in name for keyword in keywords):
                target_folder = desktop / category
                target_folder.mkdir(exist_ok=True)
                target_path = target_folder / item.name

                if item.resolve() == target_path.resolve():
                    matched =True
                    break

                safe_path = get_unique_path(target_path)
                item.rename(safe_path)
                print(f"Moved {item.name} → {safe_path.parent.name}")
                break
        if not matched:    
            item.rename(desktop / "Misc" / item.name)



