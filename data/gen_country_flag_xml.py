import os

for flag in os.listdir("country_flags/svg/"):
    print(f'<file>{os.path.join("country_flags", "svg", flag)}</file>')
