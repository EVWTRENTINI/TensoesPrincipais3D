# Análise de Tensões Principais em Elementos 3D

Este repositório contém um script Python para a visualização de tensões principais em um elemento 3D. O script calcula as tensões principais de um tensor de tensão dado e as exibe graficamente em um elemento rotacionado, representando as direções e magnitudes das tensões.

## Execução sem instalação

Para executar este script remotamente acesse esse <a href="https://trinket.io/python3/67dca2b63c" target="_blank">link</a> e clique no icone de play. 

## Utilização

### Mudando o Tensor de Tensão

Para alterar o tensor de tensão, modifique o array `tensor` no início do script. O tensor é definido como um array NumPy 3x3, representando as componentes de tensão no elemento. Por exemplo:

```python
tensor = np.array([[-30.,  40.,   0.],
                   [ 40.,  50., -50.],
                   [  0., -50., -50.]])
```      

## Requisitos

Para executar este script em seu computador local, você precisará, além de Python, das seguintes bibliotecas Python:

- matplotlib
- numpy

## Instalação

Para instalar as bibliotecas necessárias, você pode usar o seguinte comando:

```bash
pip install matplotlib numpy
```

## Uso

Para usar este script, basta clonar o repositório e executar o arquivo `Tensões principais.py`:

```bash
git clone https://github.com/EVWTRENTINI/TensoesPrincipais3D
cd TensoesPrincipais3D
python Tensões principais.py
```

O script gerará um gráfico 3D que mostra um elemento com vetores representando as tensões principais. Uma legenda é incluída para indicar os valores das tensões principais.



## Screenshots
<p align="center">
  <img src="Screenshots/Screenshot_1.jpg" width="600" title="Screenshot 1">
</p>

## Links
* __Email para contato__: [etrentini@ufu.br](mailto:etrentini@ufu.br)
