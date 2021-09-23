console.log("Correcto")

document.querySelector("#boton").addEventListener("click", traerDatos);

function ele(eletrodomesticoF) {
    this.eletrodomesticoF = eletrodomesticoF;
    }

function traerDatos(){
    console.log("en la funcion")
    var eletrodomesticoE = document.getElementsByName("eletrodomestico")[0].value;
    document.getElementById("elementos").innerHTML = eletrodomesticoE
    console.log(eletrodomesticoE)
    alert(eletrodomesticoE);
    
    var elec = new ele(eletrodomesticoE);
    alert(elec.eletrodomesticoF);
    
    let elemento = document.querySelector("elementos");
    elemento.innerHTML = <td>${eletrodomesticoE}</td>

    // for(let elem of elec){
    //     elemento.innerHTML += `
    //     <tr>
    //         <td>${id="mostrar"}</td>
    //     </tr>
    // `     
    // }
}

