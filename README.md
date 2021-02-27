# rd-tech-challenge

Este repositório contém o codigo utilizado no desafio técnico da RD Station.

O código foi escrito com enfâse na eficiência da execução. Algumas refatorações poderiam ser feitas
caso o código fosse ser reaproveitado por outras partes do sistema.

## Início rápido

Estando no diretório raiz do repositório, compile a imagem docker e suas dependências executando:

```bash
docker build --tag rd-tech-challenge .
```

Execute o código como no exemplo:

```bash
docker run --rm rd-tech-challenge python3 src/customer_success_balancing.py '[{"id": 1, "value": 10}, {"id": 2, "value": 20}]' '[{"id": 1, "value": 10}, {"id": 2, "value": 20}]' '[2]'
```

Para executar os testes automatizados, execute:

```bash
docker run --rm rd-tech-challenge python3 -m unittest tests.test_customer_success_balacing.TestCustomerSuccessBalancing
```
