import json
import os

notebook_path = r'C:\Users\guard\Desktop\Programacion\Real-State-Capital-Federal-Argentina\notebooks\analisis.ipynb'

new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 4. Verificación y Mejora del Modelo de Regresión Lineal\n",
            "Nos enfocaremos en validar los supuestos de la regresión lineal para asegurar que las conclusiones sean válidas."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import matplotlib.pyplot as plt\n",
            "import scipy.stats as stats\n",
            "import seaborn as sns \n",
            "\n",
            "# Recalcular residuos y valores ajustados del modelo OLS (modelo_log_con_dummies)\n",
            "model = modelo_log_con_dummies\n",
            "residuals = model.resid\n",
            "fitted_values = model.fittedvalues\n",
            "\n",
            "# 1. Residuals vs Fitted (Homocedasticidad y Linealidad)\n",
            "plt.figure(figsize=(10, 6))\n",
            "plt.scatter(fitted_values, residuals, alpha=0.5)\n",
            "plt.axhline(y=0, color='r', linestyle='--')\n",
            "plt.xlabel('Valores Ajustados (Fitted Values)')\n",
            "plt.ylabel('Residuos')\n",
            "plt.title('Residuos vs Valores Ajustados')\n",
            "plt.show()\n",
            "\n",
            "# 2. Verificación de Normalidad (Q-Q Plot e Histograma)\n",
            "fig, ax = plt.subplots(1, 2, figsize=(16, 6))\n",
            "\n",
            "stats.probplot(residuals, dist=\"norm\", plot=ax[0])\n",
            "ax[0].get_lines()[0].set_marker('o')\n",
            "ax[0].get_lines()[0].set_markersize(2.0)\n",
            "ax[0].set_title('Q-Q Plot')\n",
            "\n",
            "sns.histplot(residuals, kde=True, ax=ax[1])\n",
            "ax[1].set_title('Distribución de los Residuos')\n",
            "\n",
            "plt.show()"
        ]
    }
]

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

nb['cells'].extend(new_cells)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=4)

print("Notebook updated successfully.")
