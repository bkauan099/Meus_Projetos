package SmartPhone.celular;

import SmartPhone.funcionalidades.AparelhoTelefonico;
import SmartPhone.funcionalidades.NavegadorInternet;
import SmartPhone.funcionalidades.ReprodutorMusical;

public class Iphone implements AparelhoTelefonico, NavegadorInternet, ReprodutorMusical {

    public void ligar(String numero) {
        System.out.println("Ligando para o número: " + numero);
    }

    public void atender() {
        System.out.println("Atendendo Telefone!");
    }

    public void iniciarCorreioVoz() {
        System.out.println("Iniciando correio de voz");
    }

    public void exibirPagina(String url) {
        System.out.println("Exibindo página de URL: " + url);
    }

    public void adicionarNovaAba() {
        System.out.println("Adicionando nova aba");
    }

    public void atualizarPagina() {
        System.out.println("Atualizando página!");
    }

    public void tocar(String musica) {
        System.out.println("Tocando música: " + musica);
    }

    public void pausar() {
        System.out.println("Música pausada");
    }

    public void selecionarMusica(String musica) {
        System.out.println(musica + " selecionada!");
    }
}