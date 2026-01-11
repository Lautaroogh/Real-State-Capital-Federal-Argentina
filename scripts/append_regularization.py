import json
import os

notebook_path = r'C:\Users\guard\Desktop\Programacion\Real-State-Capital-Federal-Argentina\notebooks\analisis.ipynb'

new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 4.3 Regularización (Ridge & Lasso)\n",
            "Implementaremos regresión Ridge y Lasso para manejar la multicolinealidad y evitar el sobreajuste."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "from sklearn.linear_model import Ridge, Lasso\n",
            "from sklearn.model_selection import GridSearchCV\n",
            "\n",
            "# Ridge Regression\n",
            "ridge = Ridge()\n",
            "ridge_params = {'alpha': [0.01, 0.1, 1, 10, 100]}\n",
            "ridge_cv = GridSearchCV(ridge, ridge_params, cv=5, scoring='r2')\n",
            "ridge_cv.fit(X, y)\n",
            "\n",
            "print(\"Mejor alpha para Ridge:\", ridge_cv.best_params_)\n",
            "print(\"Mejor R2 para Ridge:\", ridge_cv.best_score_)\n",
            "\n",
            "# Lasso Regression\n",
            "lasso = Lasso()\n",
            "# Usamos alphas pequeños porque Lasso puede llevar coeficientes a cero\n",
            "lasso_params = {'alpha': [0.0001, 0.001, 0.01, 0.1, 1]}\n",
            "lasso_cv = GridSearchCV(lasso, lasso_params, cv=5, scoring='r2')\n",
            "lasso_cv.fit(X, y)\n",
            "\n",
            "print(\"Mejor alpha para Lasso:\", lasso_cv.best_params_)\n",
            "print(\"Mejor R2 para Lasso:\", lasso_cv.best_score_)\n"
        ]
    }
]

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

nb['cells'].extend(new_cells)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=4)

print("Notebook updated with Regularization code.")
