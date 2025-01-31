// 1º):
nome = "Bruno"
console.log(nome);

// 2º):
idade = 25;
altura = 1.75;
console.log(idade, altura);

// 3º):
preco = 50;
desconto = 0.2;
precoDesconto = preco - (preco * desconto);

console.log(precoDesconto);

// 4º):
temperatura = 30

if (temperatura > 25){
    console.log("Está calor!");
}
else{
    console.log("Está fresco!")
}

// 5º):
idade = 10 
if (idade >= 18){
    console.log("Você é maior de idade!")
}
else{
    console.log("Você é menor de idade!")
}

// 6º):
nota = 7

if (nota >= 7){
    console.log("Aprovado")
}
else{
    if (nota >= 5 && nota <= 6){
        console.log("Recuperação") 
    }
    else{
        console.log("Reprovado")
    }
}

// 7º):
numero1 = 5
numero2 = 6
if (numero1 == numero2){
    console.log("Os números são iguais")
}
else{
    console.log("Os números são diferentes")
}

// 8º):
nome = "Bruno"
idade = 20

console.log(`Olá, meu nome é ${nome} e eu tenho ${idade} anos`)

// 9º):
for (i = 1; i <= 10; i++){
    console.log(i)
}

// 10º):
numero = prompt("Digite um número: ")

while (numero != 5){
    numero = prompt("Digite um número:")
}

// 11º):
for (i = 1; i <= 10; i++){
    console.log(`${i} x 7 = ${7 * i}`)
}

// 12º):
for (i = 1; i <= 20; i++){
    if (i % 2 == 0){
        console.log(i)
    }
}

// 13º):
function calcularAreaCirculo(raio){
    area = 3.14 * raio**2
    return console.log(area)
}

calcularAreaCirculo(4)

// 14º):
// Definição dos valores de cada variável
numero1 = 32
numero2 = 21

// Definição de uma variável que vai receber a soma dos dois números
soma = numero1 + numero2

// impressão do resultado
console.log(soma)

// 15º):
function somarNumeros(numero1, numero2){
    soma = numero1 + numero2
    return console.log(soma)
}

somarNumeros(2, 5)
