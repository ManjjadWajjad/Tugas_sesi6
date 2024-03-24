print("===Skor grade Nilai===")
nilai = int(input("Input nilai akhir: "))

if nilai >= 100:
    grade = "A"
    predicate = "with compliments"
elif nilai >= 89:
    grade = "B"
    predicate = "very satisfactory"
elif nilai >= 79:
    grade = "C"
    predicate = "satisfying"
elif nilai >= 69:
    grade = "D"
    predicate = "not satisfactory"
elif nilai >= 59:
    grade = "E"
    predicate = "not pass"

print("Grade:", grade)
print("Predicate:", predicate)