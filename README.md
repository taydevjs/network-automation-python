# Automação de Configuração L2L 🚀

Este projeto foi desenvolvido para otimizar o provisionamento de serviços de rede, transformando uma tarefa manual e repetitiva em um processo automatizado e seguro.

## 📝 Sobre o Projeto
Como Assistente de NOC, identifiquei a necessidade de padronizar a geração de scripts para configurações de L2L. Utilizando **Python**, criei uma ferramenta que coleta parâmetros variáveis e gera o bloco de comandos completo.

## 🛠️ Funcionalidades
- **Coleta Dinâmica:** Entrada de dados via terminal para VLANs, VPLS IDs e Seriais de ONT.
- **Tratamento de Dados:** Uso de lógica de strings (`split`) para extrair coordenadas de hardware (Rack/Shelf/Slot).
- **Segurança:** Tratamento de exceções com `try/except` para garantir que erros de digitação não quebrem a automação.
- **Saída Estruturada:** Geração de script pronto para cópia e aplicação.

## 🚀 Tecnologias Utilizadas
- **Python 3.x**
- **Git/GitHub** para versionamento.

## 📖 Como executar
1. Clone o repositório: `git clone https://github.com/taydevjs/network-automation-python.git`
2. Execute o script: `python gerador_l2l.py`
3. Siga as instruções no terminal.

---
*Desenvolvido por Tayna Brandão como demonstração de competências técnicas em automação e desenvolvimento de sistemas.*
