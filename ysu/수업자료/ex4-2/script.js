const content = "Welcome to the HwangBBang's World";

const text1 = document.querySelector(".text1")

let index = 0; 


function typing(){
    
    text1.textContent += content[index++];
    
    if(index > content.length){

        text1.textContent = ""
        index = 0; 
    } 
    
}

setInterval(typing, 1000)