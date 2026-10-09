
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Nom": ["Amira", "Sami", "Nour", "Youssef", "Mariem"],
    "Python": [16, 12, 18, 9, 14],
    "SQL": [15, 14, 17, 10, 16],
    "BI": [17, 11, 19, 8, 15]
}

df = pd.DataFrame(data)

df["Moyenne"] = df[["Python", "SQL", "BI"]].mean(axis=1).round(2)
df["Resultat"] = df["Moyenne"].apply(
    lambda x: "Admis" if x >= 10 else "Non admis"
)

print("RESULTATS DES ETUDIANTS")
print(df)

print("\nMoyenne generale :", round(df["Moyenne"].mean(), 2))
print("Meilleur etudiant :", df.loc[df["Moyenne"].idxmax(), "Nom"])
print("Nombre d'admis :", (df["Resultat"] == "Admis").sum())

df.plot(x="Nom", y="Moyenne", kind="bar", legend=False)
plt.axhline(y=10, linestyle="--")
plt.title("Moyenne par etudiant")
plt.ylabel("Moyenne")
plt.xlabel("Etudiant")
plt.ylim(0, 20)
plt.tight_layout()
plt.show()
