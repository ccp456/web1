function setcookie(name, value){
    var first_name = ["Able","Droit","Lean"];
    var second_name = ["Sword","farmer","Knight"];
    var n1 = Math.floor((Math.random()*first_name.length)); 
    var n2 = Math.floor((Math.random()*second_name.length));
    document.cookie = "name=" + first_name[n1] + " " + second_name[n2];
    history.go(0);
}