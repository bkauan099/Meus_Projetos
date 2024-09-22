package SmartPhone.Donos;

import SmartPhone.celular.Iphone;

public class IphoneDePedro {

    public static void main(String[] args) {
        Iphone iphone = new Iphone();

        // Funcionalidades de AparelhoTelefonico
        iphone.ligar("123456789");
        iphone.atender();
        iphone.iniciarCorreioVoz();

        // Funcionalidades de NavegadorInternet
        iphone.exibirPagina("www.example.com");
        iphone.adicionarNovaAba();
        iphone.atualizarPagina();

        // Funcionalidades de ReprodutorMusical
        iphone.tocar("Minha Música");
        iphone.pausar();
        iphone.selecionarMusica("Outra Música");
    }
}
