import json
import os

notebook_path = r'C:\Users\guard\Desktop\Programacion\Real-State-Capital-Federal-Argentina\notebooks\analisis.ipynb'

new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 4.2 Selección de Características (RFE)\n",
            "Utilizaremos Recursive Feature Elimination (RFE) para identificar las 15 variables más importantes y simplificar el modelo."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "from sklearn.feature_selection import RFE\n",
            "from sklearn.linear_model import LinearRegression\n",
            "\n",
            "# Inicializar el estimador para RFE\n",
            "estimator = LinearRegression()\n",
            "# Seleccionar las 15 mejores características\n",
            "selector = RFE(estimator, n_features_to_select=15, step=1)\n",
            "selector = selector.fit(X, y)\n",
            "\n",
            "selected_features = X.columns[selector.support_]\n",
            "print(\"Top 15 Características seleccionadas por RFE:\")\n",
            "print(selected_features)\n",
            "\n",
            "# Entrenar modelo OLS con características seleccionadas\n",
            "X_rfe =X[selected_features]\n",
            "X_rfe = sm.add_constant(X_rfe)\n",
            "model_rfe = sm.OLS(y, X_rfe).fit()\n",
            "print(model_rfe.summary())"
        ]
    }
]

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

nb['cells'].extend(new_cells)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=4)

print("Notebook updated with Feature Selection code.")
