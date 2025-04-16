📊 Dashboard Interativo - Exemplo com Streamlit e Plotly
Este projeto apresenta um dashboard interativo desenvolvido com Streamlit e Plotly, utilizando dados simulados de vendas diárias. O objetivo é demonstrar como construir visualizações dinâmicas e filtros interativos em Python de forma simples e elegante.

🚀 Funcionalidades
Filtros interativos na barra lateral para seleção de Categoria e Região

Gráfico de Barras agrupado por categoria e colorido por região

Gráfico de Dispersão das vendas ao longo do tempo

Gráfico de Linhas com evolução temporal das vendas por categoria

Exibição de métricas resumidas: total, média e número de transações

Tabela de dados com os resultados filtrados

Atualização automática das visualizações com base nos filtros

📦 Tecnologias Utilizadas
Python 3.7+

Streamlit

Plotly Express

Pandas

NumPy

🛠️ Como Executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/RerissonHRS/AnaliseDadosStreamlite
Crie um ambiente virtual (opcional mas recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Exemplo de requirements.txt:

nginx
Copiar
Editar
streamlit
plotly
pandas
numpy
Execute o aplicativo:

bash
Copiar
Editar
streamlit run dashboard.py
O navegador será aberto automaticamente em http://localhost:8501.

🧪 Estrutura dos Dados
O conjunto de dados é gerado aleatoriamente com as seguintes colunas:

Data: Datas diárias de 2023

Vendas: Valor de vendas (100 a 1000)

Categoria: Classificação dos produtos (A, B, C)

Região: Região geográfica (Norte, Sul, Leste, Oeste)

📷 Captura de Tela (opcional)
Adicione uma imagem mostrando o dashboard em funcionamento para melhorar a apresentação.

📌 Observações
O projeto utiliza dados aleatórios apenas para fins de demonstração.

Você pode adaptar a lógica para carregar dados reais de um CSV, banco de dados, API, etc.

📄 Licença
Este projeto é livre para uso e modificação.
