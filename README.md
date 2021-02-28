# rd-tech-challenge

Este repositório contém o codigo utilizado no desafio técnico da RD Station.

O código foi escrito com enfâse na eficiência da execução. Algumas refatorações poderiam ser feitas
caso o código fosse ser reaproveitado por outras partes do sistema.

## Início rápido

Estando no diretório raiz do repositório, compile a imagem docker e suas dependências executando:

```bash
make build
```

Execute o código como no exemplo:

```bash
make run args="'[{\"id\": 1, \"value\": 10}, {\"id\": 2, \"value\": 20}]' '[{\"id\": 1, \"value\": 10}, {\"id\": 2, \"value\": 20}]' '[2]'"
```

Para mais informações, execute:

```bash
make run args="-h"
```

Para executar os testes automatizados, execute:

```bash
make test
```
