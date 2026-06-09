# =========================================================
# EDA COMPLETO — A3
# Predição de Risco Cardiovascular com IA
# =========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração dos gráficos
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# =========================================================
# 1. CARREGAR DATASET
# =========================================================

df = pd.read_csv('heart (1).csv')

print("\nPRIMEIRAS LINHAS:")
print(df.head())

print("\nTAMANHO DO DATASET:")
print(df.shape)

print("\nCOLUNAS:")
print(df.columns)

# =========================================================
# 2. INFORMAÇÕES GERAIS
# =========================================================

print("\nINFORMAÇÕES DO DATASET:")
print(df.info())

print("\nESTATÍSTICAS DESCRITIVAS:")
print(df.describe())

print("\nVALORES NULOS:")
print(df.isnull().sum())

print("\nVALORES DUPLICADOS:")
print(df.duplicated().sum())

# =========================================================
# 3. DISTRIBUIÇÃO DA VARIÁVEL ALVO
# =========================================================

sns.countplot(x='target', data=df)
plt.title('Distribuição de Pacientes com e sem Doença Cardíaca')
plt.xlabel('Doença Cardíaca')
plt.ylabel('Quantidade')
plt.xticks([0, 1], ['Sem Doença', 'Com Doença'])
plt.show()

# =========================================================
# 4. DISTRIBUIÇÃO DA IDADE
# =========================================================

sns.histplot(df['age'], bins=20, kde=True)
plt.title('Distribuição da Idade dos Pacientes')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

# =========================================================
# 5. IDADE X DOENÇA CARDÍACA
# =========================================================

sns.boxplot(x='target', y='age', data=df)
plt.title('Idade e Doença Cardíaca')
plt.xlabel('Doença Cardíaca')
plt.ylabel('Idade')
plt.xticks([0, 1], ['Sem Doença', 'Com Doença'])
plt.show()

# =========================================================
# 6. COLESTEROL X DOENÇA CARDÍACA
# =========================================================

sns.boxplot(x='target', y='chol', data=df)
plt.title('Colesterol e Doença Cardíaca')
plt.xlabel('Doença Cardíaca')
plt.ylabel('Colesterol')
plt.xticks([0, 1], ['Sem Doença', 'Com Doença'])
plt.show()

# =========================================================
# 7. PRESSÃO ARTERIAL X DOENÇA CARDÍACA
# =========================================================

sns.boxplot(x='target', y='trestbps', data=df)
plt.title('Pressão Arterial e Doença Cardíaca')
plt.xlabel('Doença Cardíaca')
plt.ylabel('Pressão Arterial')
plt.xticks([0, 1], ['Sem Doença', 'Com Doença'])
plt.show()

# =========================================================
# 8. MAPA DE CORRELAÇÃO
# =========================================================

plt.figure(figsize=(14, 10))

correlation = df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Mapa de Correlação das Variáveis')
plt.show()

# =========================================================
# 9. CORRELAÇÃO COM A VARIÁVEL TARGET
# =========================================================

print("\nCORRELAÇÃO DAS VARIÁVEIS COM TARGET:")
print(correlation['target'].sort_values(ascending=False))

# =========================================================
# 10. CONCLUSÕES INICIAIS
# =========================================================

print("\nCONCLUSÕES DO EDA:")

print("""
1. O dataset possui 1025 registros e 14 variáveis.

2. A variável target indica a presença ou ausência de doença cardíaca.

3. A análise exploratória permite observar padrões entre idade,
colesterol, pressão arterial e presença de doença cardiovascular.

4. O mapa de correlação ajuda a identificar quais variáveis possuem
maior associação com o risco cardiovascular.

5. Os resultados do EDA servirão como base para a próxima etapa:
pré-processamento e treinamento dos modelos de Machine Learning.
""")
print(df.shape)

from sklearn.model_selection import train_test_split

# Remover duplicados
df = df.drop_duplicates()

print("Dataset limpo:", df.shape)

# Separar X e y
X = df.drop('target', axis=1)
y = df['target']

# Dividir treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Treino:", X_train.shape)
print("Teste:", X_test.shape)
from sklearn.preprocessing import StandardScaler

# Criar scaler
scaler = StandardScaler()

# Ajustar nos dados de treino
X_train_scaled = scaler.fit_transform(X_train)

# Aplicar nos dados de teste
X_test_scaled = scaler.transform(X_test)

print("Padronização concluída!")

from sklearn.linear_model import LogisticRegression

modelo_lr = LogisticRegression(max_iter=1000)

modelo_lr.fit(X_train_scaled, y_train)

print("Modelo Logistic Regression treinado!")

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

pred_lr = modelo_lr.predict(X_test_scaled)

print("Accuracy:")
print(accuracy_score(y_test, pred_lr))

print("\nRelatório:")
print(classification_report(y_test, pred_lr))

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

modelo_rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

modelo_rf.fit(X_train, y_train)

pred_rf = modelo_rf.predict(X_test)

print("Accuracy Random Forest:")
print(accuracy_score(y_test, pred_rf))

print("\nRelatório Random Forest:")
print(classification_report(y_test, pred_rf))
import pandas as pd

importancias = pd.DataFrame({
    'Variavel': X.columns,
    'Importancia': modelo_rf.feature_importances_
})

importancias = importancias.sort_values(
    by='Importancia',
    ascending=False
)

print(importancias)