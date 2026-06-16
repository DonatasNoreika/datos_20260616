import pendulum
import sqlalchemy
metai = int(input("Metai: "))
menuo = int(input("Mėnuo: "))
diena = int(input("Diena: "))
data = pendulum.date(metai, menuo, diena)
delta = data.diff(pendulum.today())
print(f"Nuo {data} praėjo {delta.in_days()} dienų")
