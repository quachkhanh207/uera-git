import json
import os

# ====== TAI DANH BA ======
def tai_danh_ba():
    if os.path.exists("danhba.json"):
        with open("danhba.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# ====== LUU DANH BA ======
def luu_danh_ba(danh_ba):
    with open("danhba.json", "w", encoding="utf-8") as f:
        json.dump(danh_ba, f, ensure_ascii=False, indent=4)
    print("Da luu danh ba vao file danhba.json")


# ====== HIEN THI ======
def hien_thi_danh_ba(danh_ba):
    if not danh_ba:
        print("Danh ba rong.")
        return

    print("\n===== DANH BA =====")
    for i, nguoi in enumerate(danh_ba, start=1):
        print(f"{i}. Ten: {nguoi['ten']} | SDT: {nguoi['sdt']}")


# ====== THEM LIEN LAC ======
def them_lien_lac(danh_ba):
    ten = input("Nhap ten: ").strip()
    sdt = input("Nhap so dien thoai: ").strip()

    if not ten or not sdt:
        print("Thong tin khong hop le.")
        return

    danh_ba.append({"ten": ten, "sdt": sdt})
    print("Da them lien lac moi.")


# ====== MENU ======
def menu():
    print("\n===== QUAN LY DANH BA =====")
    print("1. Hien thi danh ba")
    print("2. Them lien lac moi")
    print("3. Luu danh ba")
    print("4. Thoat")


# ====== CHUONG TRINH CHINH ======
def main():
    danh_ba = tai_danh_ba()  # tu dong tai khi khoi dong

    while True:
        menu()
        lua_chon = input("Chon chuc nang: ")

        if lua_chon == "1":
            hien_thi_danh_ba(danh_ba)

        elif lua_chon == "2":
            them_lien_lac(danh_ba)

        elif lua_chon == "3":
            luu_danh_ba(danh_ba)

        elif lua_chon == "4":
            print("Thoat chuong trinh.")
            break

        else:
            print("Lua chon khong hop le.")


if __name__ == "__main__":
    main()
