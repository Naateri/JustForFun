//Si tu numero es menor a 70 imprime el numero si no te pide que lo metas de nuevo

function askNumber(){
	var num;
	num = prompt("Ingrese un numero: ");
	return num;
}

function main(){
	var num = askNumber();
	if (num < 70){
		console.log("Ingrese otra vez.");
		main();
	} else {
		console.log("Lo lograste!");
	}
	console.log("Supuestamente funciona! xd");
}

main()
