let name = document.getElementById('name');
console.log(name.value);
function name1() {
    if(name.value.length >3  ){
        name.value = 100
        console.log(name.value);

    }else if( name.value < 0){
        name.value = 0
        console.log(name.value);

    }
}
name.addEventListener('input',name1)