from openvpn3.constants import StatusMajor, StatusMinor

with open("enums.h", "a+") as f:
    f.write("\n")
    for (k,v) in StatusMajor.__members__.items():
        print(f"#define MAJOR_{k} {v.value}")
        f.write(f"#define MAJOR_{k} {v.value}\n")

    for (k,v) in StatusMinor.__members__.items():
        print(f"#define MINOR_{k} {v.value}")
        f.write(f"#define MINOR_{k} {v.value}\n")