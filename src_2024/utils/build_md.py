import os
from api import get_name, YEAR

base_link = "https://github.com/Fate6174/advent-of-code-2024/blob/main/src/"


def parse(e):
    name = get_name(int(e.replace(".py", "")))
    # name = " ".join(name.split("_")[1:])
    return f"[{name}]({base_link}{e})"


solutions = filter(lambda x: ".py" in x and "init" not in x, os.listdir("src"))

readme_content = f"# Advent of code {YEAR}\n\nProblems list:\n\n"
tmp = [f"- {parse(e)}" for i, e in enumerate(sorted(solutions))]
readme_content += "\n".join(tmp)

with open("README.md", "w") as f:
    f.write(
        readme_content
        + "\n\nCreated via: [advent-of-code-setup](https://github.com/tomfran/advent-of-code-setup)"
    )
