let x;
var toast;
let toast_success = document.getElementsByClassName("success")[0];
let toast_error = document.getElementsByClassName("error")[0];
function showToast(type,messages) {
    clearTimeout(x);
    if(type=='error')
        toast=toast_error
    else
        toast=toast_success
    let message_node=toast.getElementsByClassName("message")[0];
    message_node.textContent=messages;
    toast.style.transform = "translateX(0)";
    x = setTimeout(() => {
        toast.style.transform = "translateX(400px)"
    }, 4000);
    
}
function closeToast() {
    toast.style.transform = "translateX(400px)";
    toast.style.display = "none"
}