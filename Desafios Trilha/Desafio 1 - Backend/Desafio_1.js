// 1º):
let nome = "Bruno";
console.log(nome);

// 2º):
let idade = 25;
let altura = 1.75;
console.log(idade, altura);

// 3º):
let preco = 50;
let desconto = 0.2;
let precoDesconto = preco - (preco * desconto);

console.log(precoDesconto);

// 4º):
let temperatura = 30;

if (temperatura > 25){
    console.log("Está calor!");
}
else{
    console.log("Está fresco!");
}

// 5º):
let idade = 10;
if (idade >= 18){
    console.log("Você é maior de idade!");
}
else{
    console.log("Você é menor de idade!");
}

// 6º):
let nota = 7;

if (nota >= 7){
    console.log("Aprovado");
}
else{
    if (nota >= 5 && nota <= 6){
        console.log("Recuperação");
    }
    else{
        console.log("Reprovado");
    }
}

// 7º):
let numero1 = 5;
let numero2 = 6;
if (numero1 == numero2){
    console.log("Os números são iguais");
}
else{
    console.log("Os números são diferentes");
}

// 8º):
let nome = "Bruno";
let idade = 20;

console.log(`Olá, meu nome é ${nome} e eu tenho ${idade} anos`);

// 9º):
for (let i = 1; i <= 10; i++){
    console.log(i);
}

// 10º):
let numero = prompt("Digite um número: ");

while (numero != 5){
    numero = prompt("Digite um número:");
}

// 11º):
for (let i = 1; i <= 10; i++){
    console.log(`${i} x 7 = ${7 * i}`);
}

// 12º):
for (let i = 1; i <= 20; i++){
    if (i % 2 == 0){
        console.log(i);
    }
}

// 13º):
function calcularAreaCirculo(raio){
    let area = 3.14 * raio**2;
    return console.log(area);
}

calcularAreaCirculo(4);

// 14º):
// Definição dos valores de cada variável
let numero1 = 32;
let numero2 = 21;

// Definição de uma variável que vai receber a soma dos dois números
let soma = numero1 + numero2;

// impressão do resultado
console.log(soma);

// 15º):
function somarNumeros(numero1, numero2){
    let soma = numero1 + numero2;
    return console.log(soma);
}

somarNumeros(2, 5);
