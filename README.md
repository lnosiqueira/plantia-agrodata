# 🌱 **PlantIA Agrodata**

## 📌 **Descrição do Projeto**
O **PlantIA Agrodata** é uma solução inteligente para análise e monitoramento de dados agrícolas, integrando informações climáticas, indicadores de solo e produtividade. O objetivo é fornecer insights para otimizar a produção e reduzir riscos no agronegócio.

---

## 🎯 **Objetivos**
- Centralizar dados agrícolas em um dashboard intuitivo.
- Oferecer previsões climáticas integradas.
- Visualizar indicadores com gráficos avançados (Gauge e Donut).
- Garantir escalabilidade para integração com IoT e Machine Learning.

---

## 🛠 **Tecnologias Utilizadas**
- **Python 3.10+** (Backend e análise)
- **SQL (MySQL/PostgreSQL)** (Banco de dados)
- **C/C++** (Módulos de alto desempenho)
- **Flask** (Servidor web)
- **Chart.js / Plotly** (Visualização gráfica)

---

## 🏗 **Arquitetura do Sistema**
- **Camada de Dados**: Banco SQL para armazenar culturas, clima e sensores.
- **Camada de Processamento**: Scripts Python para análise e integração.
- **Camada de Visualização**: Dashboard web com gráficos dinâmicos.

---

## 🚀 **Como Executar o Projeto**
1. **Pré-requisitos**
   ```bash
   pip install -r requirements.txt
   ```
2. **Configuração do Banco**
   ```sql
   CREATE DATABASE plantia_agrodata;
   ```
3. **Configuração do .env**
   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASS=sua_senha
   API_KEY=chave_api_previsao_tempo
   ```
4. **Executando**
   ```bash
   python app.py
   ```
   Acesse: `http://localhost:5000`

---

## 📊 **Exemplos de Uso**
```python
from plantia import AgroData
db = AgroData()
dados = db.get_cultura("soja")
print(dados)
```
- **Dashboard**: Gráficos Gauge (umidade) e Donut (distribuição).
- **Previsão do Tempo**: Temperatura, chuva, índice UV.

---

## 🎨 **Identidade Visual FIAP**
- **Cores**: #E60012 (vermelho), #FFFFFF (branco), #000000 (preto)
- **Fontes**: Montserrat (títulos), Roboto (textos)
- Logo: `/assets/logo_fiap.png`

---

## 🛣 **Roadmap**
- [ ] Integração IoT
- [ ] Machine Learning para previsão de safra
- [ ] Exportação PDF
- [ ] Dashboard responsivo

---

## 👥 **Integrantes do Grupo** <a name="integrantes"></a>
| Nome | RM |
|------|----|
| [**Leno Siqueira**](https://www.linkedin.com/in/leno-siqueira-36789544) | **RM567893** |
| [**Fred Villagra**](https://www.linkedin.com/in/federico-villagra-97378838a) | **RM567187** |
| [**Paulo Benfica**](https://www.linkedin.com/in/paulo-benfica-76057a7b) | **RM567648** |
| [**Maria Mendes**](https://www.linkedin.com/in/andr%C3%A9a-mendes-b8959238a) | **RM568563** |
| [**Mateus Lima**](https://www.linkedin.com/in/math-penteado-1b4807200) | **RM568518** |

---

## 🧑‍🏫 **Professores** <a id="professores"></a>
**Tutor(a)**  
- [**Sabrina Otoni**](https://www.linkedin.com/in/sabrina-otoni-22525519b)

**Coordenador(a)**  
- [**André Godoi**](https://www.linkedin.com/company/inova-fusca)

---

## 🏷 **Badges**
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Database](https://img.shields.io/badge/Database-MySQL/PostgreSQL-green)
![FIAP](https://img.shields.io/badge/Powered%20by-FIAP-red)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

---

## 🔗 **Repositório**
https://github.com/seu-repositorio-aqui

---

## 🤝 **Contribuição**
1. Faça um fork do projeto.
2. Crie uma branch: `git checkout -b minha-feature`.
3. Commit: `git commit -m 'Minha feature'`.
4. Push: `git push origin minha-feature`.
5. Abra um Pull Request.

---

## 📄 **Licença**
Este projeto está sob a licença MIT.
