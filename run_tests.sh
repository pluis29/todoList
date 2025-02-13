#!/bin/bash

echo "Executando testes unitários e de integração..."
pytest tests/ --disable-warnings -v

if [ $? -eq 0 ]; then
  echo "Todos os testes passaram com sucesso!"
else
  echo "Alguns testes falharam. Verifique o log acima para mais detalhes."
fi