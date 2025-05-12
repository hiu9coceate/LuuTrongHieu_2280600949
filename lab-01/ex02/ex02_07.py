lines = []
while True:
    line = input("Nhap cac dong van ban (Nhap 'done' de ket thuc): ")
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nCac dong van ban da nhap sau khi chuyen thanh chu hoa:")
for line in lines:
    print(line.upper())