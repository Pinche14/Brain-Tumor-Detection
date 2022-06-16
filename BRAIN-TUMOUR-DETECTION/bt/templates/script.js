// selecting all reequired elements
const dropArea = document.querySelector(".drag-area");
dragText=dropArea.querySelector("header");
button=dropArea.querySelector("button");
input=dropArea.querySelector("input");

let file; //this is a global variable and we'll use it inside multiple functions

button.onclick=()=>{
    input.click();
}

input.addEventListener("change",function(){
    file=this.files[0];
    showFile();
    dropArea.classList.add("active");
});


// If user drags file over dragarea
dropArea.addEventListener("dragover",(event)=>{
    event.preventDefault(); //preventing from default behaviour
    console.log("File is over DragArea");
    dropArea.classList.add("active");
    dragText.textContent="Release to Upload File";
    });

// If user leaved dragged file from dragarea
dropArea.addEventListener("dragleave",()=>{
    console.log("File is outside dragarea");
    dropArea.classList.remove("active");
    dragText.textContent="Drag & Drop to Upload File";
    });

// If user drops file over dragarea
dropArea.addEventListener("drop",(event)=>{
    event.preventDefault(); //preventing from default behaviour
    console.log("File is dropped on dragarea");
    file=event.dataTransfer.files[0];
    showFile();
    });

function showFile(){
    let fileType=file.type;
    console.log(file);

    let validExtensions= ["image/jpeg","image/jpg","image/png","image/jpeg",
                            "image/gif","image/pdf","image/bmp","image/tiff"]
    if(validExtensions.includes(fileType)){
    console.log("This is an Image file");
    let fileReader=new FileReader();
    fileReader.onload=()=>{
    let fileURL=fileReader.result; //fileurl contains BAse64 image url
    document.getElementById("image").value = fileURL;
    console.log(fileURL);
    console.log(document.getElementById("image").value)
    let imgTag=`<img src="${fileURL}" alt="">`;
    dropArea.innerHTML = imgTag;
    }
    fileReader.readAsDataURL(file);
    }else{
    alert("This is not an Image file !");
    dropArea.classList.remove("active");
    }
}