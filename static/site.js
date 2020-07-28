$("#envia-receita").click(enviaReceita);

function enviaReceita() {
//    var params = {
//        "pessoa": "Vittor sei la vaitomanocu vacilao",
//        "nome_receita": "Bacanal",
//        "ingredientes": "Sexo anal",
//        "modo_de_preparo": "Sei la pelo amor de deus",
//        "tempo_de_preparo": "600",
//        "rendimento": "serve 7 pessoas",
//        "categoria": "Sexo"
//    }

    var filtro = {pessoa:'Vittor Valler Custodio'};
    var url = "https://appreceitas.herokuapp.com/api/lista-receitas/"
    $.ajax({
        url: url,
        type: 'get',
        data: filtro,
        success: recebeReceita,
        error: function(xhr) {
        console.log('Erro')},
        });


//    fetch(url)
//    .then((resp) => resp.json())
//    .then(recebeReceita);
}

function recebeReceita(dados) {
    console.log(dados);
}