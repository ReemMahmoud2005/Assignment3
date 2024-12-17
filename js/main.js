var input_name=document.getElementById('name');
var link=document.getElementById('url');

var allproduct=[]

if(allproduct!=null){
allproduct=JSON.parse(localStorage.getItem('websites'));

display_all_websites();
 }
 input_name.addEventListener('keyup', function () {
    validateInput(input_name);
});

link.addEventListener('keyup', function () {
    validateInput(link);
});
// allproduct =JSON.parse(localStorage.getItem('websites') )|| [];-->instead of condition

function add_new_product(){
    var book = {
        name: input_name.value,
        url: link.value
    };
    if (validateInput(input_name) && validateInput(link)) {
        allproduct.push(book);
        localStorage.setItem('websites', JSON.stringify(allproduct));
        display_all_websites();
        clear_form();
    } else {
        alert("plese enter avalid url or valid name");
    }
}

function display_all_websites(){
    var crtona='';
    for(i=0;i<allproduct.length;i++){
        crtona= crtona+`<tr  > <th >${i+1}</th>
        <th>${allproduct[i].name}</th>
        <th><button class="btn btn-visit " onclick="window.open('http://${allproduct[i].url}') "><i class="fa-solid fa-eye me-2" style="color: #ffffff;"></i>visit</button></th>
        <th><button class="btn btn-delete " onclick='delete_element(${i})'><i class="fa-solid fa-trash-can me-2" style="color: #ffffff;"></i>delete</button></th></tr>`
    }
document.getElementById('tr').innerHTML=crtona;

    
}
function delete_element(index) {
    allproduct.splice(index, 1);
    display_all_websites();
    localStorage.setItem('websites', JSON.stringify(allproduct));
}
function validateInput(input) {
    if (input.id === 'name') {
        if (input.value === "" || input.value.length < 3 || containsNonEnglish(input.value)) {
            document.getElementById('name').className = 'form-control input-error'; 
            return false;
        } else {
            document.getElementById('name').className = 'form-control input-success';  
            return true;
        }
    }

    if (input.id === 'url') {
        if (input.value === "" || !isValidUrl(input.value)) {
            document.getElementById('url').className = 'form-control input-error'; 
            return false;
        } else {
            document.getElementById('url').className = 'form-control input-success';  
            return true;
        }
    }
}
function containsNonEnglish(text) {
    for (var i = 0; i < text.length; i++) {
        var char = text[i];
        if ((char < 'A' || char > 'Z') && (char < 'a' || char > 'z') && char !== ' ') {
            return true; 
        }
    }
    return false;
}

function isValidUrl(url) {
    return url.startsWith("www.") && url.endsWith(".com");
}

function search(term){
   
     var cartona=''
    for(var i=0;i<allproduct.length;i++){

        if (allproduct[i].name.toLowerCase().includes(term.toLowerCase())){
            cartona=cartona+`<tr  > <th >${i+1}</th>
        <th>${allproduct[i].name}</th>
        <th><button class="btn btn-visit " onclick="window.open('http://${allproduct[i].url}') "><i class="fa-solid fa-eye me-2" style="color: #ffffff;"></i>visit</button></th>
        <th><button class="btn btn-delete " onclick='delete_element(${i})'><i class="fa-solid fa-trash-can me-2" style="color: #ffffff;"></i>delete</button></th></tr>`
    

        }
    }
    document.getElementById('tr').innerHTML=cartona;
}

function clear_form() {
    document.getElementById('name').value = '';
    document.getElementById('url').value = '';
    document.getElementById('name').classList.remove('input-error', 'input-success');
    document.getElementById('url').classList.remove('input-error', 'input-success');
}



