// console.log("Correcto")

function ele(eletrodomesticoF) {
    this.eletrodomesticoF = eletrodomesticoF;
    }

function traerDatos(){
    console.log("en la funcion")
    var eletrodomesticoE = document.getElementsByName("eletrodomestico")[0].value;

    var elec = new ele(eletrodomesticoE);
    alert(elec.eletrodomesticoF);

    const xhttp = new XMLHttpRequest();
    const url = "http://127.0.0.1:5500/FrondEnd/templates/index.html"
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            console.log(this.responseText);
            document.getElementById("elementos").innerHTML = this.responseText;
        }
    }

    xhttp.open("GET", url);
    xhttp.send();

    document.querySelector("#boton").addEventListener("click", function(){
        traerDatos();
    });
    let elemento = document.querySelector("#elementos");
    elemento.innerHTML = "" ;

    for(let elem of elec){
        elemento.innerHTML += `
        <tr>
            <td>${elem.eletrodomesticoF}</td>
        </tr>
    `     
    }
}