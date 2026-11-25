import matplotlib.pyplot as plt
from simulate import run
t, y, m, delta, cmd = run(2.0, 1.5, 1.0, with_gust=True)
plt.figure(figsize=(8, 4))
plt.plot(t, y, label="Angle vrai (PID)")
plt.axhline(5, ls="--", color="k", label="Consigne 5°")
plt.axvspan(5, 7, color="orange", alpha=0.2, label="Rafale")
plt.xlabel("Temps (s)"); plt.ylabel("Angle (deg)")
plt.title("Boucle fermée : échelon 5° + rafale"); plt.grid(True); plt.legend()
plt.tight_layout(); plt.savefig("../docs/step_gust_closed_loop.png")