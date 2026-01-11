import json
import os

notebook_path = r'C:\Users\guard\Desktop\Programacion\Real-State-Capital-Federal-Argentina\notebooks\analisis.ipynb'

new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 4.4 Validación Cruzada del Modelo Final\n",
            "Realizaremos una validación cruzada con 10 folds para evaluar la robustez del modelo seleccionado (usaremos el mejor de Ridge)."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "from sklearn.model_selection import cross_val_score\n",
            "import numpy as np\n",
            "\n",
            "# Usamos el mejor estimador de Ridge encontrado anteriormente\n",
            "best_model = ridge_cv.best_estimator_\n",
            "\n",
            "# Cross-Validation para R2\n",
            "cv_scores = cross_val_score(best_model, X, y, cv=10, scoring='r2')\n",
            "\n",
            "print(\"Resultados de Validación Cruzada (R2):\")\n",
            "print(cv_scores)\n",
            "print(f\"R2 Promedio: {np.mean(cv_scores):.4f} (+/- {np.std(cv_scores):.4f})\")\n",
            "\n",
            "# Cross-Validation para MAE (negativo en sklearn)\n",
            "cv_mae = cross_val_score(best_model, X, y, cv=10, scoring='neg_mean_absolute_error')\n",
            "print(f\"MAE Promedio: {-np.mean(cv_mae):.4f}\")"
        ]
    }
]

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

nb['cells'].extend(new_cells)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=4)

print("Notebook updated with Validation code.")
